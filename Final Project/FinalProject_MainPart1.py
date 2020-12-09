# Alejandra Castillo 1440370
# This is the first part of my final project
# In theory, this should be able to read any csv file and output either an
# alphabetically sorted, by item id, old to recent, or most expensive to least
# expensive list
import csv

nrow = 0

# these are where the lists will append to
csv_content = []
content_two = []


# this class sorts the files alphabetically
class CsvReading:

    # Referencing Zylab Ch.9 - this will initiate the use of csv reader
    # var name for general input file
    # decided to ask for the user to enter a file name
    input_file = input('Please enter a file name to sort alphabetically:')
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
            for j in range(i+1, len(csv_content)):
                if csv_content[i][1] > csv_content[j][1]:
                    csv_content[i], csv_content[j] = csv_content[j], csv_content[i]


print(csv_content)


# copied what I had before and pasted it into a text file named alpha_sort for ref in case I change my mind
#
# defining a class for sorting the file by damage and id
class IdSort:
    # asking for a second input so it can be sorted
    input_file_two = input('Please enter a file name to sort by item id:')
    # recreating what I need to open the selected file in order to work with it
    with open(input_file_two, 'r') as csfile:
        file_reader = csv.reader(csfile, delimiter=',')
        # these will append to another list
        for row in file_reader:
            content_two.append(row)
        # this time I'm taking the first value which is 0 to put the item id's in order
        for i in range(len(content_two)):
            for j in range(i+1, len(content_two)):
                if content_two[i][0] > content_two[j][0]:
                    content_two[i], content_two[j] = content_two[j], content_two[i]


print(content_two)
