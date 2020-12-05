# Alejandra Castillo 1440370
# This is the second part of my final project

class CReader:

    # importing csv to read the file
    import csv

    csv_content = []
    # prompting the user to input a file name
    input_file = input('Please enter a file name:')
    # letting the file print out for now
    with open(input_file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
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
        if manufacturer and item_type in CReader:
            # this will print out whether or not the specified items are found
            return 'No such item in inventory!'
        else:
            # this is the format to how it should be printing out if it is found within the csv file
            return 'Your item is: {}, {}, {}, {}'.format(self.item_id, self.manufacterer, self.item_type, self.price)
