import math

filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

def part1():
    # initialize total, set up left and right integer lists
    total = 0
    left = []
    right = []
    for line in input:
        chunks = line.split("   ")
        left.append(int(chunks[0]))
        right.append(int(chunks[1]))
    # sort both lists from least to greatest
    left.sort()
    right.sort()
    # compare all values in ascending order and sum their differences
    for i in range(len(left)):
        total += abs(left[i] - right[i])
    return total
def part2():
    # initialize total, set up left and right integer lists
    total = 0
    left = []
    right = []
    for line in input:
        chunks = line.split("   ")
        left.append(int(chunks[0]))
        right.append(int(chunks[1]))
    # we can use list.count(item) to find out how many times
    # an element from left appears in right, and sum the products
    for lftelt in left:
        total += right.count(lftelt) * lftelt
    return total;

print("Part one:", part1())
print("Part two:", part2())
