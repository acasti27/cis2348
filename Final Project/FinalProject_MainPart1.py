# Alejandra Castillo 1440370
# This is the first part of my final project
# In theory, this should be able to read any csv file and output either an
# alphabetically sorted, by item id, old to recent, or most expensive to least
# expensive list
import csv
from datetime import *
nrow = 0

# these are where the lists will append to
csv_content = []
content_two = []
content_three = []
content_four = []


# this class sorts the files alphabetically
class CsvReading:

    # Referencing Zylab Ch.9 - this will initiate the use of csv reader
    # var name for general input file
    # decided to ask for the user to enter a file name
    input_file = input('Please enter a file name to sort alphabetically:\n')
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
    input_file_two = input('\nPlease enter a file name to sort by item id:\n')
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


# this for part c, I will be defining a class that will sort the dates from oldest to newest
class OldNew:
    # asking for a third input
    input_file_three = input('\nPlease enter a file name to sort from oldest to newest:\n')
    # using the csv reader to open the input file
    with open(input_file_three, 'r') as cfile:
        the_reader = csv.reader(cfile, delimiter=',')
        # appending this elsewhere so it continues to read each file listed differently
        for row in the_reader:
            content_three.append(row)
        for i in range(len(content_three)):
            for j in range(i+1, len(content_three)):
                # trying a different approach to get it to read dates from oldest to newest
                # ideally these will be looking at each date and not only taking the year into account, but the
                # date as a whole so that it can sort it better
                m1, d1, y1 = [x for x in content_three[i][4].split('/')]
                d1 = int(d1)
                m1 = int(m1)
                y1 = int(y1)
                b1 = date(y1, m1, d1)
                m2, d2, y2 = [x for x in content_three[i][4].split('/')]
                d2 = int(d2)
                m2 = int(m2)
                y2 = int(y2)
                b2 = date(y2, m2, d2)
                if b1 > b2:
                    content_three[i], content_three[j] = content_three[j], content_three[i]
                    print('Switch made.')
                else:
                    continue


print(content_three)


# this is for part d, I will be defining a class that will sort the prices for most expensive to least expensive
class Price:
    # asking for a fourth input
    input_four = input('\nPlease enter a file name to sort from most expensive to least expensive:\n')
    # using the csv reader to open the file
    with open(input_four, 'r') as file:
        read = csv.reader(file, delimiter=',')
        # appending elsewhere so it doesn't read with the other files
        for row in read:
            content_four.append(row)
        for i in range(len(content_four)):
            for j in range(len(content_four)):
                if content_four[i][3] < content_four[j][3]:
                    content_four[i], content_four[j] = content_four[j], content_four[i]


print(content_four)
