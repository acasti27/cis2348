# Alejandra Castillo 1440370
# Fat-burning heart rate
# defining the fat burning heart rate
def fat_burning_heart_rate(age):
    # adding age input into def
    adult_age = int(input())
    heart_rate = (70 / 100 * 220) - adult_age
    # this will set the parameter for the value error
    if adult_age < 18 or adult_age > 75:
        raise ValueError('Invalid age.')
    return heart_rate, adult_age

# adding in the main
if __name__ == '__main__':
