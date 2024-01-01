import sys
sys.setrecursionlimit(100000)

DIRECTIONS = { '|': {'N','S'}, '-': {'W', 'E'}, 'L': {'N','E'}, 'F': {'S', 'E'}, '7': {'W','S'}, 'J': {'N', 'W'} }


def directions(pipe):
    return DIRECTIONS.get(pipe, [])

def find_start(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'S':
                return (x, y)

# returns length of loop, or 0 if no loop found
def travel_pipes(grid, start, pos, dir, distance):
    match dir:
        case 'N': 
            pos = (pos[0], pos[1] - 1)
            connect = 'S'
        case 'E': 
            pos = (pos[0] + 1, pos[1])
            connect = 'W'
        case 'S': 
            pos = (pos[0], pos[1] + 1)
            connect = 'N'
        case 'W': 
            pos = (pos[0] - 1, pos[1])
            connect = 'E'

    if pos == start:
        return distance
    
    if pos[0] < 0 or pos[0] >= len(grid[0]) or pos[1] < 0 or pos[1] >= len(grid):
        return 0
    
    new_directions = directions(grid[pos[1]][pos[0]])
    if connect not in new_directions:
        return 0
    next_direction = new_directions - { connect }
    
    return travel_pipes(grid, start, pos, next_direction.pop(), distance + 1)
    

with open("10/input.txt", "r") as input:
    grid = [l.strip() for l in input]
    s_pos = find_start(grid)

    # check going up:
    loop_size = 0
    for direction in ['W', 'N', 'E']:
        loop_size = travel_pipes(grid, s_pos, s_pos, direction, 1)
        if loop_size > 0:
            break

    print("largest loop had length {} max distance is half: {}".format(loop_size, loop_size / 2))


