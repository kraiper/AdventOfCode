
from aocd import get_data
from pathlib import Path
from aocd import submit

AOC_SESSION="53616c7465645f5f9f002854e18c7386a6990da3be440f7343bf01cef7e0e77bc91d72a688165c724157654f07dfecb169e3a3c998e31040a6fca90f9b1ec1c4"

def get_data_to_file(year: int, day: int):
    data = get_data(session=AOC_SESSION, year=year, day=day).splitlines()
    with open(Path() / str(year) / f"day{day}" / "input.txt", "w") as f:
        f.write("\n".join(data))
