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



# fnished tasks commits:
[Task 1](https://github.com/CCiwy/testday-repo/commit/a8948ecaca5f0116943edadbed0c2df8c27a055c)
[Task 2](https://github.com/CCiwy/testday-repo/commit/1a854d00f347db186ed0ec24cbf5a8afb2dcd519)
