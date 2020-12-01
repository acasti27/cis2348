# Alejandra Castillo 1440370
# This is the first part of my final project
# In theory, this should be able to read any csv file and output either an
# alphabetically sorted, by item id, old to recent, or most expensive to least
# expensive list
#
# Referencing Zylab Ch.9 - this will initiate the use of csv readers
import csv
# var name for general input file
input_file = input()
# this will read any input file
with open(input_file, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
# now to set some conditions for which the file should be read and outputted
    # specifically, this will be reading each row at a time and then reading each value or column
    # First I'm checking to make sure that the file can be read
    for row in csv_reader:
        if row == '':
            print('')
