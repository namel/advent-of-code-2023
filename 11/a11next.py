galaxies, empty_rows, empty_cols = [], [], []

MULTIPLIER_PER_GAP = 999999

def get_dist(i, j):
    x_start, x_end = min(i[0], j[0]), max(i[0], j[0])
    y_start, y_end = min(i[1], j[1]), max(i[1], j[1])
    empty_cols_in_range = [n for n in empty_cols if n > x_start and n < x_end]
    empty_rows_in_range = [n for n in empty_rows if n > y_start and n < y_end]
    x_dist = x_end - x_start + len(empty_cols_in_range) * MULTIPLIER_PER_GAP
    y_dist = y_end - y_start + len(empty_rows_in_range) * MULTIPLIER_PER_GAP
    return x_dist + y_dist


with open("11/input.txt", "r") as input:
    sum_distances = 0
    map = [l.strip() for l in input]
    y_range, x_range = len(map), len(map[0])

    # find galaxies
    for y in range(y_range):
        for x in range(x_range):
            if map[y][x] == '#':
                galaxies.append((x,y)) 

    for y in range(y_range):
        if '#' not in map[y]:
            empty_rows.append(y)

    for x in range(x_range):
        if '#' not in [line[x] for line in map]:
            empty_cols.append(x)

    for i in range(len(galaxies) - 1):
        for j in range(i+1, len(galaxies)):
            sum_distances += get_dist(galaxies[i], galaxies[j])

    print("galaxies:{}\nempty cols:{}\nempty rows:{}\n sum of distances: {}".format(galaxies, empty_cols, empty_rows, sum_distances))

    

