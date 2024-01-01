import itertools
import time

matrix, row_len, col_len = [], 0, 0


def pack_col(rowid, reverse):
    next_drop = 0
    for pos in range(row_len):
        c = matrix[(col_len - pos - 1) * row_len + rowid if reverse else pos * row_len + rowid]
        if c == '#':
            next_drop = pos + 1
        if c == 'O':
            if next_drop != pos:
                matrix[(col_len - next_drop - 1) * row_len + rowid if reverse else next_drop * row_len + rowid] = 'O'
                matrix[(col_len - pos - 1) * row_len + rowid if reverse else pos * row_len + rowid] = '.'
            next_drop += 1

def pack_row(colid, reverse):
    next_drop = 0
    for pos in range(col_len):
        c = matrix[(colid+1) * row_len - pos - 1 if reverse else colid * row_len + pos]
        if c == '#':
            next_drop = pos + 1
        if c == 'O':
            if next_drop != pos:
                matrix[(colid+1) * row_len - next_drop - 1 if reverse else colid * row_len + next_drop] = 'O'
                matrix[(colid+1) * row_len - pos - 1 if reverse else colid * row_len + pos] = '.'
            next_drop += 1


with open("14/input.txt", "r") as input:
    lines = [[c for c in l.strip()] for l in input]
    matrix = list(itertools.chain(*lines))

    row_len = len(lines[0])
    col_len = len(lines)

    start_time = time.time()
    print("[{}] original matrix:".format(start_time))
    # print_matrix()

    for cycle in range(10000):
        for col in range(col_len):
            pack_col(col, reverse=False)
        for row in range(row_len):
            pack_row(row, reverse=False)
        for col in range(col_len):
            pack_col(col, reverse=True)
        for row in range(row_len):
            pack_row(row, reverse=True)
    print("[{}] cycle {}".format(time.time() - start_time, cycle + 1))
    # print_matrix()




