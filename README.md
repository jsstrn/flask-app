# flask-app

A simple Flask application

## Requirements

Check that you have all the necessary tools and install them if you don't.

- Python
- pip
- Flask
- Git

```sh
python3 --version
pip3 --version
flask --version
git --version
```

## Setup virtual environment

In your project directory, we want to first create a `.venv` directory and then activate it. This should be added to your `.gitignore` file so you don't check it in.

When you clone the project you have to create a new `.venv` directory and every time you open the project in a new shell you have to activate it again.

### Create `.venv` folder

Create a new folder called `.venv` at the root of the project.

```sh
python3 -m venv .venv
```

### Activate the environment

Next, activate the environment.

```sh
source .venv/bin/activate
```

You can use either `source` or `.`. They work exactly the same.

```sh
. .venv/bin/activate
```

### Verify that the environment is activated

Check that Python is called from within the `.venv` directory. You should be able to use `python` instead of `python3` in your working directory.

```sh
which python
```

### Install a specific version of Python

Let's say you want to install Python version 3.9.

```sh
pip install python=3.9
```

## Install dependencies

```sh
pip install -r requirements.txt
```

If you add new dependencies, lock them in the `requirements.txt` file.

```sh
pip freeze > requirements.txt
```

## Start development server

To start the development server on port 8080.

```sh
python app.py
```
