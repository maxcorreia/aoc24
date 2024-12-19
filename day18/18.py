import heapq

filename = "input.txt"
input = []
with open(filename) as file:
    input = [line.strip() for line in file.readlines()]

# directions for moving in the maze (up, down, left, right)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# manhattan heuristic
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# implement astar to find optimal path
def astar(maze):
    rows = len(maze)
    cols = len(maze[0])
    start = (0, 0)
    end = (rows - 1, cols - 1)
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, end), 0, start))
    g_costs = {start: 0}
    came_from = {}
    while open_list:
        _, g, current = heapq.heappop(open_list)
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        # explore neighbors
        for dx, dy in DIRECTIONS:
            neighbor = (current[0] + dx, current[1] + dy)
            # check if neighbor is within bounds and open
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and maze[neighbor[0]][neighbor[1]] == ".":
                tentative_g = g + 1
                # if neighbor unexplored or found a better path
                if neighbor not in g_costs or tentative_g < g_costs[neighbor]:
                    g_costs[neighbor] = tentative_g
                    f = tentative_g + heuristic(neighbor, end)
                    heapq.heappush(open_list, (f, tentative_g, neighbor))
                    came_from[neighbor] = current
    # no path found
    return None

def part1():
    coords = []
    area = []
    for line in input:
        coords.append([int(i) for i in line.split(",")])
    dim = 0
    for value in coords:
        dim = max(value[0], value[1], dim)
    dim += 1
    for i in range(dim):
        area.append(["." for j in range(dim)])
    for i in range(1024):
        area[coords[i][1]][coords[i][0]] = "#"
    dots = astar(area)
    for dot in dots:
        area[dot[0]][dot[1]] = "O"
    return len(dots) - 1

def part2():
    coords = []
    area = []
    for line in input:
        coords.append([int(i) for i in line.split(",")])
    dim = 0
    for value in coords:
        dim = max(value[0], value[1], dim)
    dim += 1
    for i in range(dim):
        area.append(["." for j in range(dim)])
    lastpath = []
    counter = 0
    while lastpath != None:
        stone = coords[counter]
        area[coords[counter][1]][coords[counter][0]] = "#"
        lastpath = astar(area)
        counter += 1
    return str(stone[0]) + "," + str(stone[1])


print("Part one:", part1())
print("Part two:", part2())
