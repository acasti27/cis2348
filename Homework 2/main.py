# Alejandra Castillo 1440270
# palindrome
# basic declaration for any given input
string = input()
begin = 0
end = len(string)-1
result = True
# while loop and if,else if,else statements in order to declare the conditions in which a word is a palindrome
while begin < end:
    if string[begin] == '':
        begin += 1
    elif string[end] == '':
        end -= 1
    elif string[begin] != string[end]:
        result = False
        break
# putting a break at the end to stop the loop in order to keep the code from printing out multiples
    else:
        begin += 1
        end -= 1
        if result:
            print(string, 'is a palindrome')
        else:
            print(string, 'is not a palindrome')
        break
