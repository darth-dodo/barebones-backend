# barebones-backend
## Requirements
* Runs locally on port 8000 and accepts `GET` requests at the index URL `/`
* It checks that the request has a query parameter called `favoriteTree` with a valid value
* For a successful request, returns a properly encoded HTML document with the following content:

If `favoriteTree` was specified (e.g. a call like `127.0.0.1:8000/?favoriteTree=baobab`):

```
It's nice to know that your favorite tree is a <value of "favoriteTree" from the url> 
```

if not specified (e.g. a call like `127.0.0.1:8000/`):

```
Please tell me your favorite tree
```
---
## Backend Features
- Simple HTTP server with whitelisted HTTP methods *(SHA: d443bac5310ed8c7a5373e624868616feb62fa28)*
- Index Controller for knowing the Favorite Tree *(SHA: d443bac5310ed8c7a5373e624868616feb62fa28)*
- Multithreaded Server *(SHA: d443bac5310ed8c7a5373e624868616feb62fa28)*
- Barebones Test Cases *(SHA: 6f7da48c1364c76052f593aa7fd6ae25bfe016fd)*
- Barebones Controller *(SHA: 567602907b77288cbc6096586278d278b4710a96)*
- 404 handler and DRY headers logic *(SHA: 567602907b77288cbc6096586278d278b4710a96)* 
- Index Controller logic refactor *(SHA: b9ee7598a366c5ec750d24d7729276a119447f90)*
- Simple Docker container *(SHA: 98e3769029b8879d4ff4de63c879ae9d2b1eff05)*
    


---
## Python env
- The project uses Python 3.7. Use [PyEnv](https://github.com/pyenv/pyenv) to install the required version
- Python environment in managed through [Poetry](https://python-poetry.org/)
- Install the project virtual env and packages using the command. **Make sure you have set the `local` Python version to 3.7**
```sh
poetry install
```
- Start the project virtual env using the command
```
poetry shell
```
- To check out more details about your virtualenv please run the command
```sh
poetry env info
```
- In case of questions, please checkout the guide to maintaining virtual envs and python versions with over [here](https://python-poetry.org/docs/managing-environments/)

## Application Details
- Python 3.7
- Basic server using `http.server` 
- Tests using `unittest`
- Code autoformatter using [`black`](https://github.com/psf/black)
- The application is divided into three components
    - `barebones_server` is where the server logic resides; it includes routing, response generations and starting the multithreaded server
    - `barebones_routes` is where the application routes and route handlers are mapped
    - `barebones_controllers` is where the application controller logic reside

## API details
- Please enter the information as mentioned in the requirements
- In case, the value of favorite tree is kept blank, it will ask the default question

## Commands
- Install the dependency (`black`) using the command
```bash
poetry install
```
- Autoformat the code using `black` with the command
```bash
black .
```
- Run the application using Docker with the command
```bash
docker-compose up
```
- Run the server using the command
```bash
python barebones_server.py
```
- Run the test cases using the command
```bash
python -m unittest test_barebones_server.py
```

## Next Steps
- Precommit hooks using pre-commit eg: https://github.com/darth-dodo/hackernews-backend/blob/master/.pre-commit-config.yaml
- Setting using CI and CD using Github actions/Travis/Circle CI
- Using Python 3 type hints for more robust code
- Better application/project structuring using packages such as "app", "tests"
- Using something more robust like wsgi for creating the core Backend (or Bottle/Flask/Django)
- Creating Class based template parsers which are similar to `jinja` templating engine
- More efficient route definition using regex
- Using `typing.NamedTuples` for creating more structure while defining a route
- Adding Method support in the route definition
```python
class ValidParser(NamedTuple):
    name: str
```

```python
class BareBonesRoute(NamedTuple):
    name: str
    handler: object
    content_type: ValidParser
```
- Easier and more developer friendly test cases using `pytest`
- Using constants wherever required like for storing the HTTP status codes (similar to Django REST Framework)
- Easier route and controller integration using something like the Flask `app` decorator 
- Registering custom middlewares before parsing the request or rendering the response, eg. CSRF, Auth, Logging etc.
- Registering 500s and raising using tool like Sentry/Airbrake
- Adding a logging framework for storing required debug and error logs
- Rate limit/API throttling based on IP address to prevent abuse of the API
- Attaching a database and validating the trees entered across the ones in the system to flag erroneous inputs eg. "Salad" or "Steam"