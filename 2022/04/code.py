import re
def p1():
    v=0
    for line in open("input.txt"):
        a, b, c, d = map(int, re.findall('\d+', line))

        if a <= c and b >= d or c <= a and d >= b:
            v += 1


    print(v)
    
def p2():
    v=0
    for line in open("input.txt"):
        a, b, c, d = map(int, re.findall('\d+', line))

        if c <= a <= d or c <= b <= d or a <= c <= b or a <= d <= b:
            v += 1


    print(v)
p2()