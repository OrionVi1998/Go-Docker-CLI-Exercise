import requests
from datetime import *


class ApiGateway:
    """
    Handles the connection to the backend server
    """

    def __init__(self, user: str, password: str, api_url: str, grace_period: int):
        self.token: str | None = None
        self.timeout: datetime | None = None
        self.api_url = api_url
        self.grace_period = grace_period
        self.user = user
        self.password = password

    def refresh_token(self) -> None:
        if self.timeout is None or self.timeout < datetime.now():
            response: requests.Response = requests.post(
                self.api_url + "/auth",
                json={"username": self.user, "password": self.password},
                headers={"Content-Type": "application/json"},
            )
            if response.status_code == 200:
                r = response.json()
                self.timeout = (
                    datetime.now()
                    + timedelta(seconds=r["timeout"])
                    - timedelta(seconds=self.grace_period)
                )
                self.token = r["bearer"]

            else:
                raise Exception("Authentication Error")

    def get_movie(self, year: int, page: int) -> dict[str, str] | list[str]:
        self.refresh_token()
        response: requests.Response = requests.get(
            self.api_url + f"/movies/{year}/{page}",
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            },
        )

        if isinstance(response, dict):
            raise Exception("No page found")

        return response.json()
