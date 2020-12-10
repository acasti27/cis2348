# Alejandra Castillo 1440370
# This is the second part of my final project
# need to figure out how to get this to read three files
# this will read all the csv files
import csv
# this is for the group of files
csv_files = []

# this class will be for reading the files
class CSVReader:
    # importing csv to read the file
    # prompting the user to input a file name
    input_file = input('Please enter a file name:\n')
    # letting the file print out for now
    with open(input_file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            print(row)

# defining to check inventory
    def check_inventory(self, manufacturer, item_type, price, item_id):
        self.manufacter = manufacturer
        self.item_type = item_type
        self.price = price
        self.item_id = item_id
        # prompting the user to enter a manufacturer and an item type
        input_one = input('Please enter a manufacturer:')
        input_two = input('Please enter an item type:')
        if manufacturer and item_type not in CSVReader:
            # this will print out whether or not the specified items are found
            return 'No such item in inventory!'
        else:
            # this is the format to how it should be printing out if it is found within the csv file
            print('Your item is: {}, {}, {}, {}').format(self.item_id, self.manufacterer, self.item_type, self.price)
            print('You may, also, consider: {} {}, {}, {}').format(self.item_id, self.manufacter, self.item_type, self.price)

    # trying to loop back as a simple menu
    def print_question(self):
        print('\nWould you like to search for something else?\ny - Yes\nn - no (quit)')
        option = input('\nPlease select an option:\n')
        if option == 'y':
            print(check_inventory)
        if option == 'n':
