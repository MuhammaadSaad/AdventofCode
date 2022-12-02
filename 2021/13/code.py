def process(parts):
    grid = set()
    for line in parts[0].split('\n'):
        a, b = [int(n) for n in line.strip().split(',')]
        grid.add((a, b))
    folds = []
    for line in parts[1].strip().split('\n'):
        xy, n = line.strip().split(' ')[2].split('=')
        n = int(n)
        folds.append((xy, n))
    return grid, folds
with open('input.txt') as f:
    grid, folds = process(f.read().split('\n\n'))
def fold(grid, xy, n):
    if xy == 'x':
        return {(x, y) for x, y in grid if x < n} | {(n - (x - n), y) for x, y in grid if x > n}
    else:
        return {(x, y) for x, y in grid if y < n} | {(x, n - (y - n)) for x, y in grid if y > n}
xy, n = folds[0]
print("Part 1:")
print(len(fold(grid, xy, n)))

def display_grid():
    max_x = max([pos[0] for pos in grid])
    max_y = max([pos[1] for pos in grid])
    
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) in grid:
                print('█', end='')
            else:
                print(' ', end='')
        print()
for xy, n in folds:
    grid = fold(grid, xy, n)
print("Part 2:")
display_grid()