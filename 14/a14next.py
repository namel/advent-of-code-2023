import itertools
import time

matrix, row_len, col_len = [], 0, 0

# get pos along col
def get_pos_col(colid, offset, reverse):
    global row_len, matrix
    return (col_len - offset - 1) * row_len + colid if reverse else offset * row_len + colid
    
# get pos along row
def get_pos_row(rowid, offset, reverse):
    global col_len, matrix
    return (rowid+1) * row_len - offset - 1 if reverse else rowid * row_len + offset 

def pack_col(colid, reverse):
    next_drop = 0
    for pos in range(col_len):
        c = matrix[get_pos_col(colid, pos, reverse)]
        if c == '#':
            next_drop = pos + 1
        if c == 'O':
            if next_drop != pos:
                matrix[get_pos_col(colid, next_drop, reverse)] = 'O'
                matrix[get_pos_col(colid, pos, reverse)] = '.'
            next_drop += 1

def pack_row(rowid, reverse):
    next_drop = 0
    for pos in range(row_len):
        c = matrix[get_pos_row(rowid, pos, reverse)]
        if c == '#':
            next_drop = pos + 1
        if c == 'O':
            if next_drop != pos:
                matrix[get_pos_row(rowid, next_drop, reverse)] = 'O'
                matrix[get_pos_row(rowid, pos, reverse)] = '.'
            next_drop += 1

def print_matrix():
    for row in range(col_len):
        print("".join([matrix[get_pos_row(row, x, reverse=False)] for x in range(row_len)]))

with open("14/input.txt", "r") as input:
    lines = [[c for c in l.strip()] for l in input]
    matrix = list(itertools.chain(*lines))

    row_len = len(lines[0])
    col_len = len(lines)

    start_time = time.time()
    print("[{}] original matrix:".format(start_time))
    print_matrix()

    hashes = set()
    ITERS = 10**9
    HASH_CHECK_START = 10**4 
    first_hash_match = None
    second_hash_match = None
    iter = 0
    while iter < ITERS:
        # North, West, South, East:
        for col in range(col_len):
            pack_col(col, reverse=False)
        for row in range(row_len):
            pack_row(row, reverse=False)
        for col in range(col_len):
            pack_col(col, reverse=True)
        for row in range(row_len):
            pack_row(row, reverse=True)
        if iter > HASH_CHECK_START:
            if first_hash_match is None:
                h = hash("".join(matrix))
                if h in hashes:
                    print("hash found at iter ", iter)
                    first_hash_match = (h, iter)
                else:
                    hashes.add(h)
            else:
                if second_hash_match is None:
                    h = hash("".join(matrix))
                    if h == first_hash_match[0]:
                        print("found again at iter ", iter)
                        second_hash_match = (h, iter)
                        cycle = second_hash_match[1] - first_hash_match[1]
                        offset = iter % cycle
                        last_cycle = ITERS // cycle
                        final_iter = last_cycle*cycle + offset
                        print("cycle={} offset={} last_cycle={} final_iter={}".format(cycle, offset, last_cycle, final_iter))
                        iter = final_iter
        # print("\niter = {}", iter)
        # print_matrix()
        iter += 1
    print("[{}] iter={}".format(time.time() - start_time, iter))
    print_matrix()
    
    total = 0 
    for row in range(col_len):
        score = 0
        for col in range(row_len):
            if matrix[get_pos_row(row, col, reverse=False)] == 'O':
                score += col_len - row
        print("row score ", score)
        total += score
    print("total score ", total)




