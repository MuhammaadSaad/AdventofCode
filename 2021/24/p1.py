with open('input.txt') as f:
    lines = [  line.strip() for line in f]
#print(lines)
w=0
x=0 
y=0 
z=0 
a=0 
b=0
i=0
l=[5,1,1,3,1,6,1,6,1,1,2,7,8,1]
[9,2,7,9,3,9,4,9,4,8,9,9,9,5]
# [1,1,5,7,1,1,9,9,1,9,9,1,9,1]
def inp():
    global i
    if(i<len(l)): 
        temp=l[i] 
        i+=1
        return temp 
def updvar(vr,val):
    print(vr,val)
    if (vr=="a"):
        global a
        a=val
    if (vr=="x"):
        global x
        x=val
    if (vr=="y"):
        global y
        y=val
    if (vr=="z"):
        global z
        z=val
    if (vr=="w"):
        global w
        w=val
    if (vr=="b"):
        global b
        b=val
        
def chkvar(vr):
    if (vr=="a"):
        global a
        return a
        
    elif (vr=="x"):
        global x
        print(x)
        return x
    elif (vr=="y"):
        global y
        return y
    elif (vr=="z"):
        global z
        return z
    elif (vr=="w"):
        global w
        return w
    elif (vr=="b"):
        global b
        return b
    else:
        return int(vr)
def p1():
    for line in lines:
        s=line.split(" ")
        print(line)
        if(s[0]=="add"):
            pa=chkvar(s[1])
            pb=chkvar(s[2])
            if (pa!=None and pb!=None):
                
                updvar(s[1],pa+pb)
            
        if(s[0]=="mul"):
            pa=chkvar(s[1])
            pb=chkvar(s[2])
            if(pa!=None and pb!=None):
                updvar(s[1],pa*pb)
        if(s[0]=="div"):
            pa=chkvar(s[1])
            pb=chkvar(s[2])
            if(pa!=None and pb!=None):
                updvar(s[1],int(pa/pb))
        if(s[0]=="mod"):
            pa=chkvar(s[1])
            pb=chkvar(s[2])
            if(pa!=None and pb!=None):
                updvar(s[1],pa%pb)
        if(s[0]=="eql"):
            pa=chkvar(s[1])
            pb=chkvar(s[2])
            if(pa!=None and pb!=None):
                if pa==pb:
                    updvar(s[1],1)
                else:
                    updvar(s[1],0)

        if(s[0]=="inp"):
            updvar( s[1],inp())
p1() 

print(a,b,w,x,y,z)

