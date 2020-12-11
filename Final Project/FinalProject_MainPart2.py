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
    # importing csv to read the file
    # prompting the user to input a file name
    print('When entering group of files, please enter in the following order: '
          'Manufacturer, Service Date, Price List')
    input_file = input('Please enter a file name:\n')
    file_two = input('Please enter a second file name:\n')
    file_three = input('Please enter a third file name:\n')
    # letting the file print out for now
    with open(input_file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            print(row)
            print()

    with open(file_two, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            print(row)
            print()

    with open(file_three, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            print(row)
            print()
