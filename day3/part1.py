'''
--- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

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
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

Your puzzle answer was 551094.
'''


import re

def main():

    f = open('day3_input.txt','r')
    data = f.readlines()

    length = length_of_array(data)
    array = create_array(data)
    specials = find_specials(array,length)
    part_numbers = find_part_numbers(array,length,specials)
    sum = sum_all_part_numbers(part_numbers[0])
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
                                all_part_numbers.append(combined_part_number)
                                break
                    result = []
                    combined_part_number = ""
    return [
        all_part_numbers,
        ]
     
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
