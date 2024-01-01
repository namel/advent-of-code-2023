sum = 0

digit_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open("1/input.txt", "r") as f:
    for l in f:
        nums_found = []
        for pos in range(0,len(l) - 1):
            if (l[pos]).isnumeric():
                nums_found.append(l[pos])
            else:
                for n in range (1, 10):
                    digit_word = digit_words[n-1]
                    if (l[pos:(pos + len(digit_word))] == digit_word):
                        nums_found.append(str(n))
        print(nums_found)
        num_string = nums_found[0] + nums_found[-1]
        num = int(num_string)
        print(num)
        sum += num

print(sum)

