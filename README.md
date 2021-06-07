# Basic AUTH and CRUD FastAPI App
  This application perform basic auth authentication using FastAPI Auth and some crud opertaion using sqlalchamy ORM. Create test cases using pytest and used SQLite as a database. 


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)


## Features

- A user can registration and login using email and password
- A user can create country with states and address
- A user can read countries , states and addresses


## Installation

FastAPI Demo requires [Python](https://python.org/) v3+ to run.

pull code repo:
```sh
# clone this app using http
$ git clone https://github.com/sirayhancse/FastAPI-Demo.git
# go to project directory folder
$ cd FastAPI-Demo
```
Create a virtual environment and install the dependencies and devDependencies to start the server.

```sh
# install virtual enviornment 
$ pip install virtualenv
# create virtual envrionment
$ virtualenv venv
# active virtual environment
$ source venv/bin/active
# install dependencies from requiremtns.txt
$ pip3 install -r requirements.txt
# copy dev.env as .env
$ cp dev.env .env
```

Run the development environment server...

```sh
# Run uvicorn server
$ uvicorn app.main:app --reload
```
Verify the deployment by navigating to your server address in
your preferred browser.

```sh
http://127.0.0.1:8000/docs
```
If everthing is okay , you can see the project swagger page.

## Testing

Want to Test app API's?

FastAPI Demo use pytest for fast testing.

Follow this steps and run command on your terminal:


```sh
# run pytest suit
$ pytest
```
If you want to change dummy users or country data , you need to chane respective response data also.
## License

MIT

