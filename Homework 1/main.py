# Alejandra Castillo 1440370
print('Enter amount of lemon juice (in cups):')
lemon_juice = float(input())
print('Enter amount of water (in cups):')
water = float(input())
print('Enter amount of agave nectar (in cups):')
agave_nectar = float(input())
print('How many servings does this make?')
serving_size = float(input())

print('\nLemonade ingredients - yields',  '{:.2f}'.format(serving_size),  'servings')
print('{:.2f}'.format(lemon_juice), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(agave_nectar),  'cup(s) agave nectar')

print('\nHow many servings would you like to make?')
serving_needed = float(input())
lemon_juice_one = lemon_juice / serving_size
water_one = water / serving_size
agave_nectar_one = agave_nectar / serving_size
lemon_needed = lemon_juice_one * serving_needed
water_needed = water_one * serving_needed
agave_needed = agave_nectar_one * serving_needed

print('\nLemonade ingredients - yields',  '{:.2f}'.format(serving_needed), 'servings')
print('{:.2f}'.format(lemon_needed), 'cup(s) lemon juice')
print('{:.2f}'.format(water_needed), 'cup(s) water')
print('{:.2f}'.format(agave_needed),  'cup(s) agave nectar')


lemon_juice_gallon = lemon_needed / 16
water_gallon = water_needed / 16
agave_gallon = agave_needed / 16

print('\nLemonade ingredients - yields', '{:.2f}'.format(serving_needed), 'servings')
print('{:.2f}'.format(lemon_juice_gallon), 'gallon(s) lemon juice')
print('{:.2f}'.format(water_gallon), 'gallon(s) water')
print('{:.2f}'.format(agave_gallon), 'gallon(s) agave nectar')
