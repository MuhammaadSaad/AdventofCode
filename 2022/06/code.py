def code(data, chucksize):
    i=0
    for s in range(chucksize, len(data)):
        # check repeated char in chunk of 4
        ch=  set(data[i:s])
        i+=1
        if len(ch) == chucksize:
            return data[i:s], s
    return -1

with open("input.txt") as file:
    data=file.read()     
st,index= code(data,4)
print(st,index)
stP2,indexP2=code(data,14)
print(stP2,indexP2)

