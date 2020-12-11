# Alejandra Castillo 1440370
# This is the second part of my final project

# this will read all the csv files
import csv
# this is for the group of files to append to
csv_files = []
manufacturer = []
prices = []
service_dates = []


# this class will be for reading the files
class CSVReader:
    # prompting the user to input a file name in an order
    print('When entering a group of files to work with, please enter in the following order:\n '
          'Manufacturer, Price List, and Service Date List using the following format:\n'
          ' "file_name.csv"')
    # prompting user to input three file names
    input_file = input('Please enter a file name:\n')
    file_two = input('Please enter a second file name:\n')
    file_three = input('Please enter a third file name:\n')
    # opening each input and making sure that they append into separate places
    with open(input_file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            manufacturer.append(row)

    with open(file_two, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            prices.append(row)

    with open(file_three, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            service_dates.append(row)


# printing out each appended list to make sure it's all printing
print(manufacturer)
print(prices)
print(service_dates)
