# Alejandra Castillo 1440370
# Creating a dictionary for the months
months_list = {
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
in_file = open('C:\\User\\Desktop\\inputDates.txt')
for date in in_file:
    if date != '-1':
        lis = date.split()
        if len(lis) >= 3:
            month = lis[0]
            day = lis[1]
            year = lis[2]
# formatting
            if month.lower() in months_list:
                comma = day[-1]
                day = day[:len(day)-1]
                month_number = months_list(month.lower())
                ans = month_number+'/'+day+'/'+year
                print(ans)

