# Alejandra Castillo 1440370
# Online shopping cart (Part 1)

class ItemToPurchase:
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        print(self.item_name, '', str(self.item_quantity), '@$', str(self.item_price), '=$', str(self.item_price
              * self.item_quantity))
