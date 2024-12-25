open("input.txt").read().strip().split("\n")
p1sum=0
p2sum=0
for i in range(len(f)):
    text = f[i]
    p1 = ""
    p2 = ""
    for i in range(len(text)):
        #Part1
        if text[i] in "0123456789":
            p1 += text[i]
            p2 += text[i]
        # PART TWO CODE
        words = ["zero","one","two","three","four","five","six","seven","eight","nine"]
        for word in words:
            if text[i:i+len(word)] == word:
                p2 += str(words.index(word))
    p1sum+= int(p1[0]+p1[-1]) 
    p2sum+= int(p2[0]+p2[-1])


print("Day 1 Part 1:"+str(p1sum))
print("Day 1 Part 2:"+str(p2sum))
