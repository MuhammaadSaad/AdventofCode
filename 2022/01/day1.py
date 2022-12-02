# read lines and sum until empty line arive store sume in list
res=[]
maxSum=-1
sum=0
with open("input1.txt",encoding='utf-8') as f:
    
    for i, line in enumerate(f):
        line = line.replace("\n", "")
        if str(line) != "":
            sum+=int(line)
        else:
            res.append(sum)
            if(sum>maxSum):
                maxSum=sum
            sum=0
print("max sum is: ",maxSum)
# res.sort()
print("sorted list is: ",res)
# fun = lambda x: sum(map(int, x.split()))