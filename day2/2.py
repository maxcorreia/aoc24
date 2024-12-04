filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

# function to determine if a list of integers is safe given the rules
def isSafe(values):
    isIncreasing = False
    isDecreasing = False
    for i in range(len(values) - 1):
        # checks if values are within 1 to 3 places of each other
        if abs(values[i] - values[i+1]) in range (1, 4):
            # first two statements check if the list is incrementing or not
            if values[i] > values[i+1] and isIncreasing == isDecreasing:
                isDecreasing = True
            elif values[i] < values[i+1] and isIncreasing == isDecreasing:
                isIncreasing = True
            # given the setting above, we check down the list
            elif (values[i] < values[i+1] and isIncreasing) or (values[i] > values[i+1] and isDecreasing):
                continue
            else:
                # this list is unsafe given our rules
                return False
        else:
            # this list is unsafe given our rules
            return False
    return True

def part1():
    total = 0
    for line in input:
        raw = line.split(" ")
        vals = [int(item) for item in raw]
        # we run our safety check once per list
        if isSafe(vals):
            total += 1
    return total

def part2():
    total = 0
    for line in input:
        raw = line.split(" ")
        vals = [int(item) for item in raw]
        # for the second part, we also want to determine safety for lists with any one index removed
        canBeSafe = False
        # if the original list is safe, we can determine safety immediately
        if isSafe(vals):
            canBeSafe = True
        # we iterate over the list and remove the first, second, etc. index
        for i in range(len(vals)):
            # we make copies to avoid overriding the original values
            testVals = vals.copy()
            del testVals[i]
            if isSafe(testVals):
                canBeSafe = True
        # we add to the total if any of the original/mutations are safe
        if canBeSafe:
            total +=1
    return total

print("Part one:", part1())
print("Part two:", part2())
