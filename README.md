# flask-app

A simple Flask application

## Requirements

Check that you have all the necessary tools and install them if you don't.

- Python
- pip
- Flask
- Git

Verify that you have them installed.

```sh
python3 --version
pip3 --version
flask --version
git --version
```

## Setup a virtual environment

In your project directory, we want to first create a `.venv` directory using [venv](https://docs.python.org/3/library/venv.html) and then activate it. This should be added to your `.gitignore` file so you don't check it in.

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

## Infrastructure

We use AWS CDK to provision our infrastructure.

Run the `cdk synth` command to check if everything is working correctly. This will generate a CloudFormation template based on the code in your stack and output it to the terminal.

```sh
cdk synth
```

To view the CloudFormation template for a given stack just provide the stack id.

```sh
cdk synth <your stack id>
```

Before deploying, run `cdk bootstrap` to set up resources that CDK requires (only needs to be done once).

```sh
cdk bootstrap
```

You should see a success message for your account id and region being bootstrapped.

```sh
✅  Environment aws://<your account id>/<your region> bootstrapped.
```

To deploy all stacks for the Singapore region.

```sh
cdk deploy --region ap-southeast-1
```

You can also deploy individual stacks only.

```sh
cdk deploy <your stack id> --region ap-southeast-1
```
