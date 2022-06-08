# Installation

## Poetry

Make sure you has any pip version installed. Minimal version is 3.7

```
pip install ponodo
```

This will install Ponodo as global command in your local machine.

We recommend using [Pyenv](https://github.com/pyenv/pyenv) as development tool, which you can install various Python version in single machine.


```
ponodo new awesome
```

This command will create new directory `awesome` with content of working default Ponodo structure.

> If you to show list of ponodo command, just add `--help` option: `ponodo --help`.

Your project already created, but you cannot working on it now. The best practice
is using virtual environment to isolate your works from contamination of existing
project.

To use virtual environment and want to specific version of python, please install
python version that you want. We install it using `pyenv`

```shell
pyenv install python 3.10.3
```

Then locate the binary file of those python version. When using pyenv its usually in 
`~/.poetry/versions/3.10.3/bin/python`. Change the version accordingly. Then 

```shell
poetry env use ~/.poetry/versions/3.10.3/bin/python
```
to use specific python for poetry.

We recommend using Poetry as dependency manager as well as virtual environment. Inside the `awesome` directory:

```
poetry shell
```

It will bring you to isolated environment. Now you can install the dependency using 

```
poetry install
```

After dependency installed you can run `wrap` executable python file to help you accross the project.

```
python wrap server
```

will bring you to run local server.