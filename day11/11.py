import math
import functools
import time
from collections import defaultdict

filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

@functools.cache
def digs(elt):
    if elt != 0:
        return (int(math.log10(elt))+1)
    else:
        return 0 

def split(elt, vals, newvals):
    digits = digs(elt)
    # first case, stone has 0
    if elt == 0:
        if 1 in newvals:
            newvals[1] = vals[elt] + newvals[1]
        else:
            newvals[1] = vals[elt]
    # second case: stone has even number of digits
    elif digits % 2 == 0:
        first = int(elt // (10 ** (digits/2)))
        second = int(elt % (10 ** (digits/2)))
        if first in newvals:
            newvals[first] = vals[elt] + newvals[first]
        else:
            newvals[first] = vals[elt]
        if second in newvals:
            newvals[second] = vals[elt] + newvals[second]
        else:
            newvals[second] = vals[elt]
    # third case
    else:
        if elt * 2024 in newvals:
            newvals[elt * 2024] = vals[elt] + newvals[elt * 2024]
        else:
            newvals[elt * 2024] = vals[elt]

def part1(loops):
    vals = defaultdict(list)
    newvals = defaultdict(list)
    total = 0
    line = [int(elt) for elt in input[0].split(" ")]
    for elt in line:
        if elt in vals:
            vals[elt] += 1
        else:
            vals[elt] = 1
    for i in range(loops):
        for key in vals:
            split(key, vals, newvals)
        vals = newvals
        newvals = defaultdict(list)
    for key in vals:
        total += vals[key]
    return total

print("Part one:", part1(25))
print("Part two:", part1(75))
