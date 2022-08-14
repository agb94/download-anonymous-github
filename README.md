# Cloning from Anonymous GitHub

Want to download an anonymized repository from [https://anonymous.4open.science/](https://anonymous.4open.science/)?

1. Clone this repository and install the dependency
```shell
git clone https://github.com/agb94/download-anonymous-github
cd download-anonymous-github
pip install requests
```

2. Download an anonymized repository
```shell
# To download https://anonymous.4open.science/r/<repo>
python download.py <repo> --savedir <dir>
```
If you don't provide `--savedir` option, it is automatically set to `<repo>`.

For example,
```shell
python download.py 840c8c57-3c32-451e-bf12-0e20be300389 --savedir sample
```
this command will clone the repository [https://anonymous.4open.science/r/840c8c57-3c32-451e-bf12-0e20be300389](https://anonymous.4open.science/r/840c8c57-3c32-451e-bf12-0e20be300389) to `sample/`.

If you want to only download python files and the readme so that large files are ignored use the `--file-types` option with the file types that you want, in this case `.md` and `.py`
```shell
python download.py 840c8c57-3c32-451e-bf12-0e20be300389 --savedir sample --file-types .md .py
```
