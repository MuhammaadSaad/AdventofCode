
import json
import functools as ft
def compare(left, right):
    # 1: a < b
    # 0: a == b
    # -1: a > b

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left == right:
            return 0
        else:
            return -1

    elif isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))):
            k = compare(left[i], right[i])
            if k == 1:
                return 1
            elif k == -1:
                return -1

        if len(left) < len(right):
            return 1
        elif len(left) > len(right):
            return -1
        else:
            assert len(left) == len(right)
            return 0

    elif isinstance(left, list) and isinstance(right, int):
        return compare(left, [right])

    else:
        assert isinstance(left, int)
        assert isinstance(right, list)
        return compare([left], right)
    

# def parse(data):
#     # [1,1,3,1,1] parse into list
    
#     break
def solve(part1):
    data = open('test.txt').read().strip()
    S = 0
    PairsP2 = [
        [[2]],
        [[6]],
    ]
    pairs = data.split("\n\n")

    for i, pair in enumerate(pairs, 1):
        a, b = pair.split("\n")
        # lis = ['1', '-4', '3', '-6', '7']
        a = json.loads(a)
        b = json.loads(b)
        if part1:
            if compare(a, b) == 1:
                # print(a, b)
                S = S + i
        if not part1:
            PairsP2.append(a)
            PairsP2.append(b)
            
    if part1:
        return S
    else:
        newPairs = sorted(PairsP2, key=ft.cmp_to_key(lambda a, b: -compare(a, b)))

        S = 1
        for i, k in enumerate(newPairs, 1):
            if k == [[2]]:
                S *= i
            elif k == [[6]]:
                S *= i
        return S
print("Part 1:", solve(True))
print("part 2:", solve(False))
