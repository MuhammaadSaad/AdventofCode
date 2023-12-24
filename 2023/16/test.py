DAY_NUM = 16
DAY_DESC = 'Day 16: The Floor Will Be Lava'
from grid import Grid, Point
from collections import deque
def calc(log, values, mode):
    
    grid = Grid.from_text(values)

    def get_starts():
        for y in grid.y_range():
            yield deque([(0, y, 1, 0)])
            if mode == 1:
                break
            yield deque([(grid.axis_max(0), y, -1, 0)])
        if mode == 2:
            for x in grid.x_range():
                yield deque([(x, 0, 0, 1)])
                yield deque([(x, grid.axis_max(1), 0, -1)])

    best = 0
    for todo in get_starts():
        seen = set()
        energy = set()
        energy.add((todo[0][0], todo[0][1]))
        while len(todo) > 0:
            x, y, ox, oy = todo.pop()
            if (x, y, ox, oy) not in seen:
                seen.add((x, y, ox, oy))
                x += ox
                y += oy
                if 0 <= x <= grid.axis_max(0) and 0 <= y <= grid.axis_max(1):
                    energy.add((x, y))
                    if grid[x, y] == "|" and oy == 0:
                        todo.append((x, y, 0, 1))
                        todo.append((x, y, 0, -1))
                    elif grid[x, y] == "-" and ox == 0:
                        todo.append((x, y, 1, 0))
                        todo.append((x, y, -1, 0))
                    else:
                        if grid[x, y] == "/":
                            if (ox, oy) == (1, 0): ox, oy = 0, -1
                            elif (ox, oy) == (-1, 0): ox, oy = 0, 1
                            elif (ox, oy) == (0, -1): ox, oy = 1, 0
                            elif (ox, oy) == (0, 1): ox, oy = -1, 0
                        elif grid[x, y] == "\\":
                            if (ox, oy) == (1, 0): ox, oy = 0, 1
                            elif (ox, oy) == (-1, 0): ox, oy = 0, -1
                            elif (ox, oy) == (0, -1): ox, oy = -1, 0
                            elif (ox, oy) == (0, 1): ox, oy = 1, 0
                        todo.append((x, y, ox, oy))
    
        best = max(best, len(energy))

    return best

def test(log):
    values = log.decode_values(r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
    """)

    log.test(calc(log, values, 1), '46')
    log.test(calc(log, values, 2), '51')

def run(log, values):
    log(calc(log, values, 1))
    log(calc(log, values, 2))

if __name__ == "__main__":
    import sys, os
    
    with open("input.txt") as f: values = [x.strip("\r\n") for x in f.readlines()]
    print(f"Running day {DAY_DESC}:")
    run(print, values)