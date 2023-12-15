
from aocd import get_data
from decouple import config 
def transform(data,prevSum):
    asci=int(ord(data))
    # print(asci,data,asci+prevSum)
    asci+=prevSum
    asci=asci*17
    asci=asci%256
    
    return asci
# print(transform("H"))
def strTohop(data):
    sum=0
    for d in data:
        sum=transform(d,sum)
        
        # sum+=res
        # print(sum)
    return sum
# print(strTohop("HASH"))
data = get_data(session=config('SESSION'),year=2023, day=15)#open("input.txt").read()

sumRes=0
cmds= data.split(",")
for d in cmds:
    res=strTohop(d)
    sumRes+=res
print(sumRes)


BOX = [[] for _ in range(256)]
for cmd in cmds:
  if cmd[-1]=='-':
    name = cmd[:-1]
    h = strTohop(name)
    BOX[h] = [(n,v) for (n,v) in BOX[h] if n!=name]
  elif cmd[-2]=='=':
    name = cmd[:-2]
    h = strTohop(name)
    len_ = int(cmd[-1])
    if name in [n for (n,v) in BOX[h]]:
      BOX[h] = [(n, len_ if name==n else v) for (n,v) in BOX[h]]
    else:
      BOX[h].append((name, len_))

p2 = 0
for i,box in enumerate(BOX):
  for j,(n,v) in enumerate(box):
    p2 += (i+1)*(j+1)*v
print(p2)