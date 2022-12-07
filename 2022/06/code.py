def code(data, chucksize):
    i=0
    for s in range(2, len(data)):
        # check repeated char in chunk of 4
        
        # 
        
        ch = set(data[i:s])
        # print(i,s, data[i:s],ch)
        i += 1
        
        # 
        # 
        if len(ch) == chucksize: #3==4
            return data[i:s], s
    return -1
def sum(a,b):
    print("sum")
    print(a+b)

#  print(i) in range(0,10))
with open("input.txt") as file:
    data=file.read()
# data = "tnmmpfmfzmmnsmsjm"
st,index= code(data,4)
print(index)
stP2,indexP2=code(data,14)
print(stP2,indexP2)


