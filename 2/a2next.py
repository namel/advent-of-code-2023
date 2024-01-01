sum = 0

with open("2/input.txt", "r") as input:
    for line in input:

        # collect the game number and turns
        part1 = line.split(":")[1]
        turns = part1.split(";")

        fewest_reds = 1
        fewest_greens = 1
        fewest_blues = 1
    
        for turn in turns:
            cubes = turn.split(",")
            for cube in cubes:
                cube_number = int(cube.strip(" ").split(" ")[0])
                if "blue" in cube:
                    if cube_number > fewest_blues:
                        fewest_blues = cube_number
                if "red" in cube:
                    if cube_number > fewest_reds:
                        fewest_reds = cube_number
                if "green" in cube:
                    if cube_number > fewest_greens:
                        fewest_greens = cube_number

        power = fewest_greens * fewest_reds * fewest_blues
        print(power)
        sum += power
print(sum)
