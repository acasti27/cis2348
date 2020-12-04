# Alejandra Castillo 1440370
# This is the second part of my final project
# importing csv to read the file
import csv
# prompting the user to input a file name
input_file = input('Please enter a file name:')
# letting the file print out for now
with open(input_file, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(row)

# prompting the user to enter a manufacturer and an item type
input_one = input('Please enter a manufacturer:')
input_two = input('Please enter an item type:')

# if manufacturer and item not in inventory:
#    print('No such item in inventory')
