# Alejandra Castillo 1440370
# Creating a dictionary for the months
months = {
    'january': 1,
    'february': 2,
    'march': 3,
    'april': 4,
    'may': 5,
    'june': 6,
    'july': 7,
    'august': 8,
    'september': 9,
    'october': 10,
    'november': 11,
    'december': 12
}
# splitting the strings of data inputted
in_file = 'inputDates.txt'
for date in in_file:
    if date != '-1':
        lis = date.split()
        if len(lis) >= 3:
            month = lis[0]
            day = lis[1]
            year = lis[2]
