# Alejandra Castillo 1440370
# word frequencies
# used in order to read the file
import csv
input_file = input()
frequency = {}
# opens the file
with open(input_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
# creating a loop with conditions
    for line in csvreader:
        for word in line:
            # assigning value if not found or countd existing
            if word not in frequency.keys():
                frequency[word] = 1
            else:
                frequency[word] += 1
# printing the output with correct spacing
for key in frequency.keys():
    print(key + '', str(frequency[key]))
