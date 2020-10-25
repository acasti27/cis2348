# Alejandra Castillo 14402370
# Filter and sort a list

# input splitting
input_list = [int(i) for i in input().split() if int(i) >= 0]

# applies the sorting function to the list
input_list.sort()
# for printing out with their respective spaces
for number in input_list:
    print(number, end=" ")
