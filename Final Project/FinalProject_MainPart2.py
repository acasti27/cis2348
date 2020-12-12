# Alejandra Castillo 1440370
# This is the second part of my final project

# this will read all the csv files
import csv
# this is for the group of files to append to
# creating this dictionary to see if I can put the lists inside of it
csv_files = {'manufacturer': [], 'prices': [], 'service_dates': []}
manufacturer = []
prices = []
service_dates = []


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


# printing out each appended list to make sure it's all printing
print(csv_files)
# this is to print the item type and manufacter that the user searched for including id, name, type and
# price
# print('Your item is: ID - {} Manufacturer - {} Item Type - {} Price - {} ').format(self.item_type,
# self.item_manufacturer)

# def askuser():
# this will be asking the user to enter a manufacturer and an item type and taking them as inputs
# manufacturer_input = input('Please enter a manufacturer:\n')
# item_input = input('Please enter an item type:\n ')


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
