# with open('input.txt') as f:
#     # lines = [  line.strip() for line in f]
#     # print(lines)
#     IN = f.read()
#     it = IN.strip()
import sys

def main():
    f = open('input.txt')
    g = [list(l.rstrip('\n')) for l in f]
    width = len(g[0])
    height = len(g)

    def rstep(g):
        moves = []
        for r, row in enumerate(g):
            for c, item in enumerate(row):
                if item == '>':
                    nextpos = (r, (c + 1) % width)
                    if getindex(g, nextpos) == '.':
                        moves.append(((r, c), nextpos))
        for old, new in moves:
            setindex(g, old, '.')
            setindex(g, new, '>')
        return g, bool(moves)

    def dstep(g):
        moves = []
        for r, row in enumerate(g):
            for c, item in enumerate(row):
                if item == 'v':
                    nextpos = ((r + 1) % height, c)
                    if getindex(g, nextpos) == '.':
                        moves.append(((r, c), nextpos))
        for old, new in moves:
            setindex(g, old, '.')
            setindex(g, new, 'v')
        return g, bool(moves)

    step = 1
    while True:
        g, rchanged = rstep(g)
        g, dchanged = dstep(g)
        if not rchanged and not dchanged:
            print(step)
            return
        step += 1

def getindex(mygrid, vec):
    for x in vec:
        mygrid = mygrid[x]
    return mygrid

def setindex(mygrid, vec, value):
    for x in vec[:-1]:
        mygrid = mygrid[x]
    mygrid[vec[-1]] = value

if __name__ == '__main__':
    main()