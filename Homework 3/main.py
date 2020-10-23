# Alejandra Castillo 1440370
# Online shopping cart (Part 1)
# defining the class for purchasing items
class ItemToPurchase:
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0.0
        self.item_quantity = 0

# for item costs
    def print_item_cost(self):
        print(self.item_name + '' + str(self.item_quantity) + '@$' + str(self.item_price) + '=$' + str(self.item_price
              * self.item_quantity))


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

# This is the equation for the total cost
    total_cost = item_one.item_price * item_one.item_quantity + item_two.item_price * item_two.item_quantity

    print('TOTAL COST')
    item_one.print_item_cost()
    item_two.print_item_cost()

    print('Total: $' + str(total_cost))
