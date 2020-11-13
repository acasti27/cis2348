# Alejandra Castillo 1440370
# This is the first part of my final project
# In theory, this should be able to read any csv file and output either
# alphabetically sorted, by item id, old to recent, or most expensive to least
# expensive
#
# Referencing Zylab - this will initiate the use of csv readers
import csv
# var name for general input file
input_file = input()
# this will read any input file
with open(input_file, 'File') as csvfile:
    csv_reader = csv.reader(csvfile)
