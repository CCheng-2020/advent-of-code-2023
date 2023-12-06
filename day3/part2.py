'''
--- Part Two ---
The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?

Your puzzle answer was 80179647.
'''

import re

def main():

    f = open('day3_input.txt','r')
    data = f.readlines()

    length = length_of_array(data)
    array = create_array(data)
    specials = find_specials(array,length)
    part_numbers = find_part_numbers(array,length,specials)
    sum = sum_all_part_numbers(part_numbers)
    print(sum)

def sum_all_part_numbers(array):
    sum = 0 
    for n in range(len(array)):
        sum = sum + int(array[n])
    return sum

def length_of_array(lines):
    for row in lines:
        chars = list(row)
    return len(chars)
    
def create_array(lines):
    array = []

    for row in lines:
        chars = list(row)
        array.append(chars)
    return array

def find_part_numbers(array,length,specials):
    all_part_numbers =[]
    combined_part_number = ""
    result = []
    specials_count = []
    combined_part_count = []

    for n in range(len(array)):
        for i in range(length):
            part_number = re.findall("[0-9]",array[n][i])         
            if part_number:
                combined_part_number = combined_part_number + part_number[0] 
                index_no = str(n) +"," + str(i)            
                result.append(check_adjacency(index_no,len(array)))
            else:
                if combined_part_number:
                    for k in range(len(specials)):
                        for l in range(len(result)):
                            if specials[k] in result[l]:
                                specials_count.append(specials[k])
                                combined_part_count.append(combined_part_number)
                                all_part_numbers.append(combined_part_number)
                                break
                    result = []
                    combined_part_number = ""
    
    gear_ratio = find_duplicates(specials_count,combined_part_count)


    return gear_ratio

def find_duplicates(specials_count, combined_part_count):

    gear_ratio_array = []
    gear_ratio = 1

    duplicates = [x for x in specials_count if specials_count.count(x) == 2]
    dupes_array = list(set(duplicates))


    for n in range(len(dupes_array)):
        for i in range(len(specials_count)):
            if dupes_array[n] == specials_count[i]:
                gear_ratio = int(combined_part_count[i]) * gear_ratio
        gear_ratio_array.append(gear_ratio)
        gear_ratio=1

    return(gear_ratio_array)
               
def find_specials(array,length):
    index = []
    for n in range(len(array)):
        for i in range(length):
            special = re.findall("[*#+$/@%&=-]",array[n][i])
            if special:
                index_no = str(n) +"," + str(i)
                index.append(index_no)
    return index

def check_adjacency(index,length):
    new_index = []

    split_comma = re.split(",", index)
    x = int(split_comma[0]) +1
    y = int(split_comma[1])
    if x == -1 or y == -1 or x > length or y > length:
        x=int(split_comma[0])
        y=int(split_comma[1])
    index_no = str(x) +"," + str(y)
    new_index.append(index_no)

    split_comma = re.split(",", index)
    x = int(split_comma[0]) - 1
    y = int(split_comma[1])
    if x == -1 or y == -1 or x > length or y > length:
        x=int(split_comma[0])
        y=int(split_comma[1])
    index_no = str(x) +"," + str(y)
    new_index.append(index_no)

    #check left
    split_comma = re.split(",", index)
    x = int(split_comma[0]) -1
    y = int(split_comma[1]) -1
    if x == -1 or y == -1 or x > length or y > length:
        x=int(split_comma[0])
        y=int(split_comma[1])
    index_no = str(x) +"," + str(y)
    new_index.append(index_no)

    split_comma = re.split(",", index)
    x = int(split_comma[0]) 
    y = int(split_comma[1]) -1
    if x == -1 or y == -1 or x > length or y > length:
        x=int(split_comma[0])
        y=int(split_comma[1])
    index_no = str(x) +"," + str(y)
    new_index.append(index_no)

    split_comma = re.split(",", index)
    x = int(split_comma[0]) +1
    y = int(split_comma[1]) -1
    if x == -1 or y == -1 or x > length or y > length:
        x=int(split_comma[0])
        y=int(split_comma[1])
    index_no = str(x) +"," + str(y)
    new_index.append(index_no)

    #check right
    split_comma = re.split(",", index)
    x = int(split_comma[0]) -1
    y = int(split_comma[1]) +1
    if x == -1 or y == -1 or x > length or y > length:
        x=int(split_comma[0])
        y=int(split_comma[1])
    index_no = str(x) +"," + str(y)
    new_index.append(index_no)

    split_comma = re.split(",", index)
    x = int(split_comma[0]) 
    y = int(split_comma[1]) +1
    if x == -1 or y == -1 or x > length or y > length:
        x=int(split_comma[0])
        y=int(split_comma[1])
    index_no = str(x) +"," + str(y)
    new_index.append(index_no)

    split_comma = re.split(",", index)
    x = int(split_comma[0]) +1
    y = int(split_comma[1]) +1
    if x == -1 or y == -1 or x > length or y > length:
        x=int(split_comma[0])
        y=int(split_comma[1])
    index_no = str(x) +"," + str(y)
    
    new_index.append(index_no)

    return new_index

main()
