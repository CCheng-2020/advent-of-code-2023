'''
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?

Your puzzle answer was 54418.
'''

import re

def main():
    f = open('day2_input.txt','r')
    data = f.readlines()

    lines = list(data)
    sum = 0
    for text in lines:
        forward = re.findall('[0-9]|one|two|three|four|five|six|seven|eight|nine', text)
        first_element = string_to_int(forward[0])
        last_element = string_to_int(forward[-1])
        combined_elements = first_element + last_element
        int_element = int(combined_elements)
        sum = int_element + sum
        print(sum)

def reverse_string(x):
    return x[::-1]

def string_to_int(x):
    if x == "one":
        return "1"
    if x == "two":
        return "2"
    if x == "three":
        return "3"
    if x == "four":
        return "4"
    if x == "five":
        return "5"
    if x == "six":
        return "6"
    if x =="seven":
        return "7"
    if x == "eight":
        return "8"
    if x == "nine":
        return "9"
    return x

main()



