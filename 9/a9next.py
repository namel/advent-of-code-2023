import functools

def all_zeros(l):
    return len([x for x in l if x != 0]) == 0

sum_of_prev_values = 0
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

        # calc the prev value at each level
        prev_value = [0] * len(gaps)
        for i in range(len(gaps) - 2, -1, -1):
            prev_value[i] = gaps[i][0] - prev_value[i+1]

        sum_of_prev_values += prev_value[0]
    print("sum of all prev_values is {} ".format(sum_of_prev_values))
        


    


