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

def is_star(c):
    return c == "*"

def star_name(x,y):
    return "star"+str(x)+"-"+str(y)

def number_touches_star(line_num, num, elements, lines):

    line_len = len(lines[line_num]) - 1

    # check above
    if line_num > 0:
        for top_pos in range(num[1] - 1, num[2] + 1):
            if top_pos >= 0 and top_pos < line_len:
                c = lines[line_num-1][top_pos]
                if is_star(c):
                    return star_name(line_num-1, top_pos)

    # check before
    pos = num[1] - 1
    if pos >= 0 and is_star(lines[line_num][pos]):
        return star_name(line_num, pos)
    

    # check after
    pos = num[2]
    if pos < line_len  and is_star(lines[line_num][pos]):
        return star_name(line_num, pos)

    # check below
    if line_num < len(lines) - 1:
        for bottom_pos in range(num[1] - 1, num[2] + 1):
            if bottom_pos >= 0 and bottom_pos < line_len:
                c = lines[line_num+1][bottom_pos]
                if is_star(c):
                    return star_name(line_num + 1, bottom_pos)

    return None

total = 0
stars = {}
with open("3/input.txt", "r") as input:
    lines = [l for l in input]
    elements = [get_elements_for_line(l) for l in lines]
    for line_num in range(0, len(elements)):
        for num in elements[line_num][0]:
            star_found = number_touches_star(line_num, num, elements, lines)
            if star_found is not None:
                print(star_found)
                star = stars.get(star_found)
                if star is None:
                    stars[star_found] = [num]
                else:
                    star.append(num)

print(stars)
for s, nums in stars.items():
    if len(nums) == 2:
        total += nums[0][0] * nums[1][0]
print(total)
