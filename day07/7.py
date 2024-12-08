import math

filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

def genst(ops, i):
    if len(i) == 0:
        if len(ops) > 1:
            return int(ops[-1]) + genst(ops[:-1], i[1:])
        else:
            return int(ops[-1])
    else:
        # multiply
        if i[0] == "1":
            return int(ops[-1]) * genst(ops[:-1], i[1:])
        # add
        else:
            return int(ops[-1]) + genst(ops[:-1], i[1:])

def evaleq(final, ops):
    binrange = 2 ** (len(ops) - 1)
    for i in range(binrange):
        binops = str(bin(i)[2:].zfill(int(len(ops) - 1)))
        statement = genst(ops, binops)
        if final == statement:
            return final
    return 0

def ternary(n):
    if n == 0:
        return "0"
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return "".join(reversed(nums))

def genst_con(ops, i):
    if len(i) == 0:
        if len(ops) > 1:
            return int(ops[-1]) + genst_con(ops[:-1], i[1:])
        else:
            return int(ops[-1])
    else:
        # multiply
        if i[0] == "1":
            return int(ops[-1]) * genst_con(ops[:-1], i[1:])
        # concatenate
        if i[0] == "2":
            return int(str(genst_con(ops[:-1], i[1:]))+str(ops[-1]))
        # add
        else:
            return int(ops[-1]) + genst_con(ops[:-1], i[1:])

def evaleq_3(final, ops):
    tertrange = 3 ** (len(ops) - 1)
    for i in range(tertrange):
        tertops = str(ternary(i).zfill(int(len(ops) - 1)))
        statement = genst_con(ops, tertops)
        if final == statement:
            return final
    return 0

def part1():
    total = 0
    finalslist = []
    opslist = []
    for line in input:
        splitline = line.split(": ")
        finalslist.append(int(splitline[0]))
        opslist.append([int(x) for x in splitline[1].split(" ")])
    for i in range(len(finalslist)):
        total += evaleq(finalslist[i], opslist[i])
    return total

def part2():
    total = 0
    finalslist = []
    opslist = []
    for line in input:
        splitline = line.split(": ")
        finalslist.append(int(splitline[0]))
        opslist.append([int(x) for x in splitline[1].split(" ")])
    for i in range(len(finalslist)):
        total += evaleq_3(finalslist[i], opslist[i])
    return total

print("Part one:", part1())
print("Part two:", part2())
