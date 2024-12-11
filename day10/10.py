from collections import defaultdict

filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

seenends = defaultdict(list)

def trailhead(topmap, i, j, coords):
    total = 0
    # end of recursion state
    if topmap[i][j] == 9 and [i, j] not in seenends[coords[0], coords[1]]:
        seenends[coords[0], coords[1]].append([i, j])
        return 1
    # cases ordered up, right, down, left
    # up case
    if i - 1 >= 0 and topmap[i][j] + 1 == topmap[i-1][j]:
        total += trailhead(topmap, i-1, j, coords)
    # right case
    if j + 1 < len(topmap[i]) and topmap[i][j] + 1 == topmap[i][j+1]:
        total += trailhead(topmap, i, j+1, coords)
    # down case
    if i + 1 < len(topmap) and topmap[i][j] + 1 == topmap[i+1][j]:
        total += trailhead(topmap, i+1, j, coords)
    # left case
    if j - 1 >= 0 and topmap[i][j] + 1 == topmap[i][j-1]:
        total += trailhead(topmap, i, j-1, coords)
    return total

def trailheadall(topmap, i, j):
    total = 0
    # end of recursion state
    if topmap[i][j] == 9:
        return 1
    # cases ordered up, right, down, left
    # up case
    if i - 1 >= 0 and topmap[i][j] + 1 == topmap[i-1][j]:
        total += trailheadall(topmap, i-1, j)
    # right case
    if j + 1 < len(topmap[i]) and topmap[i][j] + 1 == topmap[i][j+1]:
        total += trailheadall(topmap, i, j+1)
    # down case
    if i + 1 < len(topmap) and topmap[i][j] + 1 == topmap[i+1][j]:
        total += trailheadall(topmap, i+1, j)
    # left case
    if j - 1 >= 0 and topmap[i][j] + 1 == topmap[i][j-1]:
        total += trailheadall(topmap, i, j-1)
    return total

def part1():
    total = 0
    topmap = []
    for line in range(len(input)):
        topmap.append([])
        for char in input[line]:
            if char == ".":
                topmap[line].append(-1)
            else:
                topmap[line].append(int(char))
    for i in range(len(topmap)):
        for j in range(len(topmap[i])):
            if topmap[i][j] == 0:
                seenends[i, j] = [] 
                value = trailhead(topmap, i, j, [i, j])
                total += value
    return total
            

def part2():
    total = 0
    topmap = []
    for line in range(len(input)):
        topmap.append([])
        for char in input[line]:
            if char == ".":
                topmap[line].append(-1)
            else:
                topmap[line].append(int(char))
    for i in range(len(topmap)):
        for j in range(len(topmap[i])):
            if topmap[i][j] == 0:
                value = trailheadall(topmap, i, j)
                total += value
    return total

print("Part one:", part1())
print("Part two:", part2())
