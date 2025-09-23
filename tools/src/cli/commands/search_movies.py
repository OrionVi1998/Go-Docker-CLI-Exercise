from datetime import datetime
from ..gateway import ApiGateway


def search_movie(api: ApiGateway, year: int, search: str) -> list[str]:
    page_num = 1
    found_movies = []
    search = search.lower()

    while True:
        try:
            curr_page = api.get_movie(year, page_num)
        except Exception:
            return found_movies

        for movie_title in curr_page:
            if search in movie_title.lower():
                found_movies.append(movie_title)

        page_num+=1




def search_movies(api: ApiGateway, years: list[int], count_only: bool, search: str) -> dict[int, list[str]] | dict[int, int]:
    """
    Counts the movies in each year and returns a dictionary with year, count key value pairs
    :param api:
    :param years:
    :return:
    """
    assert all(
        1800 <= n <= datetime.now().year for n in years
    ), "Years must be between 1800 and the current year"
    if count_only:
        return {y: len(search_movie(api, y, search)) for y in set(years)}

    return {y: search_movie(api, y, search) for y in set(years)}