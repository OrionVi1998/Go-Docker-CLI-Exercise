CLI
============

Testing the CLI tool
=====
To test, first install the optional dependencies found in `./tools/pyproject.toml`

```bash
pip install -e ./tools[test]
```

Then the following command will run the included tests

```bash
mypy ./tools/src && black --check ./tools && pytest ./tools/tests/test_count_movie.py
```

Requirements
=====
To build and run the container through docker compose version 28.4.0 or newer of docker is needed.

Running the container and CLI tool
=====
The CLI is installed within the container. To run the container and access its shell you can run the following command
in a bash terminal:

```bash
  docker compose up -d && docker exec -it movies bash
```

From there the cli tool is accessible through `movies-cli`

```
usage: movies-cli [-h] [-y YEARS [YEARS ...]] [-u USER] [-p PASSWORD] [-a API_URL] [-g GRACE_PERIOD]

options:
  -h, --help            show this help message and exit
  -y, --years YEARS [YEARS ...]
                        Count the number of movies per year. Accepts values between 1800 to current year
  -u, --user USER       The user to be used for authentification. Defaults to 'username'
  -p, --password PASSWORD
                        The password to be used for authentification. Defaults to 'password'
  -a, --api_url API_URL
                        The address of the server to connect to. Defaults to 'http://localhost:8080/api'
  -g, --grace_period GRACE_PERIOD
                        The time in seconds before the received token timeout when the token should be refreshed. Defaults to '3'
```

### Examples

```
movies-cli -y 2000
```


```
movies-cli -y 2000 1999 2005
```
