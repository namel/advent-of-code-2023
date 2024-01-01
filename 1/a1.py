sum = 0

with open("1/input.txt", "r") as f:
    for l in f:
        nums = [c for c in l if c.isnumeric()]
        print(nums)
        num_string = nums[0] + nums[-1]
        num = int(num_string)
        print(num)
        sum = sum + num

print(sum)

