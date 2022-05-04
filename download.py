import requests
import os
import argparse
import time

api_url = "https://anonymous.4open.science/api/repo/"
repo_url = "https://anonymous.4open.science/r/"

def get_children(dirpath, path=""):
    all_files = []
    for key in dirpath:
        if len(dirpath[key]) == 1 and \
            'size' in dirpath[key] and \
            isinstance(dirpath[key]['size'], int):
            all_files.append(path + key)
        else:
            all_files += get_children(dirpath[key], path=path+key+"/")
    return all_files

def download_repo(repo, savedir, interval):
    print(f"Repository: {repo_url}/{repo}")
    print("Get the list of files..")
    r = requests.get(f"{api_url}/{repo}/files")
    root_dir = r.json()
    files = get_children(root_dir, path="")
    print(f"{len(files)} files are found.")

    downloaded_files = []
    for filepath in files:
        try:
            download_path = os.path.join(savedir, filepath)
            if os.path.exists(download_path):
                print(f"{download_path} already exists. Skipped")
                continue
            dirname = os.path.dirname(filepath)
            dirname = os.path.join(savedir, dirname)
            if dirname.strip() and not os.path.exists(dirname):
                os.makedirs(dirname, exist_ok=True)
            print(f"Downloading {filepath}...")
            os.system(f"wget {api_url}/{repo}/file/{filepath} -P {dirname}")
            downloaded_files.append(download_path)
            time.sleep(interval)
        except KeyboardInterrupt as e:
            raise e

    unavailable_files = [
        filepath for filepath in downloaded_files
        if not os.path.exists(filepath)
    ]

    return unavailable_files

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('repo', type=str)
    parser.add_argument('--savedir', type=str)
    parser.add_argument('--interval', type=float, default=1)
    args = parser.parse_args()
    repo = args.repo
    if args.savedir is None:
        savedir = repo
    else:
        savedir = args.savedir

    unavailable_files = download_repo(args.repo, savedir, args.interval)

    if unavailable_files:
        print(f"Unable to download files: {unavailable_files}")
    else: 
        print(f"The repository has been successfuly cloned to {os.path.abspath(savedir)}")
