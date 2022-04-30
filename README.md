# Download Anonymous GitHub

Download an anonymized repository from [https://anonymous.4open.science/](https://anonymous.4open.science/)

```shell
git clone https://github.com/agb94/download-anonymous-github
cd download-anonymous-github
pip install requests
python download.py [repo] --savedir [dir]
```

For example,
```shell
python download.py 840c8c57-3c32-451e-bf12-0e20be300389 --savedir sample_repo
```
this command will download the repository [https://anonymous.4open.science/r/840c8c57-3c32-451e-bf12-0e20be300389](https://anonymous.4open.science/r/840c8c57-3c32-451e-bf12-0e20be300389) to `sample_repo/`.

