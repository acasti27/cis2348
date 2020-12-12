# Alejandra Castillo 1440370
# This is the second part of my final project

# this will read all the csv files
import csv
# this is for the group of files to append to
# this dictionary has each list inside of it
csv_files = {'manufacturer': [], 'prices': [], 'service_dates': []}
name_list = []
user_input = []
item_id = []
items = False
manu = False
types = []
brand = []


# this class will be for reading the files
class CSVReader:
    # prompting the user to input a file name in an order
    print('When entering a group of files to work with, please enter in the following order:\n '
          'Manufacturer, Price List, and Service Date List using the following format:\n'
          ' "file_name.csv"')
    # prompting user to input three file names
    input_file = input('Please enter a file name:\n')
    file_two = input('Please enter a second file name:\n')
    file_three = input('Please enter a third file name:\n')
    # opening each input and making sure that they append into separate places
    with open(input_file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            csv_files['manufacturer'].append(row)

    with open(file_two, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            csv_files['prices'].append(row)

    with open(file_three, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            csv_files['service_dates'].append(row)


# this prints out the dictionary
print(csv_files)

# prompting the user to enter a manufacturer name and item type
user_input = input('Please enter manufacturer and item type:\n')
# this will spilit that input into to separate variables
user_input = user_input.split()
print(user_input)
# taking those two and searching for them within the manufacturer list in the dictionary
for i in range(len(user_input)):
    if 'manufacturer'[i][1] in user_input:
        manu = True
    if 'manufacturer'[i][2] in user_input:
        items = True

if manu is True and items is True:
    for i in range(len(user_input)):
        if 'manufacturer'[i][1] in user_input and 'manufacturer'[i][2] in user_input:
            print('manufacturer'[i])
            if 'manufacturer'[i][3] == 'damaged':
                print('This item item is damaged.')
            else:
                item_id.append('manufacturer[1][0]')
else:
    print('This item is not in our inventory.\n')

while True:
    # this will ask the user to search again or quit
    print('\nWould you like to search for something else?\ny - yes\nq - quit')
    option = input('Please select an option:\n')
    # this will prompt the user to search for something else again
    if option == 'y':
        print(CSVReader)
    # this will quit the program
    if option == 'q':
        break
