# Alejandra Castillo 1440370
# Creating a dictionary for the months
months_list = {
    'january': '1',
    'february': '2',
    'march': '3',
    'april': '4',
    'may': '5',
    'june': '6',
    'july': '7',
    'august': '8',
    'september': '9',
    'october': '10',
    'november': '11',
    'december': '12'
}
# opens files
in_file = open('C:\\Users\\Desktop\\inputDates.txt')
out_file = open('C:\\Users\\Desktop\\parsedDates.txt')
# splitting the strings of data inputted
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
                month_number = months_list[month.lower()]
                ans = month_number+'/'+day+'/'+year
                print(ans)
                out_file.write(ans)
                out_file.write('\n')
# closes file
out_file.close()
in_file.close()
