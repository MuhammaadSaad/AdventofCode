filename="intput.txt"
# import Polygon
# input=open("intput.txt").read()
# lines = input.strip().split('\n')
ll = [x for x in open(filename).read().strip().split('\n')]
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
DNS = ['R', 'D', 'L', 'U']
def run(part2):
	boundary = set()
	pos = (0, 0)
	points = [pos]
	perimeter = 0
	for l in ll:
		if part2:
			l = l.split("#")[1].split(")")[0]
			d = DIRS[int(l[-1])]
			dist = int(l[:-1], 16)
		else:
			d = DIRS[DNS.index(l.split(" ")[0])]
			dist = int(l.split(" ")[1])
		pos = (pos[0] + d[0] * dist, pos[1] + d[1] * dist)
		perimeter += dist
		points.append(pos)

	points = points[::-1]
	a = 0
	for i in range(len(points) - 1):
		a += (points[i][1] + points[i + 1][1]) * (points[i][0] - points[i + 1][0])
	print(perimeter // 2 + a // 2 + 1)

run(False)
run(True)
# for line in lines:
#     line = line.strip()
#     if line == "": continue
#     a, b, c = line.split()
#     cur_dir = dir_map[a]
#     cur_len = int(b)
#     for i in range(cur_len+1):
#         pts.add((loc[0]+i*cur_dir[0], loc[1]+i*cur_dir[1]))
#     loc = (loc[0]+cur_len*cur_dir[0], loc[1]+cur_len*cur_dir[1])
#     xs.append(loc[0])
#     ys.append(loc[1])
#     print(loc)

# A = PolyArea(xs, ys)
# b = len(pts)
# # A = i + b/2 - 1 -> i = A + 1 - b/2
# assert(b % 2 == 0)
# I = A + 1 - b // 2
# print(I+b)