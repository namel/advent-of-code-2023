


def get_points(line):
    hits = 0
    lists = line.split(":")[1].split("|")
    nums1 = lists[0].lstrip().rstrip().split(" ")
    nums2 = lists[1].lstrip().rstrip().split(" ")
    nums1_int = [int(x) for x in nums1 if x != '']
    nums2_int = [int(x) for x in nums2 if x != '']
    for i in nums2_int:
        if i in nums1_int:
            if hits == 0:
                hits = 1
            else:
                hits = hits * 2
    return hits

total = 0
with open("4/input.txt", "r") as input:
    for l in input:
        points = get_points(l)
        print(points)
        total += points
print(total)
