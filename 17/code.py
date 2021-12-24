with open('input') as f:
    data = f.read().split('\n')

inp = data[0].split('=')
x1 = int(inp[1][:inp[1].index('.')])
x2 = int(inp[1][inp[1].index('.') + 2: inp[1].index(',')])
y1 = int(inp[2][:inp[2].index('.')])
y2 = int(inp[2][inp[2].index('.') + 2:])

def check(xVel, yVel):
	x = 0
	y = 0
	maxY = 0

	for _ in range(1000):
		x += xVel
		y += yVel
		maxY = max(maxY, y)

		if xVel < 0:
			xVel += 1
		elif xVel > 0:
			xVel -= 1
		
		yVel -= 1

		if (
			(x < x1 and xVel <= 0) or 
			(x > x2 and xVel >= 0) or 
			(y < y1 and yVel <= 0)
		):
			return -int(1e9)

		if x1 <= x <= x2 and y1 <= y <= y2:
			return maxY
	
	return -int(1e9)

res = 0
for yVel in range(-1000, 1000):
	for xVel in range(1000):
		i = check(xVel, yVel)
		if i != -int(1e9):
			res += 1

print(res)