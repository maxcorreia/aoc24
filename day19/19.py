import re

filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

def combocount(pattern, line, combos):
    if not re.match(pattern, line):
        return 0
    # initialize dp
    dp = [0] * (len(line) + 1)
    dp[0] = 1
    # begin count of valid combos
    for i in range(1, len(line) + 1):
        for combo in combos:
            if i >= len(combo) and line[i - len(combo):i] == combo:
                dp[i] += dp[i - len(combo)]
    return dp[len(line)]

def solve():
    part1 = 0
    part2 = 0
    combos = input[0].split(", ")
    # create regex pattern based on input
    pattern = r"^((" + "|".join(combos) + r")+)$"
    for line in input[2:]:
        current = combocount(pattern, line, combos)
        part1 += min(1, current)
        part2 += current
    return part1, part2

soln = solve()
print("Part one:", soln[0])
print("Part two:", soln[1])
