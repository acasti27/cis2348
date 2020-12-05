# Alejandra Castillo 1440370
# This is the first part of my final project
# In theory, this should be able to read any csv file and output either an
# alphabetically sorted, by item id, old to recent, or most expensive to least
# expensive list
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


# defining a class for sorting the file alphabetically
class AlphabetSort:
    # defining my column names
    def columns(self, item_id, manufacturer, item_type, price, manu_date, condition='none'):
        self.item_id = item_id
        self.manufacterer = manufacturer
        self.item_type = item_type
        self.price = price
        self.manu_date = manu_date
        self.condition = condition

    # defining a sorting format
    def column_sort(self):
        return '({}, {}, {}, ${}, {}, {}'.format(self.item_id, self.manufacterer, self.item_type,
                                                 self.price, self.manu_date, self.condition)

    # hoping that this will print out everything alphabetically
    def manufacturer_sort(manu):
        return manu.manufacturer
    # since sorted can give me an output which is pretty much alphabetical, I decided to go with that approach
    alpha_manu = sorted(csv_content, key=manufacturer_sort())

    print(alpha_manu)
