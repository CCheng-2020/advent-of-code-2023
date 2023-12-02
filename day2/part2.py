'''
--- Part Two ---
The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure why the water stopped; however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!

As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?

Your puzzle answer was 54911.
'''

import re

def main():

    f = open('day2input.txt','r')
    data = f.readlines()
    sum_of_power = 0

    lines = list(data)

    for text in range(len(lines)):
        split_line = re.split(":",lines[text])
        cube_segment = split_line[1]
        power_of_cube = parse_cube_segment(cube_segment)
        sum_of_power += power_of_cube
    print(sum_of_power)

def parse_game(x):
    split_space = re.split("\s",x)
    return(split_space[1])

def parse_cube_segment(x):
    blue_array =[]
    red_array =[]
    green_array =[]
    split_semicolon = re.split(";",x)

    for n in range(len(split_semicolon)):
        split_comma = re.split(",",split_semicolon[n])
        for i in range(len(split_comma)):
            split_space = re.split("\s",split_comma[i])
            for z in range(len(split_space)):
                if (split_space[z].isdigit()):                  
                    number=int(split_space[z])
                if (re.findall("blue",split_space[z])):
                    blue_array.append(number)
                if (re.findall("red",split_space[z])):
                    red_array.append(number)
                if (re.findall("green",split_space[z])):     
                    green_array.append(number)
    least_red = max(red_array)
    least_blue = max(blue_array)
    least_green = max(green_array)
    power_of_cube = least_blue * least_green * least_red
    return power_of_cube
main()
