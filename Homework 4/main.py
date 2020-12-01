# Alejandra Castillo 1440370
# Fat-burning heart rate
# defining the fat burning heart rate
def fat_burning_heart_rate(age):
    heart_rate = (70 / 100 * 220) - adult_age
    # adding age input into def
    adult_age = int(input())
    if adult_age < 18 or > 75 :
        raise ValueError('Invalid age.')
