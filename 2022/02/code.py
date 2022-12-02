
# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors

# Scores 1 for Rock, 2 for Paper, and 3 for Scissors

# 0 if you lost, 3 if the round was a draw, and 6 if you won

#  Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape,
# the round instead ends in a draw




score_chartPart2 = {
    'A X': 3 + 0,
    'A Y': 1 + 3,
    'A Z': 2 + 6,
    'B X': 1 + 0,
    'B Y': 2 + 3,
    'B Z': 3 + 6,
    'C X': 2 + 0,
    'C Y': 3 + 3,
    'C Z': 1 + 6,
}
score_chartP1 = {
    'A X': 1 + 3,
    'A Y': 2 + 6,
    'A Z': 3 + 0,
    'B X': 1 + 0,
    'B Y': 2 + 3,
    'B Z': 3 + 6,
    'C X': 1 + 6,
    'C Y': 2 + 0,
    'C Z': 3 + 3,
}

data=""
total=0
with open('input.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]
sumP1 = 0
sumP2 = 0
for round in data:
    sumP1 += score_chartP1[round]
    sumP2+= score_chartPart2[round]

print("Part 1",sumP1)
print("Part 2", sumP2)


