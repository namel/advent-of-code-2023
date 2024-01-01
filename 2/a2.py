# Determine which games would have been possible if the bag had been loaded with only 
# 12 red cubes, 13 green cubes, and 14 blue cubes. 
sum = 0

with open("2/input.txt", "r") as input:
    for line in input:
        line_parts = line.split(":")
        part0 = line_parts[0]
        part1 = line_parts[1]
        game_number = part0[5:]
        turns = part1.split(";")
        print(game_number, turns)

        # check if there is one bad turn
        good_turn = True
        for turn in turns:
            cubes = turn.split(",")
            for cube in cubes:
                cube_number = int(cube.strip(" ").split(" ")[0])
                if "blue" in cube:
                    if cube_number > 14:
                        good_turn = False
                if "red" in cube:
                    if cube_number > 12:
                        good_turn = False
                if "green" in cube:
                    if cube_number > 13:
                        good_turn = False

        if good_turn:
            sum += int(game_number)
        else:
            print("bad game found: ", part1)

print(sum)

