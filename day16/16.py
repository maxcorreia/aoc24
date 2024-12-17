from sys import argv
from heapq import heappop, heappush
from math import inf

filename = "input.txt"
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

def part1():
    dimx, dimy = (len(input[0]), len(input))
    maze = list("".join(input))
    start, end = (maze.index("S"), maze.index("E"))
    dirs = [-dimx, 1, dimx, -1]
    visited = dict()
    q = []
    highscore = inf
    paths = []
    heappush(q, (0, start, 1, ""))
    while q:
        score, pos, d, path = heappop(q)
        if score > highscore:
            break
        if (pos, d) in visited and visited[(pos, d)] < score:
            continue
        visited[(pos, d)] = score
        if pos == end:
            highscore = score
            paths.append(path)
        if maze[pos + dirs[d]] != "#":
            heappush(q, (score + 1, pos+dirs[d], d, path + "F"))
        heappush(q, (score + 1000, pos, (d + 1) % 4, path + "R"))
        heappush(q, (score + 1000, pos, (d - 1) % 4, path + "L"))

    tiles = set()
    tiles.add(start)
    for p in paths:
        t, d = (start, 1)
        for c in p:
            if c=="L": d=(d-1)%4
            elif c=="R": d=(d+1)%4
            elif c=="F":
                t+=dirs[d]
                tiles.add(t)
    return highscore, len(tiles)

print("Part one:", part1()[0])
print("Part two:", part1()[1])
