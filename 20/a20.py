from collections import deque


# %flip-flop
# initially OFF
# "OFF" really means l-flips ?
# OFF:
#     h ->
#     l -> h + flip ON/OFF
# ON: 
#     h -> 
#     l -> l + flip ON/OFF


# &conjunction
# initially remembers recents as l
# all high -> l
# otherwise -> h

PUSH_COUNT = 1000

# Module =>  name: type, in_list, out_list, mem
modules = {}
signal_queue = deque()


# returns list(next_signal, from_module, to_modules_list)
def propagate(signal, from_mod, mod_list):
    for m in mod_list:
        if m not in modules:
            continue
        mtype, in_list, out_list, mem = modules[m]
        if mtype == '%':
            if signal == 0:
                signal_queue.append(((0 if mem else 1), m, out_list))
                modules[m][3] = not mem
        elif mtype == '&':
            modules[m][3][from_mod] = signal
            next_signal = 1 if len([ s for s in modules[m][3].values() if s==0]) > 0 else 0
            signal_queue.append((next_signal, m, out_list))
        elif mtype == 'b':
            signal_queue.append((signal, m, out_list))


with open("20/input.txt", "r") as input:
    modules = { e[0][1:]: [e[0][0], [], [ t.strip(',') for t in e[2:]], False] for e in [l.strip().split(' ') for l in input] }
    for mod_name, mod_desc in modules.items():
        type, in_list, out_list, mem = mod_desc
        for target in out_list:
            if target in modules:
                modules[target][1].append(mod_name)
    for mod_name, mod_desc in modules.items():
        type, in_list, out_list, mem = mod_desc
        if type == '%':
            modules[mod_name][3] = False
        elif type == '&':
            modules[mod_name][3] = { incoming: 0 for incoming in [k for k, v in modules.items() if mod_name in v[2]] }
    print("modules = ", modules)
        

sig_counts = [0, 0]
for p in range(PUSH_COUNT):
    # print("PUSH!")
    signal_queue.append((0, "button", ['roadcaster']))

    while len(signal_queue) > 0:
        next_signal, this_modname, target_list = signal_queue.popleft()
        # print("signal {} from {} to {}".format(next_signal, this_modname, target_list))
        sig_counts[next_signal] += len(target_list)
        propagate(next_signal, this_modname, target_list)           
    
print("lows = {} highs = {} mult = {}".format(sig_counts[0], sig_counts[1], sig_counts[0]*sig_counts[1]))






