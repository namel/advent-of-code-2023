def get_elements_for_line(l):
    numbers = []
    symbols = []
    num = ""
    num_start = None
    for pos in range(0, len(l)):
        if l[pos] == ".":
            if num != "":
                numbers.append((int(num), num_start, pos))
                num_start = None
                num = ""
        elif (l[pos]).isnumeric():
            num += l[pos]
            if num_start is None:
                num_start = pos
        else:
            if pos < len(l) - 1:
                symbols.append((l[pos], pos))
            if num != "":
                numbers.append((int(num), num_start, pos))
                num_start = None
                num = ""

    return (numbers, symbols)

def is_symbol(c):
    return c != "." and not c.isnumeric()

def number_touches_symbol(line_num, num, elements, lines):

    line_len = len(lines[line_num]) - 1

    # check above
    if line_num > 0:
        for top_pos in range(num[1] - 1, num[2] + 1):
            if top_pos >= 0 and top_pos < line_len:
                c = lines[line_num-1][top_pos]
                if is_symbol(c):
                    return True

    # check before
    pos = num[1] - 1
    if pos >= 0 and is_symbol(lines[line_num][pos]):
        return True
    

    # check after
    pos = num[2]
    if pos < line_len  and is_symbol(lines[line_num][pos]):
        return True

    # check below
    if line_num < len(lines) - 1:
        for bottom_pos in range(num[1] - 1, num[2] + 1):
            if bottom_pos >= 0 and bottom_pos < line_len:
                c = lines[line_num+1][bottom_pos]
                if is_symbol(c):
                    return True

    return False

total = 0
with open("3/input.txt", "r") as input:
    lines = [l for l in input]
    elements = [get_elements_for_line(l) for l in lines]
    for line_num in range(0, len(elements)):
        for num in elements[line_num][0]:
            if number_touches_symbol(line_num, num, elements, lines):
                print(num[0])
                total += num[0]

print(total)
