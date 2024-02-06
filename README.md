# testday-repo
Testing Task for a Python Expert Test Day

# Requirements
This project uses the django rest framework for api endpoints.



# Manual setup
setup virtual env
```bash
python3 -m venv .venv
```

activate virtual env
```bash
source .venv/bin/activate
```

install requirements
```bash
python3 -m pip install -r requirements.txt
``` 

run migrations
```bash
python3 src/manage.py migrate
``` 

load superuser fixture
```bash
python3 src/manage.py loaddata src/fixtures/users.json 
```

start the application
```bash
python3 src/manage.py runserver
```

run tests
```bash
cd src/
python3 manage.py test apps/
```


# API Endpoints
1. Get Token:
- Endpoint: '/token/'
- Method: POST
- Request Format: JSON
- Parameters:
    - 'email' : unique email used as username
    - 'password' : users password
- Response:
    - Status Code: 200 OK
    - Body: {"token": "<VALID_TOKEN>"}

2. Protected
- Endpoint: '/protected/'
- Method: GET
- Request Format: None (Token should be include in Authentication headers)
- Response:
    - Status Code: 200 OK
    - Body: {"email" : "<USER_EMAIL>"}
    - Status Code: 401 Unauthorized (If no valid token is provided)


# finished tasks commits:
[Task 1](https://github.com/CCiwy/testday-repo/commit/a8948ecaca5f0116943edadbed0c2df8c27a055c)
[Task 2](https://github.com/CCiwy/testday-repo/commit/1a854d00f347db186ed0ec24cbf5a8afb2dcd519)
[Task 3](https://github.com/CCiwy/testday-repo/commit/f5df4a2e952fc4ca11869811052b683453791d5f)


# Formatting
Formatting was done using [https://github.com/astral-sh/ruff](ruff)
