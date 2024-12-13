filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

regions = [[]]

# takes in neighbors to a region
def absorbneighbors(region, i, j):
    if i + 1 < len(input) and [i+1, j] not in region and input[i][j] == input[i+1][j]:
        region.append([i+1, j])
        absorbneighbors(region, i+1, j)
    if j+1 < len(input[i]) and [i, j+1] not in region and input[i][j] == input[i][j+1]:
        region.append([i, j+1])
        absorbneighbors(region, i, j+1)
    if i - 1 >= 0 and [i-1, j] not in region and input[i][j] == input[i-1][j]:
        region.append([i-1, j])
        absorbneighbors(region, i-1, j)
    if j - 1 >= 0 and [i, j-1] not in region and input[i][j] == input[i][j-1]:
        region.append([i, j-1])
        absorbneighbors(region, i, j-1)

# we do not change the input
def createregion(i, j):
    found = False
    for region in regions:
        if [i, j] in region:
            found = True
    if not found:
        regions.append([[i, j]])
        absorbneighbors(regions[-1], i, j)

def calcperim(region):
    total = 0
    for elt in region:
        elttotal = 4
        if [elt[0] + 1, elt[1]] in region:
            elttotal += -1
        if [elt[0], elt[1] + 1] in region:
            elttotal += -1
        if [elt[0] - 1, elt[1]] in region:
            elttotal += -1
        if [elt[0], elt[1] - 1] in region:
            elttotal += -1
        total += elttotal
    return total

def calcsides(region):
    total = 0
    for i in range(-1, len(input) + 1):
        for j in range(-1, len(input[0]) + 1):
            local = 0
            edgecase = 0
            if [i, j] in region:
                local += 1
                # edgecase used in case indices are diagonal => ec in [2, -2]
                edgecase += 1
            if [i, j+1] in region:
                local += 1
                edgecase += -1
            if [i+1, j] in region:
                local += 1
                edgecase += -1
            if [i+1, j+1] in region:
                local += 1
                edgecase += 1
            if edgecase % 4 == 2:
                total += 2
            else:
                total += local % 2
    return total

def part1(func):
    total = 0
    areamap = []
    for i in range(len(input)):
        areamap.append([])
        for j in range(len(input[i])):
            areamap[i].append(input[i][j])

    for i in range(len(input)):
        for j in range(len(input[i])):
            createregion(i, j)
    
    for region in regions:
        total += func(region) * len(region)
    return total

print("Part one:", part1(calcperim))
print("Part two:", part1(calcsides))
