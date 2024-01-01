from collections import namedtuple

subspaces = []

def get_subspace(space, next_workflow, depth):
    global subspaces
    if next_workflow == 'A':  
        if space not in subspaces:
            subspaces.append(space)
    elif next_workflow != 'R':
        explore_space(space, workflow_map[next_workflow], depth + 1) 
    return

def get_overlap_combinations(new_subspace, scanned_space):
    overlap = 1
    for attr in 'xmas':
        overlap_span = min(new_subspace[attr][1], scanned_space[attr][1]) - max(new_subspace[attr][0], scanned_space[attr][0]) + 1
        overlap *= max(overlap_span, 0)
    return overlap

def space_overlap(s1, s2):
    overlap = {}
    for attr in 'xmas':
        overlap_span = [max(s1[attr][0], s2[attr][0]), min(s1[attr][1], s2[attr][1])]
        if overlap_span[1]<overlap_span[0]:
            return None
        overlap[attr] = overlap_span
    return overlap

def space_remove(s1, s2):
    return     

def find_remaining_overlap(new_space, known_space, already_removed):
    overlap = space_overlap(new_space, known_space)
    for ar in already_removed:
        overlap = space_remove(overlap, ar)
    return overlap

def space_size(s):
    return (s['x'][1] - s['x'][0] + 1) * (s['m'][1] - s['m'][0] + 1) * (s['a'][1] - s['a'][0] + 1) * (s['s'][1] - s['s'][0] + 1)

def count_unique_subspaces():

    # for each space, collect list of mutually exclusive overlapping subspaces (MEOS) that were already counted
    scanned_subspaces = []
    unique_combinations = 0
    for s in subspaces:
        meos_list = []
        for ss in scanned_subspaces:
            meos = find_remaining_overlap(s, ss, meos_list)
            meos_list.append(meos)
        scanned_subspaces.append(s)
        s_size = space_size(s)
        removal_sizes = [space_size(m) for m in meos_list]
        new_combinations = s_size - sum(removal_sizes)
        print("new combinations {} from subspace of size {} minus removals {}".format(new_combinations, s_size, removal_sizes))
        unique_combinations += new_combinations

    print("unique_combinations = ", unique_combinations)


def explore_space(space, workflow, depth):

    reduced_space = space.copy()
    for step in workflow[:-1]:
        test, next_w = step.split(':')
        attr, sign, value = test[0], test[1], int(test[2:])
        cur_range = reduced_space[attr]
        if sign == '>':
            if cur_range[1] <= value:
                continue
            reduced_space[attr] = [value+1, space[attr][1]]
            get_subspace(reduced_space, next_w, depth)
            reduced_space[attr] = [space[attr][0], value]
        else:
            if cur_range[0] >= value:
                continue
            reduced_space[attr] = [space[attr][0], value-1]
            get_subspace(reduced_space, next_w, depth)
            reduced_space[attr] = [value, space[attr][1]]
    get_subspace(reduced_space, workflow[-1], depth)
    return

with open("19/input.txt") as input:
    lines = [l.strip() for l in input]
    workflows = [l.strip('}') for l in lines[:lines.index('')]]
    workflow_map = { w.split('{')[0]: w.split('{')[1].split(',') for w in workflows}
    explore_space({'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}, workflow_map['in'], 0)
    print("unique combinations = ", count_unique_subspaces())
    # print("subranges identified = ", subspaces)
    # print("final combinations = ", combinations)