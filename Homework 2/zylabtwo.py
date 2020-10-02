# Alejandra Castillo 1440370
# brute force equation solver
# declaring the variables
a = int(input())
b = int(input())
c = int(input())
u = int(input())
w = int(input())
z = int(input())
# declaration if no solution is found
found_solution = False
# implementing the brute force approach
for x in range(-10, 11):
    for y in range(-10, 11):
        if a * x + b * y == c and u * x + w * y == z:
            print(x, y)
            found_solution = True
# alternative solution if none is found
if not found_solution:
    print('No solution')
