

f = open("input.txt").read().strip().split("\n")

for i in range(len(f)):
    s1 = f[i]
    m = re.findall(r"\d", s1)
    #print(m)
    sum+=int(m[0]+m[-1])
    print(sum)




# part 2
o = 0
for i in range(len(f)):
    x = f[i]
    y = ""
    for i in range(len(x)):
        if x[i] in "0123456789":
            y += x[i]
        # PART TWO CODE
        words = ["zero","one","two","three","four","five","six","seven","eight","nine"]
        for j in words:
            if x[i:i+len(j)] == j:
                y += str(words.index(j))
        
    o+= int(y[0]+y[-1])
print(o)
