# Alejandra Castillo 1440370
# password modifier

simple_password = input()
password = ''
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

password += 'q*s'
print(password)
