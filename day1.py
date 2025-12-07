# set up
import re
import math
codes = []
with open('day1.input', 'r') as file:
    for line in file:
        line = line.strip('\n')
        codes.append(line)

# Silver star
dial = 50
password = 0
for code in codes:
    if code[0] == 'L':
        dial = (dial - int(code[1:])) % 100      
    else:
        dial = (dial + int(code[1:])) % 100
    if dial == 0:
        password += 1

print(password)

# Gold star
dial = 50
password = 0
for code in codes:
    if code[0] == 'L':
        if (dial < int(code[1:])):
            if (dial == 0):
                password -= 1
            password += math.floor(abs(dial - int(code[1:])) / 100) + 1
        dial = (dial - int(code[1:])) % 100      
    else:
        if (dial + int(code[1:]) > 100):
            password += math.floor(abs(dial + int(code[1:])) / 100)
        dial = (dial + int(code[1:])) % 100
    if dial == 0:
        password += 1

print(password)
