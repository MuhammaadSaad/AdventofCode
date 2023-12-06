time=[52,94,75,94]
Distance=  [ 426,1374,1279,1216]
milisec=0
sum=0
# 11,41 =31
# 19,75=57
# 27,48=22
# 16,78=63
# from functools import reduce
timr=52947594
dist= 426137412791216
from functools import reduce
import sys
from typing import List, Tuple

def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            lines.append(line)

    return lines


def calculate_distance(held, remaining):
    return remaining * held

def part_one():
    lines = read_lines_to_list()
    times = [int(val) for val in lines[0].split(":")[1].strip().split()]
    records = [int(val) for val in lines[1].split(":")[1].strip().split()]

    races = [(time, distance) for (time, distance) in zip(times, records)]

    num_ways = []

    for time, record in races:
        wins = 0
        for i in range(time + 1):
            if calculate_distance(i, time - i) > record:
                wins += 1

        num_ways.append(wins)

    result = reduce((lambda x, y: x * y), num_ways)
    print(f"Part 1: {result}")

def part_two():
    lines = read_lines_to_list()
    time = int("".join(lines[0].split(":")[1].strip().split()))
    record = int("".join(lines[1].split(":")[1].strip().split()))

    wins = 0
    for i in range(150,time + 1):
        if calculate_distance(i, time - i) > record:
            wins += 1

    print(f"Part 2: {wins}")
part_one()
part_two()