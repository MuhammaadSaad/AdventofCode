
from aocd import get_data
from decouple import config 

data = get_data(session=config('SESSION'),year=2023, day=19)
print(data[:2])
#open("input.txt").read()