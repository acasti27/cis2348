# Alejandra Castillo 1440370
# Fat-burning heart rate
# redefining age - for some reason the name is confusing me so I'll rename it
def get_age():
    age = int(input())
    if age < 18 or age > 75:
        raise ValueError('Invalid age.')
    return age


# defining the fat burning heart rate
def fat_burning_heart_rate(age):
    heart_rate = (220 - age) * 0.7
    return heart_rate


# adding in the main
if __name__ == '__main__':
    try:
        age = get_age()
        print('Fat burning heart rate for a {} year-old: {} bpm'.format(age, fat_burning_heart_rate(age)))
    except ValueError as ve:
        print(ve)
        print('Could not calculate heart rate info.\n')
