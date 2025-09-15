Movie Server
============

This server serves movie lists via a REST API.

Endpoints
=========

```
The following endpoints are available:

POST /api/auth
	This endpoint allows users to authenticate themselves with the server. Accepts a JSON body with the following format:
		{"username": "USERNAME", "password": "PASSWORD"}

	On a success, the endpoint will return a JSON packet with the following format:
		{"bearer": "TOKEN", "timeout": TOKEN_LIFETIME}

GET /api/movies/$YEAR/$PAGE	
	This endpoint requires the bearer token passed in the Authorization header. Will return a JSON list of upto 10 movies.
```

Usage
=====

```
  -port uint
    	port to listen on (default 8080)
```

CLI
============

Testing the CLI tool
=====
To test, first install the optional dependencies found in `./tools/pyproject.toml`
```bash
pip install -e ./tools[test]
```
Then the following command will run the tests 
```bash
mypy ./tools/src && black --check ./tools && pytest ./tools/tests/test_count_movie.py
```


Running the container and CLI tool
=====
To run the container and access it's shell you can run the following command:
```bash
  docker-compose up -d && docker exec -it movies bash
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