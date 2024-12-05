import re

filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

def count_word_in_grid(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    count = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    # sub-helper to search
    def search_from(r, c, dr, dc):
        for i in range(word_len):
            nr, nc = r + i * dr, c + i * dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != word[i]:
                return False
        return True
    # begin search in all directions without overcounting
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if search_from(r, c, dr, dc):
                    count += 1
    return count

# rotate grid 90 degrees macro function
def rotate_90(subgrid):
    return list(zip(*subgrid[::-1]))

# creates a set of rotations for a grid/subgrid
def generate_rotations(subgrid):
    rotations = [subgrid]
    for _ in range(3):
        rotations.append(rotate_90(rotations[-1]))
    return rotations

# part 2, counts the subgrids in a grid
def count_subgrid_in_grid(grid, subgrid, wildcard='*'):
    rows = len(grid)
    cols = len(grid[0])
    subgrid_rows = len(subgrid)
    subgrid_cols = len(subgrid[0])
    count = 0
    subgrid_rotations = generate_rotations(subgrid)
    # sub-helper to check, similar to part 1
    def check_subgrid_match(r, c, subgrid):
        for i in range(subgrid_rows):
            for j in range(subgrid_cols):
                # checks against the corresponding element in the subgrid
                if subgrid[i][j] != wildcard and grid[r + i][c + j] != subgrid[i][j]:
                    return False
        return True
    for rotation in subgrid_rotations:
        for r in range(rows - subgrid_rows + 1):
            for c in range(cols - subgrid_cols + 1):
                if check_subgrid_match(r, c, rotation):
                    count += 1
    return count

def snaplist(item):
    breaklist = []
    for line in item:
        breaklist.append(list(line))
    return breaklist

def part1():
    breaklist = snaplist(input)
    return count_word_in_grid(breaklist, 'XMAS')

def part2():
    breaklist = snaplist(input)
    subgrid = [['M', '*', 'M'], ['*', 'A', '*'], ['S', '*', 'S']]
    return count_subgrid_in_grid(breaklist, subgrid)

print("Part one:", part1())
print("Part two:", part2())
