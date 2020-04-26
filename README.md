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
- [x] Simple HTTP server with whitelisted HTTP methods
- [x] Index Controller for knowing the Favorite Tree
- [x] Multithreaded Server
- [x] Test Cases
- [x] Returns JSON response with status code `404` if the route is not defined/supported
- [x] Index Controller logic refactor
- [x] Simple Docker container
    


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