from collections import defaultdict
import itertools
import string

filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

# Runs an antinode calculation in one direction
def runanti(loc1, loc2):
    antiloc = [2* loc1[0] - loc2[0], 2* loc1[1] - loc2[1]]
    if antiloc[0] < 0 or antiloc[1] < 0 or antiloc[0] >= len(input) or antiloc[1] >= len(input[0]):
        return []
    else:
        return antiloc

# Runs an antinode calculation in one direction, and adds new ones
def runanti2(loc1, loc2):
    antiloc = [2* loc1[0] - loc2[0], 2* loc1[1] - loc2[1]]
    if antiloc[0] < 0 or antiloc[1] < 0 or antiloc[0] >= len(input) or antiloc[1] >= len(input[0]):
        return []
    else:
        return [antiloc] + runanti2(antiloc, loc1)

def part1():
    antidict = defaultdict(list)
    locations = []
    antennas = []
    grid = [[' ' for _ in range(len(input) + 1)] for _ in range(len(input[0]) + 1)]
    # iterate over all symbols
    for char in string.ascii_uppercase + string.ascii_lowercase + string.digits:
        for i in range(len(input)):
            for j in range(len(input[i])):
                grid[i][j] = input[i][j]
                if input[i][j] == char:
                    antidict[char].append([i, j])
                    antennas.append([i, j])
        # permutes all combinations of nodes
        perms = list(itertools.combinations(antidict[char], 2))
        for pair in perms:
            testanti = runanti(pair[1], pair[0])
            testanti2 = runanti(pair[0], pair[1])
            if testanti not in locations and testanti != []:
                locations.append(testanti)
            if testanti2 not in locations and testanti2 != []:
                locations.append(testanti2)
    for coord in locations:
        i, j = coord
        grid[i][j] = '#'
    for row in grid:
        print(' '.join(row))
    return len(locations)

def part2():
    antidict = defaultdict(list)
    locations = []
    antennas = []
    grid = [[' ' for _ in range(len(input) + 1)] for _ in range(len(input[0]) + 1)]
    # iterate over all symbols
    for char in string.ascii_uppercase + string.ascii_lowercase + string.digits:
        for i in range(len(input)):
            for j in range(len(input[i])):
                grid[i][j] = input[i][j]
                if input[i][j] == char:
                    antidict[char].append([i, j])
                    antennas.append([i, j])
        # permutes all combinations of nodes
        perms = list(itertools.combinations(antidict[char], 2))
        for pair in perms:
            testantis = runanti2(pair[1], pair[0])
            testanti2s = runanti2(pair[0], pair[1])
            if testantis != None:
                for testanti in testantis:
                    if testanti not in locations and testanti != []:
                        locations.append(testanti)
            if testanti2s != None:
                for testanti2 in testanti2s:
                    if testanti2 not in locations and testanti2 != []:
                        locations.append(testanti2)
    overlap = []
    for location in locations:
        if location in antennas:
            overlap.append(location)
    for coord in locations:
        i, j = coord
        if coord not in overlap:
            grid[i][j] = '#'
    for row in grid:
        print(' '.join(row))
    return len(locations) + len(antennas) - len(overlap)

print("Part one:", part1())
print("Part two:", part2())
