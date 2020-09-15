# Alejandra Castillo 1440370
import math
paint = {
    'red': 35,
    'blue': 25,
    'green': 23
}
print('Enter wall height (feet):')
wall_height = int(input())
print('Enter wall width (feet):')
wall_width = int(input())
wall_area = wall_height * wall_width
print('Wall area:', wall_area, 'square feet')

# one_gallon = 350
paint_needed = wall_area / 350
print('Paint needed:', '{:.2f}'.format(paint_needed), 'gallons')

paint_cans = math.ceil(paint_needed)
print('Cans needed:', '{:.2f}'.format(paint_cans), 'can(s)')

print('\nChoose a color to paint the wall:')
paint_color = input()
if paint_color in paint:
    price = paint[paint_color]
    total = int(price) * paint_cans
    print('Cost of purchasing', paint_color, 'paint: $', '{:.2f}'.format(total))
