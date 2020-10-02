# Alejandra Castillo 1440370
# password modifier
# prompts an input from user
simple_password = input()
password = ''
# for if and else if statements to switch around letters
for a in simple_password:
    if a == 'i':
        password += '!'
    elif a == 'a':
        password += '@'
    elif a == 'm':
        password += 'M'
    elif a == 'B':
        password += '8'
    elif a == 'o':
        password += '.'
    else:
        password += a
# appends to the end of the string and prints the new code
password += 'q*s'
print(password)
