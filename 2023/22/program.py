

import numpy as np
D = open("input.txt").read().strip()
L = D.split('\n')

dat = []
# fig = plt.figure()
# ax = plt.axes(projection='3d')

for row in L:
    c1,c2=row.split("~")
    x, y, z=c1.split(",")    
    x1, y1, z1=c2.split(",")
    dat.append(((int(x),int(y), int(z)),(int(x1),int(y1), int(z1))))
    # dic[ch]=[[x, y, z],[x1, y1, z1]]

print(len(dat)) #to verify input readed correctly or not




bricks = list(dat)
bricks.sort(key=lambda x:min(x[0][2], x[1][2]))
offsets = [None] * len(dat)
supported = [None] * len(dat)
covered = {}
for i, ((x1,y1,z1),(x2,y2,z2)) in enumerate(bricks):
	def isok(zofs):
		touching = set()
		if z1 - zofs <= 0 or z2 - zofs <= 0:
			touching.add(-1)
		for x in range(x1,x2+1):
			for y in range(y1,y2+1):
				for z in range(z1-zofs,z2-zofs+1):
					if (x,y,z) in covered:
						touching.add(covered[x,y,z])
		return touching
	zofs = 0
	while True:
		touch = isok(zofs + 1)
		if touch:
			break
		zofs = zofs + 1
	offsets[i] = zofs
	supported[i] = touch
	for x in range(x1,x2+1):
		for y in range(y1,y2+1):
			for z in range(z1-zofs,z2-zofs+1):
				covered[x,y,z] = i

#print(supported)
unremovable = set.union(*(i for i in supported if len(i) == 1))
unremovable.remove(-1)
print(len(bricks) - len(unremovable))

cascade = [None] * len(dat)
for i in range(len(dat)):
	fallen = {i}
	for j in range(i+1, len(dat)):
		if not supported[j] - fallen:
			fallen.add(j)
	cascade[i] = len(fallen) - 1
print(sum(cascade))