from datetime import datetime
from ..gateway import ApiGateway


def count_movies(api: ApiGateway, year: int) -> int:
    """
    Counts the movies in a single year
    :param api:
    :param year:
    :return:
    """
    # Given that a page can only hold up to 10 movies
    # by finding the last page we can calculate the number of movies
    # Captures the last page between two bounds and then reduces the size of the bound as it performs binary search to find the last page

    current_page = 500
    # Range where the last page is
    lower_bound: int = 0
    upper_bound: int | None = None

    while True:
        r = api.get_movie(year, current_page)

        if type(r) == dict:  # If page does not exist
            if current_page == 1:
                return 0  # No movies in year

            if upper_bound is None:  # Adjust upper bound
                upper_bound = current_page
            upper_bound = min([upper_bound, current_page])

            # Update current page value
            current_page -= (upper_bound - lower_bound) // 2

            if upper_bound is not None and (upper_bound - lower_bound) <= 1:
                # If the page was found but the current page is not existing
                return lower_bound * 10

        else:  # If page found
            # Adjust the lower bound
            lower_bound = max([current_page, lower_bound])

            if len(r) == 10:
                # Update current page value if last page not found
                if upper_bound is None:
                    current_page += current_page
                else:
                    current_page += (upper_bound - lower_bound) * 2

            if len(r) != 10:
                # If the page isn't full we know it's the last one
                # If the delta between lower bound and upper bound is 1 we found the last page
                return (current_page - 1) * 10 + len(r)


def count_movies_years(api: ApiGateway, years: list[int]) -> dict[int, int]:
    """
    Counts the movies in each year and returns a dictionary with year, count key value pairs
    :param api:
    :param years:
    :return:
    """
    assert all(
        1800 <= n <= datetime.now().year for n in years
    ), "Years must be between 1800 and the current year"
    return {y: count_movies(api, y) for y in set(years)}
