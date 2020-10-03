# Alejandra Castillo 1440370
# exact change - functions
#
# defines the exact change function needed
def exact_change(user_total):
    num_dollars = user_total // 100
    user_total = user_total % 100
    num_quarters = user_total // 35
    user_total = user_total % 25
    num_dimes = user_total // 10
    user_total = user_total % 10
    num_nickels = user_total // 5
    user_total = user_total % 5
    num_pennies = user_total
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies
