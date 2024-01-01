import sys

sys.setrecursionlimit(100000)

DIRECTIONS = { '|': {'N','S'}, '-': {'W', 'E'}, 'L': {'N','E'}, 'F': {'S', 'E'}, '7': {'W','S'}, 'J': {'N', 'W'} }
orientations = {}
onpipe = set()
start_shape = set()

def directions(pipe):
    return DIRECTIONS.get(pipe, [])

def find_start(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'S':
                return (x, y)

# returns length of loop, or 0 if no loop found
def travel_pipes(grid, start, pos, dir, distance):
    global orientations, onpipe

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
        start_shape.add(connect)
        return distance
    
    if pos[0] < 0 or pos[0] >= len(grid[0]) or pos[1] < 0 or pos[1] >= len(grid):
        return 0
    
    new_directions = directions(grid[pos[1]][pos[0]])
    if connect not in new_directions:
        return 0
    next_direction = new_directions - { connect }
    onpipe.add(pos)

    if grid[pos[1]][pos[0]] == '7':
        orientations[pos] = '+' if connect == 'W' else '-'
    elif grid[pos[1]][pos[0]] == 'J':
        orientations[pos] = '+' if connect == 'N' else '-'
    elif grid[pos[1]][pos[0]] == 'L':
        orientations[pos] = '+' if connect == 'E' else '-'
    elif grid[pos[1]][pos[0]] == 'F':
        orientations[pos] = '+' if connect == 'S' else '-'

    return travel_pipes(grid, start, pos, next_direction.pop(), distance + 1)
    

with open("10/input.txt", "r") as input:
    grid = [l.strip() for l in input]
    s_pos = find_start(grid)
    onpipe.add(s_pos)

    # check going up:
    loop_size = 0
    for direction in ['N', 'E', 'S']:
        loop_size = travel_pipes(grid, s_pos, s_pos, direction, 1)
        if loop_size > 0:
            start_shape.add(direction)
            orientations[s_pos] = '+' # this is arbitrary from looking at data, not derived!
            break


    # replace the start marker with a real pipe:
    for (k,v) in DIRECTIONS.items():
        if v == start_shape:
            grid[s_pos[1]] = grid[s_pos[1]].replace("S", k)

    # traverse looking for borders
    is_inside = False
    inside_elements = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (x,y) in onpipe:
                match grid[y][x]:
                    case '|':
                        is_inside = not is_inside
                    case '7':
                        is_inside = orientations[(x,y)] == '+' # whether this is + or - depends on orientation of S
                    case 'J':
                        is_inside = orientations[(x,y)] == '+' # whether this is + or - depends on orientation of S
            else:
                if is_inside:
                    inside_elements += 1
            

    print("inside elements = ", inside_elements)
                
    

