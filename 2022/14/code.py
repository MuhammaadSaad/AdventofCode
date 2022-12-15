"""# Open the input file
with open('input.txt') as input_file:
    # Read the file line by line
    lines = input_file.readlines()
grid= []
for i in range(160):
    grid.append([])
    for j in range(90):
        grid[i].append(".")
print(len(grid), len(grid[0]))
for line in lines:
    
    line =line.replace('\n',"")
    ln=line.split(" -> ")
    for  l in ln:
        a, b = map(int, l.split(","))
        print(a-480,b-13)
        if a== 500:
            grid[b-13][a-480] = "+"
        else:
            grid[b-13][a-480] = "#"
            # grid.append("#") # for air

# count how many sand point needed to be filled
c=0
print(grid)

"""

def parse_cave(s):
    cave = {}

    for line in s.splitlines():
        parts = line.split(' -> ')
        parts = [tuple(map(int, p.split(',')))
                 for p in parts]
        x, y = parts.pop(0)
        cave[x,y] = '#'
        for x2, y2 in parts:
            dx, dy = x2-x, y2-y
            if dx != 0:
                dx = dx // abs(dx)
            if dy != 0:
                dy = dy // abs(dy)

            while x != x2 or y != y2:
                x += dx
                y += dy
                cave[x,y] = '#'

    return cave

def generate_sand(cave, in_x, in_y, max_y):
    x = in_x
    y = in_y
    while (x,y) not in cave:
        if y > max_y:
            return False
        if (x,y+1) not in cave:
            y += 1
            continue
        if (x-1,y+1) not in cave:
            x -= 1
            y += 1
            continue
        if (x+1,y+1) not in cave:
            x += 1
            y += 1
            continue
        # This must have settled
        cave[x,y] = 'o'
        return True

def part1(s):
    cave = parse_cave(s)
    
    max_y = max(y for x,y in cave.keys())
    # print(max_y)
    answer = 0

    while generate_sand(cave, 500, 0, max_y):
        answer += 1
    print(answer)
    # lib.aoc.give_answer(2022, 14, 1, answer)

def part2(s):
    cave = parse_cave(s)

    max_y = max(y for x,y in cave.keys())


    # print(max_y)
    floor = max_y + 2

    for x in range(500-floor-2, 500+floor+3):
        cave[x,floor] = '#'

    answer = 0

    while cave.get((500,0)) is None:
        assert(generate_sand(cave, 500, 0, floor))
        answer += 1
    print(answer)
    # lib.aoc.give_answer(2022, 14, 2, answer)


# with open('input.txt') as input_file:
#     # Read the file line by line
#     INPUT = input_file.readlines()
    
INPUT = open('input.txt').read().strip()
# INPUT = lib.aoc.get_input(2022, 14)
part1(INPUT)
part2(INPUT)