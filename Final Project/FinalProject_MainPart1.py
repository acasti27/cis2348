# Alejandra Castillo 1440370
# This is the first part of my final project
# In theory, this should be able to read any csv file and output either an
# alphabetically sorted, by item id, old to recent, or most expensive to least
# expensive list
nrow = int(input())
nrow = 0


# defining a class solely for reading the file
class CsvReading:
    import csv
# Referencing Zylab Ch.9 - this will initiate the use of csv reader
# var name for general input file
# decided to ask for the user to enter a file name
    input_file = input('Please enter a file name:')
# Will move around later, but I wanted to include a list of choices to give myself a better idea on how to go about the
# rest of this part
    csv_content = []
# this will read any input file
    with open(input_file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        # now to set some conditions for which the file should be read and outputted
        # specifically, this will be reading each row at a time and then reading each value or column
        # First I'm checking to make sure that the file can be read
        for row in csv_reader:
            print(row)
            # storing the row into the list I've made
            csv_content.append(row)


# letting the file print out for now


# defining a class for sorting the file alphabetically
class AlphabetSort:
    def columns(item_id, manufacturer, item_type, price, manu_date, condition):
        i = 0
        while i < nrow:
            i.item_id = item_id
            i.manufacturer = manufacturer
            i.item_type = item_type
            i.price = price
            i.manu_date = manu_date
            i.condition = condition
