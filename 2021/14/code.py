import collections
def process(parts):
    grid = []
    for line in parts[0].split('\n'):
        for n in line.strip():
            
            grid.append(n) 
       
    folds = []
    for line in parts[1].strip().split('\n'):
        xy, n = line.strip().split(' -> ')
        
        folds.append((xy, n))
    return grid, folds
with open('input') as f:
    grid, folds = process(f.read().split('\n\n'))
def fold(grid,folds):
    
    re=[]
    for x in grid:
        for xy, n in folds:
        
            if xy ==x:
                s,e=xy.strip()
                x=s+n+e
                re.append(x)
    return re
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    l=""
    for ele in s:
        sf,sm,sl=ele.strip()
        if l==sf:
            l=sl
            str1 += sm+sl
        else:
            l=sl
            str1 += ele


    # return string  
    return str1 
def part_one():
    print("Part 1:")
    for i in range(10):
        re= []
        for x in range(len(grid)-1):
            re.append(grid[x]+grid[x+1])
        #print(re)
        res=fold(re, folds)
        
        grid=listToString(res)
        print("step "+str(i),len(grid))
    result(grid)

def result(grid):
    frequencies = collections.Counter(grid)
    repeated = {}

    for key, value in frequencies.items():

        if value > 1:
            repeated[key] = value

    print(repeated)
    max=0
    min=len(grid)
    for key,val in repeated.items():
        if int(val)<min:
            min=int(val)
        if int(val)>max:
            max=int(val)
    print(max,min,max-min)
print("Part 2:")
for i in range(40):
    re= []
    for x in range(len(grid)-1):
        re.append(grid[x]+grid[x+1])
    #print(re)
    res=fold(re, folds)
    
    grid=listToString(res)
    print("step "+str(i),len(grid))
result(grid)