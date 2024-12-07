import re

filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]
    input = [" ".join([str(item) for item in input])]

# helper for part 2
# intended to find the earliest do and dont indices
# before the index of a mul statement
def markhelp(inputlist, elt):
    mark = -1
    for idx in inputlist:
        if idx < elt:
            mark = idx
        else:
            break
    return mark

def part1():
    total = 0
    for line in input:
        # regex to find all 'mul(x,y)' statements, for x, y are ints
        matches = re.findall(r"mul\((-?\d+),(-?\d+)\)", line)
        # adds up all of the products of the mul pairs
        for i in matches:
            total += int(i[0]) * int(i[1])
    return total

def part2():
    total = 0
    for line in input:
        # regexes to set up dos, donts, and muls
        dos = re.finditer(r"do\(\)", line)
        donts = re.finditer(r"don\'t\(\)", line)
        matches = re.finditer(r"mul\((-?\d+),(-?\d+)\)", line)
        pairs = []
        pairidxs = []
        doidxs = []
        dontidxs = []
        # collect mul pairs + indices, do indices, dont indices
        for match in matches:
            pairs.append(match.groups())
            pairidxs.append(match.start())
        for do in dos:
            doidxs.append(do.start())
        for dont in donts:
            dontidxs.append(dont.start())
        for i in range(len(pairs)):
            dontmark = markhelp(dontidxs, pairidxs[i])
            domark = markhelp(doidxs, pairidxs[i])
            # includes a mul product if a do is later
            # than a dont before the mul
            if domark >= dontmark:
                total += int(pairs[i][0]) * int(pairs[i][1])
    return total

print("Part one:", part1())
print("Part two:", part2())
