# Alejandra Castillo 1440370
# Exception handling to detect input string vs. integer
# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    # FIXME: The following line will throw ValueError exception.
    #        Insert try/except blocks to catch the exception.
    # added try and exception
    try:
        age = int(parts[1]) + 1

    except Exception as exe:
        age = 0
    print('{} {}'.format(name, age))

    # Get next line
    parts = input().split()
    name = parts[0]
