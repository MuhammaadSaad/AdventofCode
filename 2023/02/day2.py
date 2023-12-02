from collections import defaultdict
ll = [x for x in open('input.txt').read().strip().split('\n')]

p1 = 0
p2 = 0
for l in ll:
	gameid = int(l.split(":")[0].split(" ")[1]) # get game no from "Game 1:" 
	l = l.split(":")[1]
	possible = True
	mincounts = defaultdict(int)
	for s in l.split(";"):
		counts = defaultdict(int)
		for colors in s.split(", "):
			colors = colors.strip()
			counts[colors.split(" ")[1]]+=int(colors.split(" ")[0])
		for k,v in counts.items():
			mincounts[k] = max(mincounts[k], v)
		if not (counts["red"] <= 12 and counts["green"] <= 13 and counts["blue"] <= 14):
			possible=False
	if possible:
		p1 += gameid
	p2 += mincounts["red"]*mincounts["green"]*mincounts["blue"]
print(p1)
print(p2)