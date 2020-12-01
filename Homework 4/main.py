# Alejandra Castillo 1440370
# Fat-burning heart rate
# defining the fat burning heart rate
def fat_burning_heart_rate():
    heart_rate = (70/100 * 220) - adult_age
    # might be incorrect way to write in formula


# defining age input
def age():
    adult_age = int(input())
# if else statement for what to do if the age is within parameters
    if age >= 18 and <= 75:
        print(adult_age)
    # inluding the value error
    else:
        raise ValueError('Invalid age.')
