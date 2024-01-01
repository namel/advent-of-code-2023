from datetime import datetime

subspaces = []
space_map = {'x': {}, 'm': {}, 'a': {}, 's': {}}
spaceset_map = {'x': {}, 'm': {}, 'a': {}, 's': {}}
sorted_spacesets = {}

def get_subspace(space, next_workflow, depth):
    global subspaces
    if next_workflow == 'A':  
        if space not in subspaces:
            subspaces.append(space.copy())
    elif next_workflow != 'R':
        explore_space(space, workflow_map[next_workflow], depth + 1) 
    return

def explore_space(space, workflow, depth):
    reduced_space = space.copy()
    for step in workflow[:-1]:
        test, next_w = step.split(':')
        attr, sign, value = test[0], test[1], int(test[2:])
        cur_range = reduced_space[attr]
        if sign == '>':
            if cur_range[1] <= value:
                continue
            reduced_space[attr] = [value+1, cur_range[1]]
            get_subspace(reduced_space, next_w, depth)
            reduced_space[attr] = [cur_range[0], value]
        else:
            if cur_range[0] >= value:
                continue
            reduced_space[attr] = [cur_range[0], value-1]
            get_subspace(reduced_space, next_w, depth)
            reduced_space[attr] = [value, cur_range[1]]
    get_subspace(reduced_space, workflow[-1], depth)
    return

def build_space_map():
    for sid, s in enumerate(subspaces):
        for attr in 'xmas':
            start, end = tuple(s[attr])
            if start not in space_map[attr]:
                space_map[attr][start] = []
            if end+1 not in space_map[attr]:
                space_map[attr][end+1] = []
            space_map[attr][start].append(("start", sid))
            space_map[attr][end+1].append(("end", sid))
    for attr in 'xmas':
        sorted_hits = sorted(space_map[attr].items(), key=lambda x: x[0])
        subspaces_in_range = set()
        for pos, spans in sorted_hits:
            if pos not in spaceset_map[attr]:
                spaceset_map[attr][pos] = []
            for s in spans:
                if s[0] == 'start':
                    subspaces_in_range.add(s[1])
                else:
                    subspaces_in_range.remove(s[1])
            spaceset_map[attr][pos] = subspaces_in_range.copy()   
        sorted_spacesets[attr] = sorted(spaceset_map[attr].items(), key=lambda x: x[0])

def scan_dimension(d, prev_subspaces = None):
    attr = 'xmas'[d]
    last_pos = 0
    space_size = 0
    subspace_size = 0
    for pos, spaceset in sorted_spacesets[attr]:
        if subspace_size > 0:
            space_size += subspace_size * (pos - last_pos)
        subspace_size = 0
        next_subspaces = spaceset & prev_subspaces if prev_subspaces is not None else spaceset
        if len(next_subspaces) > 0:
            subspace_size = scan_dimension(d+1, next_subspaces) if d < 3 else 1
        last_pos = pos
    return space_size

with open("19/input.txt") as input:
    lines = [l.strip() for l in input]
    workflows = [l.strip('}') for l in lines[:lines.index('')]]
    workflow_map = { w.split('{')[0]: w.split('{')[1].split(',') for w in workflows}

    # discover the sub-spaces, which have overlaps
    explore_space({'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}, workflow_map['in'], 0)

    # build a map to quickly find sub-spaces
    build_space_map()

    # scan the entire space
    total = scan_dimension(0)
    print("total = ", total)

