import string

filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

def foldsum(tofold):
    for i in range(len(tofold)):
        incomplete = True
        # fold from back to front
        curridx = len(tofold) - 1 - i
        # if the element is None, it is not folded
        if tofold[curridx] == None:
            continue
        # determine whether this element should be swapped
        else:
            for i in range(curridx):
                if tofold[i] == None:
                    tofold[i], tofold[curridx] = tofold[curridx], tofold[i]
    total = 0
    for i in range(len(tofold)):
        if tofold[i] != None:
            total += i * tofold[i]
    return total

def foldclust(tofold):
    elts = []
    for i in range(len(tofold)):
        # fold from back to front
        curridx = len(tofold) - 1 - i
        # if the element is None, it is not folded
        if tofold[curridx] == None:
            continue
        # otherwise if the element is equal to the other one, we build
        elif i != len(tofold) - 1 and tofold[curridx] == tofold[curridx-1]:
            elts.append(curridx)
            continue
        # determine whether this element should be swapped
        else:
            elts.append(curridx)
            for i in range(curridx):
                if tofold[i:i + len(elts)] == [None] * len(elts):
                    for j in range(len(elts)):
                        tofold[i+j], tofold[curridx+j] = tofold[curridx+j], tofold[i+j]
            elts = []     
    total = 0
    for i in range(len(tofold)):
        if tofold[i] != None:
            total += i * tofold[i]
    return total

def part1():
    line = input[0]
    unfolded = []
    currid = 0
    isactive = True
    for char in line:
        for i in range(int(char)):
            if isactive:
                unfolded.append(currid)
            else:
                unfolded.append(None)
        if isactive:
            currid += 1
        isactive = not isactive
    return foldsum(unfolded)

def part2():
    line = input[0]
    unfolded = []
    currid = 0
    isactive = True
    for char in line:
        for i in range(int(char)):
            if isactive:
                unfolded.append(currid)
            else:
                unfolded.append(None)
        if isactive:
            currid += 1
        isactive = not isactive
    return foldclust(unfolded)

print("Part one:", part1())
print("Part two:", part2())

#6221662795602
