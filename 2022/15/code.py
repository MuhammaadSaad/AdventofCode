box = {}
ranges = list()
data = list()
target_row = 200000
with open("input.txt") as f:
    for line in f.readlines():
        # Do something with the line
        # l=line.split(":")
        l = line.replace("\n", "")
        # Sensor at x=2885528, y=2847539: closest beacon is at x=2966570, y=2470834
        S,B=l.split(":")
        li=S.split(",")
        yS=li[-1]
        xS=li[-2]
        sy=int(yS.split("=")[1])
        sx = int(xS.split("=")[1])

        
        box[sx,sy]="S"
        li = B.split(",")
        yB = li[-1]
        xB = li[-2]
        by = int(yB.split("=")[1])
        bx = int(xB.split("=")[1])
        
        box[bx,by] = "B"
        data.append((sx, sy, bx, by, ))
        L1 = abs(sx - bx) + abs(sy - by)

        if (sy - L1) <= target_row <= (sy + L1):
            width = L1 - abs(sy - target_row)
            ranges.append((sx - width, sx + width, ))

ranges.sort()

count = 0
print(ranges)
head = ranges[0][0]
for x, y in ranges:
    if head < x:
        count += y - x + 1
        head = y
    else:
        if head < y:
            count += y - head
            head = y
    
print(count)

# if y ="2000000":
#     print(l[0])
#     break