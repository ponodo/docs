---
title: Installation
draft: false
description: |
    Ponodo is powerful MVC framework built on top of Python programming language. We agree that developing application should be fun and enjoyable, that's why Ponodo here.
section: Getting Started
---

## Requirements

### Install Pyenv

[Pyenv](https://github.com/pyenv/pyenv) make switching between Python version easier. Although you can use your native Python in your operating system, it will cumbersome if you manage projects that has different versions. Pyenv also feel powerful when combining with virtual environment.

How to install it please refer to official [Pyenv](https://github.com/pyenv/pyenv) documentation.

### Install Poetry

Ponodo use [Poetry](https://python-poetry.org/) to manage its dependencies. Just install as the documentation said and put the `poetry` binary in your `PATH` environment variable, then you ready to make awesome application. 

Using Poetry does not need install separate virtual environment anymore, Poetry has build in virtual environment. Unlike other programming language, Python utilize virtual environment to isolate dependencies among other projects.



### Install Ponodo Installer

Before using `pyenv` and `poetry`, make sure you has any `pip` version installed in your native system. Then execute command below to install Ponodo in your native system.

```bash
pip install ponodo
```

This will install `ponodo` as global command in your local machine, so you can run it anywhere.

## Setup Environment


First choose the python version that you want to use. For example you want to use python 3.10.2.

```bash
pyenv install 3.10.2
```

This will install python 3.10.2 inside directory `~/.pyenv/versions/3.10.2/`. Which in this case we need exact location of the binary file in the `~/.pyenv/versions/3.10.2/bin/python`.

The second step is create skeleton of your project using `ponodo` command.

```bash
ponodo new awesome
```


This command will create new directory `awesome` with content of working default Ponodo structure. Go to your project directory `cd awesome`, then tell poetry to use specific python binary.

```bash
poetry env use ~/.pyenv/versions/3.10.2/bin/python
```

Poetry utilizing file `pyproject.toml`. If you are in the wrong directory, command above will not run. Make sure to go to inside your working project directory and `pyproject.toml` exists inside your working directory.

After specify the python version, the third step is go inside virtual environment.


```
poetry shell
```

It will bring you into isolated environment. Poetry utilize virtual environment out of the box, and create random virtual environment name inside `.cache` directory. Poetry will tell you where is your virtual environment after command above ran.

Inside the virtual environment, now you can install the dependency using 

```shell
poetry install
```

It will install dependencies included with development dependencies. Poetry also create new file `poetry.lock` to lock the dependencies, this very useful to make installation faster for the next developer.


After dependencies installed you can run `wrap` executable python file that exists in the root project to help you working on the project. For example command below will give you lite webserver for development only.

```bash
python wrap server
```

By default, open `http://localhost:4000/` will bring you beautiful Ponodo welcoma page.