import functools

def all_zeros(l):
    return len([x for x in l if x != 0]) == 0

sum_of_next_values = 0
with open("9/input.txt", "r") as input:
    for l in input:
        nums = [int(n) for n in l.strip().split(" ")]

        sequence = nums[:]
        gaps = [sequence]
        while not all_zeros(sequence):
            next_sequence = []
            for i in range(len(sequence) - 1):
                next_sequence.append(sequence[i+1] - sequence[i])
            gaps.append(next_sequence)
            sequence = next_sequence
        print ("done line, gaps = {}",gaps)

        for i in range(len(gaps) - 2, -1, -1):
            gaps[i].append(gaps[i][-1] + gaps[i+1][-1])

        sum_of_next_values += gaps[0][-1]
    print("sum of all next_values is {} ".format(sum_of_next_values))
        


    


