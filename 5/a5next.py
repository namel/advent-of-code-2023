MAP_LAYERS = 7
maps = [[] for i in range(MAP_LAYERS)]

def update_low(last, new_low):
    if last is None:
        return new_low
    return min(last, new_low)

def build_map(lines, current_line, layer):
    while current_line < len(lines) and len(lines[current_line]) > 1:
        new_map = lines[current_line].strip().split(" ")
        new_map = [int(n) for n in new_map]
        (dest, source, range_len) = new_map
        maps[layer].append({ "dest": dest, "source": source, "range_len": range_len})
        current_line += 1
    maps[layer].sort(key=lambda x: x["source"])
    return current_line

# tuples are destination, source, range length
def lookup(n, span_size, layer):
    lowest = None
    
    if layer == len(maps):
        return n

    map_entry = 0
    while span_size > 0:

        # check last empty range
        if map_entry == len(maps[layer]):
            lowest = update_low(lowest, lookup(n, span_size, layer + 1))
            span_size = 0
            continue


        m = maps[layer][map_entry]

        # check empty range
        if n < m["source"]:
            subspan_size = min(span_size, m["source"] - n)
            lowest = update_low(lowest, lookup(n, subspan_size, layer + 1))
            span_size -= subspan_size
            n += subspan_size
            continue
        
        if n >= m["source"] and n < m["source"] + m["range_len"]:
            offset = n - m["source"]
            next_num = m["dest"] + offset
            subspan_size = min(span_size, m["range_len"] - offset)
            lowest = update_low(lowest, lookup(next_num, subspan_size, layer + 1))
            span_size -= subspan_size
            n += subspan_size
        map_entry += 1

    return lowest

with open("5/input.txt", "r") as input:
    lines = [l for l in input]
    seeds = lines[0].split(":")[1].strip().split(" ")
    seeds = [int(n) for n in seeds]
    current_line = 3

    for layer in range(0, MAP_LAYERS):
        current_line = build_map(lines, current_line, layer)
        current_line += 2
        print(maps[layer])


    lowest_location = None
    for s_range in range(0, int(len(seeds)/ 2)):
        print("lookup seeds at {}".format(seeds[s_range*2]))
        location = lookup(seeds[s_range*2], seeds[s_range*2 + 1], 0)
        lowest_location = update_low(lowest_location, location)

    print("lowest location is {}".format(lowest_location))
    