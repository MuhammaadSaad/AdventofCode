lines="""24 38 52 66 80 94 108 122 136 150 164 178 192 206 220 234 248 262 276 290 304
1 6 8 2 -10 -6 67 305 879 2127 4775 10402 22342 47347 98546 200559 398101 770084 1452146 2671762 4801686
13 21 20 3 -33 -68 -21 310 1329 3739 8646 17657 32955 57330 94141 147180 220405 317505 441256 592623 769559"""
def is_all_zero(nums):
    for n in nums:
        if n != 0:
            return False
    return True


p1_total = 0
p2_total = 0
for hist in lines.split('\n'):
    nums = [int(n) for n in hist.split()]
    sets = [nums]

    while not is_all_zero(sets[-1]):
        ns = []
        for i in range(0, len(sets[-1]) - 1):
            ns.append(sets[-1][i + 1] - sets[-1][i])
        sets.append(ns)

    next_last = 0
    next_start = 0
    for i in range(len(sets) - 2, -1, -1):
        next_last = sets[i][-1] + next_last
        next_start = sets[i][0] - next_start

    p1_total += next_last
    p2_total += next_start


print(p1_total)
print(p2_total)
