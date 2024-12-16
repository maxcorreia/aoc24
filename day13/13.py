import re
from sympy import solve
from sympy.abc import x, y

filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

def getcost(anum, bnum):
    return (anum * 3) + bnum

def findcombo(a, b, target):
    soln = solve([a[0] * x + b[0] * y - target[0], a[1] * x + b[1] * y - target[1]], [x, y])
    if int(soln[x]) == soln[x] and int(soln[y]) == soln[y]:
        return 3 * int(soln[x]) + int(soln[y])
    return 0


def part1(surplus):
    total = 0
    for i in range(int((len(input) + 1) / 4)):
        avals = [int(a) for a in re.findall("[0-9]+", input[i*4])]
        bvals = [int(b) for b in re.findall("[0-9]+", input[(i*4)+1])]
        target = [surplus + int(c) for c in re.findall("[0-9]+", input[(i*4)+2])]
        currcost = findcombo(avals, bvals, target)
        total += currcost
    return total

print("Part one:", part1(0))
print("Part two:", part1(10000000000000))
