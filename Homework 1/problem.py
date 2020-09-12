# Alejandra Castillo 1440370
# This a calculator for birthdays
print('Birthday Calculator')
current_mon = input('Enter the current month:')
current_day = input('Enter current day:')
current_year = input('Enter current year:')

birth_mon = input('Enter birth month:')
birth_day = input('Enter birth day:')
birth_year = input('Enter birth year:')

current_age = int(current_year) - int(birth_year)

print()
print('Birthday Calculator')
print('Current Month:', current_mon)
print('Current Day:', current_day)
print('Current Year:', current_year)
print('Birthday Month:', birth_mon)
print('Birthday Day:', birth_day)
print('Birthday Year', birth_year)
print('You are', current_age, 'years old.')
if current_mon == birth_mon:
    if current_day == birth_day:
        print('Happy Birthday!')
