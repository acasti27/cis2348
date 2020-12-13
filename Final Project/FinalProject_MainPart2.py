# Alejandra Castillo 1440370
# This is the second part of my final project
# this will read all the csv files
import csv
# this is for the group of files to append to
csv_files = []
manufacturer = []
prices = []
service_dates = []
name_list = []
item_type = []
usr_input = []
item_id = []
items = False
manu = False
isDamaged = False
loop = True
types = []
brand = []

while loop:

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
            csv_files.append(row)

    with open(file_two, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            prices.append(row)
            csv_files.append(row)

    with open(file_three, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            service_dates.append(row)
            csv_files.append(row)


        # printing out each appended list to make sure it's all printing
        print(manufacturer)
        print(prices)
        print(service_dates)
        # this prints out the dictionary
        print(csv_files)

        # prompting the user to enter a manufacturer name and item type
        user_input = input('Please enter manufacturer and item type:\n')
        # this will split that input into to separate variables
        user_input = user_input.split()
        print(user_input)
        # taking those two and searching for them within the manufacturer list in the dictionary
        for i in range(len(user_input)):
            if manufacturer[i][1] in user_input:
                manu = True
            if manufacturer[i][2] in user_input:
                items = True
         # this is to check whether or not the item is damaged, I opted to display a message in place in case it is
        if manu == True and items == True:
            for i in range(len(manufacturer)):
                if manufacturer[i][1] in user_input and manufacturer[i][2] in user_input:
                    if manufacturer[i][3] == 'damaged':
                        isDamaged = True
                        print("This item is damaged. \n")
                        break
            # if the item is not damaged, then the idea is to store the information into the list
            else:
                item_id.append(manufacturer[i][0])
                brand.append(manufacturer[i][1])
                types.append(manufacturer[i][2])
                print('items have been copied\n')
        else:
            print('This item is not in our inventory.\n')

        if isDamaged == False:
            for i in range(len(manufacturer)):
                # finds info of item
                    if manufacturer[i][0] in item_id:
                         print(manufacturer[i])
    # finds price of item
                    if prices[i][0] in item_id:
                        print('prices'[i])



    # this will ask the user to search again or quit
    print('\nWould you like to search for something else?\ny - yes\nq - quit')
    option = input('Please select an option:\n')
    # this will prompt the user to search for something else again
    if option == 'y':
        csv_files = []
        manufacturer = []
        prices = []
        service_dates = []
        name_list = []
        item_type = []
        usr_input = []
        item_id = []
        items = False
        manu = False
        isDamaged = False
        loop = True
        types = []
        brand = []
    elif option == 'q':
        loop is False
        break
    else:
        print('That is not an option. Goodbye.')
        break
