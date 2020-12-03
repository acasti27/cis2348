# Alejandra Castillo 1440370
# This is the first part of my final project
# In theory, this should be able to read any csv file and output either an
# alphabetically sorted, by item id, old to recent, or most expensive to least
# expensive list
#
# Referencing Zylab Ch.9 - this will initiate the use of csv readers
import csv
# var name for general input file
# decided to ask for the user to enter a file name
input_file = input('Please enter a file name:')
# Will move around later, but I wanted to include a list of choices to give myself a better idea on how to go about the
# rest of this part
print('\nMenu\na - Sort alphabetically\ns - Sort by item id\no - Sort by oldest to newest\ne - Sort by most expensive'
      'to least\nq = Quit')

# this will read any input file
with open(input_file, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
# now to set some conditions for which the file should be read and outputted
    # specifically, this will be reading each row at a time and then reading each value or column
    # First I'm checking to make sure that the file can be read
#    for row in csv_reader:
#        print(row)
