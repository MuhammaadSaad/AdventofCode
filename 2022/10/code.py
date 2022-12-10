
ll = [x for x in open("input.txt").read().strip().split('\n')]

x = 1
cnt = 0
sm = 0
crt = [[" " for x in range(40)] for y in range(6)]


def cycle():
	global cnt, sm, x
	cnt += 1
	if cnt == 20 or cnt == 60 or cnt == 100 or cnt == 140 or cnt == 180 or cnt == 220:
		sm += cnt * x
	if abs((cnt-1) % 40-x) < 2:
		crt[(cnt-1)//40][(cnt-1) % 40] = "#"


for line in ll:
	if line == "noop":
		cycle()
	else:
		add = int(line[5:])
		cycle()
		cycle()
		x += add
print(sm)
for line in crt:
	print("".join(line))
        
       
        
     