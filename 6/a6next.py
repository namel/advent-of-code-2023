
with open("6/input2.txt", "r") as input:
    lines = [l for l in input]
    times = lines[0].split(":")[1].strip().split(" ")
    distances = lines[1].split(":")[1].strip().split(" ")

    times = [int(t) for t in times if t != '']
    distances = [int(d) for d in distances if d != '']

    total_ways = 1
    for race in range(len(times)):
        ways = 0
        time = times[race]
        for loadtime in range(1, time):
            sailtime = time - loadtime 
            distance = loadtime * sailtime  
            if distance > distances[race]:
                ways += 1
            if loadtime % 1000000 == 0:
                print("1 million")
        print("{} ways to win race {}".format(ways, race))
        total_ways *= max(ways, 1)

    print(total_ways)


