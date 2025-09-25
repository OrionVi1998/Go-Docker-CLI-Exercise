import argparse


def get_parser() -> argparse.ArgumentParser:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="CLI Tool to connect to the movies server"
    )
    parser.add_argument(
        "-y",
        "--years",
        nargs="+",
        type=int,
        help="Count the number of movies per year. Accepts values from 1800 to current year",
        required=False,
    )

    parser.add_argument("--search", type=str, help="Optional search pattern")

    parser.add_argument(
        "--count-only", type=bool, help="Return the count of movies found"
    )

    parser.add_argument(
        "-u",
        "--user",
        type=str,
        help="The user to be used for authentification. Defaults to 'username'",
        required=False,
        default="username",
    )
    parser.add_argument(
        "-p",
        "--password",
        type=str,
        help="The password to be used for authentification. Defaults to 'password'",
        required=False,
        default="password",
    )
    parser.add_argument(
        "-a",
        "--api_url",
        type=str,
        help="The address of the server to connect to. Defaults to 'http://localhost:8080/api'",
        required=False,
        default="http://localhost:8080/api",
    )
    parser.add_argument(
        "-g",
        "--grace_period",
        type=int,
        help="The time in seconds before the received token timeout when the token should be refreshed. Defaults to '3'",
        required=False,
        default=3,
    )
    return parser
