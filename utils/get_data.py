
from aocd import get_data
from pathlib import Path
from aocd import submit

AOC_SESSION="53616c7465645f5f355c90aa89fae92f79588f6bc7b9ee4b79aa3d9d27dfcc3ba12e1ae2f2ea947421d5fc8c85ef91e404fae5c5296c2b9bbc11af57f9fe10af"

def get_data_to_file(year: int, day: int):
    data = get_data(session=AOC_SESSION, year=year, day=day).splitlines()
    with open(Path() / str(year) / f"day{day}" / "input.txt", "w") as f:
        f.write("\n".join(data))
