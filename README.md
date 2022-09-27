# Python Flask REST API
This repository demonstrates an implementation of a simple REST API with Python and Flask.

### API Features

- A Simply REST API implementation with a single parameterized hello world endpoint `/user-id`
- A greeting message is returned for `/1`, `/2`, `/3`. Other numeric values in the path variable will return `Hello, World!` by default.
- `AppService` is a simple Data Access Object (DAO) that reads JSON data from `users.json`.

### Running locally

- Download Python 3.7 from https://www.python.org/downloads. Ensure both `python` and `pip` binary locations are available in the `PATH` environment variable.
- Install the dependency with `pip install -r requirements.txt`.
- Run the server with the command `python -m flask run --host=0.0.0.0`.
- These steps are documented in `Dockerfile`.

### Running as Docker container

- The application can be run via Docker. Docker has the benefit of shipping the application software together with its runtime dependencies and configurations.
- To create the Docker build, make sure you are authenticated to the container registry (e.g. Dockerhub) and execute the command `docker build -t <USER_NAME>:python-flask-restapi-0.0.1`, where `USER_NAME` is your container registry login ID and `0.0.1` is the version number for the build.
- Push the docker build to the container registry using the command `docker push <USER_NAME>:python-flask-restapi-0.0.1`.
- On the remote server, login to the container registry (e.g. Dockerhub), pull and run the image with the command `docker run --restart always <USER_NAME>:python-flask-restapi-0.0.1`.
- Docker makes it a very reliable way of deploying containers at scale. For example, the image can be pulled into AWS ECS (Elastic Container Services) or a fleet of EC2 instances using automatic bootstrap startup script, which can be used in combination with AWS Application Load Balancer (ALB) and Auto Scaling features to create a very robust service.

### Static code checking and unit testing

- Few tests implemented with `unittest` library are provided along with this example.
- `test/test_unit.py` demonstrates the unit tests written for the `AppService` class.
- `test/test_app.py` demonstrates the integration tests written for the entire API service. Note that it is expected to turn on the server process before the integration tests can be executed.
- Execute the command `python -m unittest discover` to run all tests.
- The coverage report can be obtained with the command `coverage run -m unittest discover`. HTML formatted coverage report can be generated using `coverage report` command. In this example, a coverage of 89% is reached.
- Pylint is the static code analysis tool in this project. For example, run `pylint app.py` and observe that a score of 100% is attained.
- Detailed code analysis can be supported by SonarQube (https://www.sonarqube.org) which is beyond the scope of this demo application.
- Continuous integration is supported with Travis CI in this example. `.travis.yml` shows a simple configuration that specifies the Python runtime environment and the command to run the unit tests.
- Jenkins is another CI platform for similar purpose. I recommend that Jenkins can automate the mentioned steps (e.g. Pylint, unittest, coverage, sonarqube), and only if these steps are meeting the code quality requirements, the docker build and push steps should be triggered.


### Changes and version control

- A separate code branch `random_names` with one single commit is created to demonstrate the use of feature branch in the development.
- The commit aims to support a list of names for each user instead of just a name. The API will return a randomized name using Python's `random.choice()` function.
- The data migration is straightforward - use an array in flavor of a String variable to contain the user names.
- Unit tests need to be updated to reflect the change in data structure from String to array as well as the randomized behavior.


