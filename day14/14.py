from collections import defaultdict
import re
import math

filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

endcoords = defaultdict(int)

def calcend(coords, w, h, ticks, finaldict):
    psnx = coords[0]
    psny = coords[1]
    velx = coords[2]
    vely = coords[3]
    resx = (coords[0] + coords[2] * ticks) % w
    resy = (coords[1] + coords[3] * ticks) % h
    finaldict[resx, resy] += 1

# helper for calculating middle value
def middle(val):
    return ((val + 1) / 2) - 1

def ranges(nums):
    nums = sorted(set(nums))
    gaps = [[s, e] for s, e in zip(nums, nums[1:]) if s+1 < e]
    edges = iter(nums[:1] + sum(gaps, []) + nums[-1:])
    return list(zip(edges, edges))

def part1(w, h, ticks):
    for line in input:
        numbers = re.findall(r"-?\d+", line)
        calcend([int(i) for i in numbers], w, h, ticks, endcoords)
    # ul, ur, br, bl
    quadtotal = [0, 0, 0, 0]
    for val in endcoords:
        #print(val, endcoords[val])
        midx, midy = middle(w), middle(h)
        if val[0] < midx and val[1] < midy:
            quadtotal[0] += endcoords[val]
        elif val[0] > midx and val[1] < midy:
            quadtotal[1] += endcoords[val]
        elif val[0] < midx and val[1] > midy:
            quadtotal[2] += endcoords[val]
        elif val[0] > midx and val[1] > midy:
            quadtotal[3] += endcoords[val]
    print(quadtotal)
    return math.prod(quadtotal)

def part2(w, h):
    total = 0
    done = False
    while not done:
        coords = defaultdict(int)
        y_dict = defaultdict(list)
        for line in input:
            numbers = re.findall(r"-?\d+", line)
            calcend([int(i) for i in numbers], w, h, total, coords)
        for key in coords:
            y_dict[key[1]].append(key[0])
        for yvals in y_dict:
            sortdone = y_dict[yvals].copy()
            sortdone.sort()
            if sortdone != None:
                for cluster in ranges(sortdone):
                    if cluster[1] - cluster[0] >= 10:
                        done = True
        total += 1
    return total - 1

print("Part one:", part1(101, 103, 100))
print("Part two:", part2(101, 103))
