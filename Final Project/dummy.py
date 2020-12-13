#
#
#
import csv
# this is for the group of files to append to
csv_files = []
manufacturer = []
prices = []
service_dates = []
name_list = []
item_type = []
usr_inpt = []
item_Id = []
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
        #takes user input and stores it into a list
        usr_in = input("Please enter manufacturer and item type\n")

        usr_inpt = usr_in.split()
        print(usr_inpt)

        #checks if both manufacturer and item type exist in inventory
        for i in range(len(manufacturer)):
            if manufacturer[i][1] in usr_inpt:
                manu = True
            if manufacturer[i][2] in usr_inpt:
                items = True
        #if both exist then check if item is damaged else store item id
        if manu == True and items == True:
            for i in range(len(manufacturer)):
                #finds item that has both brand and item type input from user
                if manufacturer[i][1] in usr_inpt and manufacturer[i][2] in usr_inpt:
                    #checks if this item is damaged and breaks
                    if manufacturer[i][3] == "damaged":
                        isDamaged = True
                        print("This item is damaged. \n")
                        break
                    #if item is not damaged then store id, brand and item type
                    else:
                        item_Id.append(manufacturer[i][0])
                        brand.append(manufacturer[i][1])
                        types.append(manufacturer[i][2])
                        print(" items have been copied \n")
        #if even one of the requirements is not met then we print out item not in inventory
        else:
            print("This item is not in our inventory. \n")
        #if item is not damaged then find both information and price of item using id
        if isDamaged == False:
            for i in range(len(manufacturer)):
                #finds info of item
                if manufacturer[i][0] in item_Id:
                    print(manufacturer[i])
                #finds price of item
                if prices[i][0] in item_Id:
                    print(prices[i])






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
        usr_inpt = []
        item_Id = []
        items = False
        manu = False
        isDamaged = False
        loop = True
        types = []
        brand = []
    # this will quit the program
    elif option == 'q':
        loop is False
        break
    else:
        print("That is not a option. Goodbye \n")
        break
