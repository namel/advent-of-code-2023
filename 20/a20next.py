from collections import deque
from datetime import datetime


PUSH_COUNT = 1000

# Module =>  name: type, in_list, out_list, mem
modules = {}
signal_queue = deque()


# returns list(next_signal, from_module, to_modules_list)
def propagate(signal, from_mod, mod_list, press):
    if 'rx' in mod_list and signal == 0:
        return True

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
    return False


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
p = 0
done = False
important_conjunctions = ['qs', 'mj', 'cs', 'rd']
while not done:
    p += 1
    if p % 2**22 == 0:
        print("[{}] push = {}".format(datetime.now(), p))
    signal_queue.append((0, "button", ['roadcaster']))

    while len(signal_queue) > 0:
        next_signal, this_modname, target_list = signal_queue.popleft()
        if this_modname in important_conjunctions and next_signal == 0:
            print("conjunction {} emits {} at press {} ".format(this_modname, next_signal, p))
            important_conjunctions.remove(this_modname)
        if propagate(next_signal, this_modname, target_list, p):
            done = True

    state = [v[3] for k, v in sorted(modules.items(), key= lambda x: x[0])]
    ds = ''
    for s in state:
        if s == False:
            ds += 'F'
        elif s == True:
            ds += 'T'
        else:
            ds += ''.join([str(v) for v in s.values()])


# rs gets its inputs from &bt, &dl, &fr, &rv.  These are inveters of 4 conjunctions
# the code above prints very quickly the period (number of presses) for each input.
#
# running the program shows that the 4 important conjunctions emit l at: 
# conjunction mj emits 0 at press 3739 
# conjunction cs emits 0 at press 3821 
# conjunction rd emits 0 at press 3943 
# conjunction qs emits 0 at press 4001
#
# the least common multiple for these 4 numbers is : LCM = 225,386,464,601,017
# on that press, they all emit "l" at the same time, and the 4 inputs of rs emit a high
            
# so that is the solution for my input data: 225386464601017

            
    
