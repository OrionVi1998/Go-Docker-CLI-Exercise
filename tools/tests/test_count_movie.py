import pytest
from cli.commands.count_movie_years import count_movies
from .utils import StubApi


@pytest.mark.repeat(1000)
def test_count_movies():
    api = StubApi()
    test = count_movies(api, 0)
    print(f"Test Result: {test}", end="\t-\t")
    answer = api.get_answer()
    assert test == answer, f"!="
