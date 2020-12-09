# Alejandra Castillo 1440370
# This is the first part of my final project
# In theory, this should be able to read any csv file and output either an
# alphabetically sorted, by item id, old to recent, or most expensive to least
# expensive list
import csv

nrow = 0

csv_content = []

class CsvReading:

# Referencing Zylab Ch.9 - this will initiate the use of csv reader
# var name for general input file
# decided to ask for the user to enter a file name
    input_file = input('Please enter a file name:')
# this will read any input file
    with open(input_file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        # now to set some conditions for which the file should be read and outputted
        # specifically, this will be reading each row at a time and then reading each value or column
        # First I'm checking to make sure that the file can be read
        for row in csv_reader:

            # storing the row into the list I've made
            csv_content.append(row)
        # for my understanding of this concept, this essentially takes each value and keeps flipping them until in
        # placed into the right order

        for i in range(len(csv_content)):
            for j in range(i+1 , len(csv_content)):
                if csv_content[i][1] > csv_content[j][1]:
                    csv_content[i], csv_content[j] = csv_content[j], csv_content[i]

print(csv_content)


# defining a class for sorting the file alphabetically
class AlphabetSort:
    # copied what I had before and pasted it into a text file named alpha_sort for ref

# this class will be for sorting csv files by item id and outputting a file
class id_sort:
    # defining a class for now,name will be figured out later
    def id_columns(self, item_id):
        self.item_id = item_id

    id_sorted = sorted(csv_content, key=id_sort())
    print(id_sorted)

# this class will be for sorting items from old to new, so descending order
# note to self: this is also in descending order
class old_to_new:
    # defining something for now just to fill this class
    def service_date_order(self, service_date='December 12, 2020'):
        self.service_date = service_date




# this class will be for sorting damaged items from most expensive to least
# descending order?
class damaged_expenses:
    # defining something for now just to fill in the class
    def item_condition(self, item_cond=''):
        self.item_condition
