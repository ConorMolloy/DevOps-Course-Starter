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

In order to run this application you will require the appropriate Mongo information in the `.env` file. They are as follows
```
DB_URL=<url to your atlas cluster>
DB_NAME=<db name>
TODO_COLLECTION_NAME=<collection name>

CLIENT_ID=<github client id>
CLIENT_SECRET=<github client secret>

SECRET_KEY=<flask secret key>
OAUTHLIB_INSECURE_TRANSPORT=1

WRITER_USER=<hardcoded github user that has write access to the app>

TEST_COLLECTION=<another collection for e2e tests>
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
All tests can be run with pytest using the following commands, Firefox and the correct version of geckodriver.exe will be needed for the e2e test
```bash
poetry run pytest test
```

# Running in Docker
For this you will need docker installed on your machine.

To build and run a development docker container that will automatically update, run the fillowing commands
```bash
docker build --target development --tag todo-app:dev .
docker-compose up   
```

To build a production ready container using gunicorn instead of the dev server, run the following command
```bash
docker build --target production --tag todo-app:prod .    
```
In order for this to work as expected you will need to inject the .env file when you run the container
```bash
docker run -p 5000:5000 --env-file .env todo-app:prod
```

# Running the tests in Docker
To run the applications tests inside a docker container (what Travis does in the build pipleline) run 
```bash
docker build --target test --tag test-image .
```
to build the test container with all the dependencies, including a version of Firefox

To run the tests, unit, integration and e2e run the following
```bash
docker run test-image test/unit
docker run test-image test/integration
docker run --env-file .env test-image test/e2e
```

# Deployment Pipeline
When a PR is merged on this project the changes will be deployed to Heroku (https://devops-starter.herokuapp.com/) and a copy of the image will be pushed to DockerHub (https://hub.docker.com/repository/docker/mertmanable/todo-app)

# Auth
The app now supports OAuth sign-in with Github. Any user can read the apps data but only the user defined in the .env file will be able to write to the app.
