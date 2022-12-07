# read lines and sum until empty line arive store sume in list
res=[]
maxSum=-1
sum=0
with open("input2.txt",encoding='utf-8') as f:
    data = [line.strip() for line in f.readlines()]
for line in data:
    
    # for i, line in enumerate(f):
    #     line = line.replace("\n", "")#18814\n
    if str(line) != "":
        sum+=int(line)
    else:
        res.append(sum)
        if(sum>maxSum):
            maxSum=sum
        sum=0
print("max sum is: ",maxSum)
#PArt 2 
res.sort()

print("sorted list is: ", res)
n=3
highsum=0
for i in range(n):
    highsum+=res[len(res)-1-i]
print("high sum is: ",highsum)
# fun = lambda x: sum(map(int, x.split()))