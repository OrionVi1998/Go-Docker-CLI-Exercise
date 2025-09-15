import random


class StubApi:
    def __init__(self):
        num_pages = random.randint(0, 1000)
        pages = [list(range(10)) for _ in range(num_pages)]
        last_page = list(range(random.randint(1, 9)))
        result = num_pages * 10

        if random.choice([False, True]):
            pages.append(last_page)
            result += len(last_page)

        self.year: list[list[int]] = pages
        self.result = result

    def get_movie(self, year: int, page) -> dict | list[int]:
        try:
            return self.year[page - 1]
        except IndexError:
            return {"error": ""}

    def get_answer(self):
        total = len(self.year)
        if self.result <= 30:
            print(self.year)
        else:
            print(self.year[-1])
        print(f"Correct: {self.result}, NPages={total}")
        return self.result
