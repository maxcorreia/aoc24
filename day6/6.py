filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

# Runs a "step" of the guards movements, returns end direction
def runstep(space, i, j, direction, obstacles):
    space[i] = space[i][:j] + "X" + space[i][j+1:]
    # Up case
    if direction == 0:
        # Up OOB, return -1
        if i - 1 < 0:
            return -1
        else:
            if space[i-1][j] == "#":
                if [i-1, j, direction] in obstacles:
                    return -2
                else:
                    obstacles.append([i-1, j, direction])
                    return runstep(space, i, j, (direction + 1) % 4, obstacles)
            else:
                space[i-1] = space[i-1][:j] + "^" + space[i-1][j+1:]
                return direction
    # Right case
    elif direction == 1:
        # Right OOB, return -1
        if j + 1 >= len(space[i]):
            return -1
        else:
            if space[i][j+1] == "#":
                if [i, j+1, direction] in obstacles:
                    return -2
                else:
                    obstacles.append([i, j+1, direction])
                    return runstep(space, i, j, (direction + 1) % 4, obstacles)
            else:
                space[i] = space[i][:j+1] + "^" + space[i][j+2:]
                return direction
    # Down case
    elif direction == 2:
        # Down OOB, return -1
        if i + 1 >= len(space):
            return -1
        else:
            if space[i+1][j] == "#":
                if [i+1, j, direction] in obstacles:
                    return -2
                else:
                    obstacles.append([i+1, j, direction])
                    return runstep(space, i, j, (direction + 1) % 4, obstacles)
            else:
                space[i+1] = space[i+1][:j] + "^" + space[i+1][j+1:]
                return direction
    # Left case
    elif direction == 3:
        # Left OOB, return -1
        if j - 1 < 0:
            return -1
        else:
            if space[i][j-1] == "#":
                if [i, j-1, direction] in obstacles:
                    return -2
                else:
                    obstacles.append([i, j-1, direction])
                    return runstep(space, i, j, (direction + 1) % 4, obstacles)
            else:
                space[i] = space[i][:j-1] + "^" + space[i][j:]
                return direction
    else:
        return -1
    return -1

def part1(data):
    space = data.copy()
    total = 0
    isloop = 0
    edgereached = False
    obstacles = []
    # 0 = Up, 1 = Right, 2 = Down, 3 = Left
    direction = 0
    while not edgereached:
        donefornow = False
        for i in range(len(space)):
            if space == []:
                break
            guardidx = space[i].find("^")
            # if a guard is found on the map and has yet to be found, run the step; otherwise continue
            if guardidx != -1 and not donefornow:
                direction = runstep(space, i, guardidx, direction, obstacles)
                if direction == -1:
                    edgereached = True
                elif direction == -2:
                    isloop += 1
                    edgereached = True
                else:
                    donefornow = True
                    continue
            else:
                continue
    for line in space:
        total += line.count("X")
    return total, isloop
        
def part2():
    space = input.copy()
    total = 0
    for i in range(len(space)):
        for j in range(len(space[i])):
            # cannot place obstacle on guard
            if space[i][j] == "^":
                continue
            newspace = [
                string[:j] + "#" + string[j+1:] if i == idx else string
                for idx, string in enumerate(space.copy())
            ]
            toplay = newspace.copy()
            if part1(toplay)[1] == 1:
                total += 1
    return total

print("Part one:", part1(input)[0])
print("Part two:", part2())
