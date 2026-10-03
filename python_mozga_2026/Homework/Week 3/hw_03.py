# Write a function which count number of lines and number of words in a text.
# The text should be retrieved from a file. (Hint 1: read all lines and count them.
# Hint 2: For each line split with the white space as delimiter and count parts).

import random
file = open("data.txt")

line_count = 0
word_count = 0

for lines in file:
    line_count = line_count + 1
    word_count = word_count + len(lines.split())

print(line_count)
print(word_count)

# *********************************************************************************************

# You are asked to help a Car Rental company keep track of their vehicles.
# For each vehicle they need: plate number, total number of km
# The application will present the following menu:
# 1. Add Vehicle
# 2. View Vehicles
# 0. Exit

file = open('vehicles.txt', 'r')
existing = file.read()

plate = input('Enter the plate number: ')
total = input('Enter the total KM: ')

if f'Plate Number: {plate}, ' in existing:
    print('Error. This plate number already exists and cannot be added again.')
else:
    file = open('vehicles.txt', 'a')
    file.write(f'Plate Number: {plate}, ')
    file.write(f'Total KM: {total}\n')
    print('Vehicle successfully added.')

# *********************************************************************************************

# (a) Write a program to read the file, select a random Sudoku and display it properly.

# Then, (b) ask user to play, giving row, column, and value, and respond if the play is valid or not.


# data = pd.read_csv('sudoku.csv')

# random_sudoku = random.randint(0, len(data) - 1)

# print("Random Sudoku Puzzle:\n", data.iloc[random_sudoku])
# sudoku.csv file was too large to push to github.
