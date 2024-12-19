import re

filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

def runprogram(A, B, C, program):
    output = []
    ptr = 0
    while ptr < len(program):
        inst = program[ptr]
        op = program[ptr + 1]
        # run instructions
        match inst:
            # adv
            case 0:
                A = A // (2 ** combo(op, A, B, C))
                ptr += 2
            # bxl
            case 1:
                B = B ^ op
                ptr += 2
            # bst
            case 2:
                B = combo(op, A, B, C) % 8
                ptr += 2
            # jnz
            case 3:
                if A != 0:
                    ptr = op
                else:
                    ptr += 2
            # bxc
            case 4:
                B = B ^ C
                ptr += 2
            # out
            case 5:
                output.append(combo(op, A, B, C) % 8)
                ptr += 2
            # bdv
            case 6:
                B = A // (2 ** combo(op, output, A, B, C))
                ptr += 2
            case 7:
                C = A // (2 ** combo(op, A, B, C))
                ptr += 2
            case _:
                return "huh"
    return output

def combo(op, A, B, C):
    if op == 4:
        return A
    if op == 5:
        return B
    if op == 6:
        return C
    else:
        return op

def outstr(output):
    result = ""
    for i in output:
        result += (str(i) + ",")
    return result[:-1]

def delta(num):
    return 2 ** (3 * num)

def part1():
    A = int(re.search(r"\d+", input[0]).group())
    B = int(re.search(r"\d+", input[1]).group())
    C = int(re.search(r"\d+", input[2]).group())
    program = [int(i) for i in re.findall(r"\d+", input[4])]
    return outstr(runprogram(A, B, C, program))

def part2():
    B = int(re.search(r"\d+", input[1]).group())
    C = int(re.search(r"\d+", input[2]).group())
    program = [int(i) for i in re.findall(r"\d+", input[4])]
    # reworked strategy from r/AOC
    queue = [[15, 0]]
    possibles = []
    while queue:
        i, a = queue.pop(0)
        if i < 0:
            continue
        for o in range(8):
            testA = (a << 3) + o
            # get the program after a certain point
            target = program[i:]
            output = runprogram(testA, B, C, program)
            if output != target:
                continue
            if i == 0:
                possibles.append(testA)
            queue.append([i-1, testA])
    possibles.sort()
    return possibles[0]

print("Part one:", part1())
print("Part two:", part2())
