from collections import defaultdict
import re

filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

# we can use a dictionary of pages (keys) with lists of items they should appear after (their values)
def part1():
    total = 0
    rulelist = []
    updates = []
    ruledict = defaultdict(list)
    for line in input:
        # regex differentiates between the rule and update lines
        if re.match(r"[0-9]+\|[0-9]+", line):
            rulelist.append(re.findall(r"\d+", line))
        elif "," in line:
            updates.append([int(x) for x in line.split(",")])
        else:
            continue
    # create our rule dictionary
    for rule in rulelist:
        ruledict[int(rule[1])].append(int(rule[0]))
    # check all updates for safety
    for update in updates:
        safe = True
        for idx, num in enumerate(update):
            # we go through all rules against an update
            for rulenum in ruledict[num]:
                # if the rule is broken in our update, it is not safe
                if rulenum in update[idx:]:
                    safe = False
                    break
            if not safe:
                break
        else:
            total += update[len(update)//2]
    return total

def part2():
    total = 0
    rulelist = []
    updates = []
    ruledict = defaultdict(list)
    for line in input:
        # regex differentiates between the rule and update lines
        if re.match(r"[0-9]+\|[0-9]+", line):
            rulelist.append(re.findall(r"\d+", line))
        elif "," in line:
            updates.append([int(x) for x in line.split(",")])
        else:
            continue
    # create our rule dictionary
    for rule in rulelist:
        ruledict[int(rule[1])].append(int(rule[0]))
    # we change our approach for faulty updates
    for update in updates:
        # beenunsafe => was a fixed update deemed unsafe before
        # safe => is the update safe now
        beenunsafe = False
        safe = False
        while not safe:
            safe = True
            for idx, num in enumerate(update):
                for rulenum in ruledict[num]:
                    # unlike part 1, trips if a pairing is invalid
                    if rulenum in update[idx:]:
                        safe = False
                        # this list was previously unsafe
                        beenunsafe = True
                        rulenumidx = update.index(rulenum)
                        # swap the elements based on the rules, continue
                        update[idx], update[rulenumidx] = update[rulenumidx], update[idx]
        if beenunsafe:
            total += update[len(update)//2]
    return total

print("Part one:", part1())
print("Part two:", part2())
