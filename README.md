# testday-repo
Testing Task for a Python Expert Test Day


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

```bash
python3 src/manage.py runserver
```
