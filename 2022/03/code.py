res=[]
sum=0
AlphabatasDic={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,
               'A':27,'B':28,'C':29,'D':30,'E':31,'F':32,'G':33,'H':34,'I':35,'J':36,'K':37,'L':38,'M':39,'N':40,'O':41,'P':42,'Q':43,'R':44,'S':45,'T':46,'U':47,'V':48,'W':49,'X':50,'Y':51,'Z':52}
def p1():
    res = []


    sum = 0
    with open("input.txt", encoding='utf-8') as f:

        for i, line in enumerate(f):
            line = line.replace("\n", "")
            s=len(line)
            f,s=line[:s//2],line[s//2:]
            #find same element in both list
            for i in range(len(f)):
                if f[i] in s:
                    res.append(f[i])
                    sum += AlphabatasDic[f[i]]
                    break
    print(res)

    print(sum)
def p2():
    res=[]
    sum=0
    gp=[]
    resgp=[]
    j=1
    with open("input.txt", encoding='utf-8') as f:
        
        for i, line in enumerate(f):
            line = line.replace("\n", "")
            gp.append(line)
            
            if len(gp)==3:
                
                
                for c in gp[0]:
                    if c in gp[1] and c in gp[2]:
                        res.append(c)
                        sum+=AlphabatasDic[c]
                        break
                
                resgp.append(gp)
                gp=[]
                # j=0
            # print("gp is: ", gp)
    # if len(gp)==3:
    #     for c in gp[0]:
    #         if c in gp[1] and c in gp[2]:
    #             res.append(c)
    #             sum += AlphabatasDic[c]

    #     resgp.append(gp)
    print(res)        
    print(sum)
p2()