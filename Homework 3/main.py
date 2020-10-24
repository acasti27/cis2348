# Alejandra Castillo 1440370
# Online shopping cart (Part 2)

# defining the class for purchasing items
class ItemToPurchase:
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0.0
        self.item_quantity = 0
        self.item_description = 'none'

    def print_tem_description(self):
        print('%s %d @ $%d = $%d' % (self.item_name, self.item_quantity, self.item_price,
                                     (self.item_price * self.item_quantity)))


# defining another class for the shopping cart
class ShoppingCart:
    def __init__(self):
        self.customer_name = 'none'
        self.current_date = 'January 1,2016'
        self.cart_items = []

# this will ask the user to enter two items amd their prices and quantities
if __name__ == '__main__':
    print('Item 1')
    item_one = ItemToPurchase()
    item_one.item_name = input('Enter the item name:\n')
    item_one.item_price = int(input('Enter the item price:\n'))
    item_one.item_quantity = int(input('Enter the item quantity:\n'))

    print('\nItem 2')
    item_two = ItemToPurchase()
    item_two.item_name = input('Enter the item name:\n')
    item_two.item_price = int(input('Enter the item price:\n'))
    item_two.item_quantity = int(input('Enter the item quantity:\n'))

# This is the equation for the total cost as well as individual costs
    total_cost = item_one.item_price * item_one.item_quantity + item_two.item_price * item_two.item_quantity
    total_cost1 = item_one.item_price * item_one.item_quantity
    total_cost2 = item_two.item_price * item_two.item_quantity

# formatting for the display of information
    print('\nTOTAL COST')
    print('{} {} @ ${} = ${}'.format(item_one.item_name, item_one.item_quantity, item_one.item_price, total_cost1))
    print('{} {} @ ${} = ${}'.format(item_two.item_name, item_two.item_quantity, item_two.item_price, total_cost2))

    print('\nTotal: $' + str(total_cost))
