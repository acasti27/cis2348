# Alejandra Castillo 1440370
# Word frequencies
# prompts the user for input
word = input()
# splits the inputs
word = word.split(" ")

dictionary = {}
# setting the conditions for repeated words and then prints them
for each in word:
    if each in dictionary:
        dictionary[each] = dictionary[each] + 1
    else:
        dictionary[each] = 1
for each in word:
    print(each, dictionary[each])
