# Alejandra Castillo 1440370
# Online shopping cart (Part 2)

# defining the class for purchasing items
# adding on item description
class ItemToPurchase:
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0.0
        self.item_quantity = 0
        self.item_description = 'none'

# defining item cost formula and print
    def print_item_cost(self):
        print(self.item_name + '' + str(self.item_quantity) + '@ $' + str(self.item_price) + '= $' +
              str(self.item_quantity * self.item_price))

# defining item description
# will print out in the order of item name and then description
    def print_item_description(self):
        print(self.item_name + ':' + self.item_description)
