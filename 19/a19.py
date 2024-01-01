from collections import namedtuple


WorkFlow = namedtuple("WorkFlow", ('name', 'steps'))
Part = namedtuple("Part", ('x', 'm', 'a', 's'))

def next_process(p, next_w):
    if next_w == 'A':  
        return sum(p)
    if next_w == 'R':
        return 0
    return process(p, workflow_map[next_w])    

def process(p, w):
    for step in w[:-1]:
        test, next_w = step.split(':')
        attr = test[0]
        success = getattr(p,attr) < int(test[2:]) if test[1] == '<' else getattr(p, attr) > int(test[2:])
        if success:
            return next_process(p, next_w)
    return next_process(p, w[-1])


with open("19/input.txt") as input:
    lines = [l.strip() for l in input]
    workflows = [l.strip('}') for l in lines[:lines.index('')]]
    parts = [Part(*[int(a.strip('xmas=')) for a in l.strip('{}').split(',')]) for l in lines[lines.index('') + 1:]]
    workflow_map = { w.split('{')[0]: w.split('{')[1].split(',') for w in workflows}

    rating = 0
    for p in parts:
        rating += process(p, workflow_map['in'])

    print("final rating = ", rating)