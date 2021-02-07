# DevOps Apprenticeship: Project Exercise

## Getting started

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from a bash shell terminal:

### Poetry installation (Bash)
```bash
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### On macOS and Linux
```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-line operation on first setup:
```bash
$ cp .env.template .env # (first time only)
```

The `.env` file is used by flask to set environment variables when running ` flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). 

In order to run this application you will require the appropriate trello information in the `.env` file. They are as follows
```
boardId=<your_board_id>
key=<your_key>
token=<your_token>
```

Once the setup script has completed and all packages have been installed, start the Flask app by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

# Running Tests
All tests can be run with pytest using the following commands
```bash
poetry run pytest test
```