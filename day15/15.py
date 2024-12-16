import copy

filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

def checkblanks(area, queue):
    for coord in queue:
        if area[coord[0]][coord[1]] == ".":
            return True
    return False

def getstart(area):
    for a in range(len(area)):
        for b in range(len(area[a])):
            if area[a][b] == "@":
                return [a, b]
    return [-1, -1]

def makemove(area, direction, start, isbegin):
    # get target coordinates
    queue = [start]
    i, j = start[0], start[1]
    # up case
    if direction == "^":
        if area[i-1][j] == "#":
            return queue[:-1]
        elif area[i-1][j] == ".":
            queue.append([i-1, j])
        elif area[i-1][j] == "[":
            if makemove(area, direction, [i-1, j+1], True) == []:
                return []
            else:
                queue.extend(makemove(area, direction, [i-1, j], False))
        elif area[i-1][j] == "]":
            if makemove(area, direction, [i-1, j-1], True) == []:
                return []
            else:
                queue.extend(makemove(area, direction, [i-1, j], False))
        else:
            queue.extend(makemove(area, direction, [i-1, j], False))
        
    # right case
    elif direction == ">":
        if area[i][j+1] == "#":
            return queue[:-1]
        elif area[i][j+1] == ".":
            queue.append([i, j+1])
        else:
            queue.extend(makemove(area, direction, [i, j+1], False))
        
    # down case
    elif direction == "v":
        target = [i+1, j]
        if area[i+1][j] == "#":
            return queue[:-1]
        elif area[i+1][j] == ".":
            queue.append([i+1, j])
        elif area[i+1][j] == "[":
            if makemove(area, direction, [i+1, j+1], True) == []:
                return []
            else:
                queue.extend(makemove(area, direction, [i+1, j], False))
        elif area[i+1][j] == "]":
            if makemove(area, direction, [i+1, j-1], True) == []:
                return []
            else:
                queue.extend(makemove(area, direction, [i+1, j], False))
        else:
            queue.extend(makemove(area, direction, [i+1, j], False))
    
    # left case
    else:
        if area[i][j-1] == "#":
            return queue[:-1]
        elif area[i][j-1] == ".":
            queue.append([i, j-1])
        else:
            queue.extend(makemove(area, direction, [i, j-1], False))
    
    if len(queue) > 1 and isbegin:
        for i in range(len(queue)-1, 0, -1):
            if area[queue[i][0]][queue[i][1]] in ["@", "O"] and area[queue[i-1][0]][queue[i-1][1]] in ["@", "O"]:
                continue
            else:
                area[queue[i][0]][queue[i][1]], area[queue[i-1][0]][queue[i-1][1]] = area[queue[i-1][0]][queue[i-1][1]], area[queue[i][0]][queue[i][1]]
    return queue

def part1():
    total = 0
    area = []
    dirs = ""
    atdirs = False
    for line in input:
        if line == "":
            atdirs = True
        if atdirs:
            dirs += line
        else:
            area.append([i for i in line])
    for dx in dirs:
        makemove(area, dx, getstart(area), True)
    for i in range(len(area)):
        for j in range(len(area[i])):
            if area[i][j] == "O":
                total += 100 * i + j
    return total

def part2():
    total = 0
    area = []
    dirs = ""
    atdirs = False
    for line in input:
        if line == "":
            atdirs = True
        if atdirs:
            dirs += line
        else:
            area.append([i for i in line])
    # set up size doubling
    # create new move function with box movement recursion on u/d
    bigarea = [[] for line in area]
    for i in range(len(area)):
        for char in area[i]:
            if char == "#":
                bigarea[i].append("#")
                bigarea[i].append("#")
            elif char == "O":
                bigarea[i].append("[")
                bigarea[i].append("]")
            elif char == ".":
                bigarea[i].append(".")
                bigarea[i].append(".")
            else:
                bigarea[i].append("@")
                bigarea[i].append(".")
    area = bigarea
    count = 0
    for dx in dirs:
        count += 1
        areacopy = copy.deepcopy(area)
        makemove(area, dx, getstart(area), True)
        for i in range(len(area)):
            for j in range(len(area[i])-1):
                badleft = area[i][j] == "[" and area[i][j+1] != "]"
                badright = area[i][j] == "]" and area[i][j-1] != "["
                if area[i][j] == area[i][j+1] and area[i][j] in ["[", "]"]:
                    area = areacopy
                if badleft:
                    area = areacopy
                if badright:
                    area = areacopy
    for i in range(len(area)):
        for j in range(len(area[i])):
            if area[i][j] == "[":
                total += 100 * i + j
    return total

print("Part one:", part1())
print("Part two:", part2())
