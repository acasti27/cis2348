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


# defining the shopping cart class
class ShoppingCart:
    def __init__(self):
        self.customer_name = 'none'
        self.current_date = 'January 1,2016'
        self.cart_items = []

    # defining adding an item
    def add_item(self):
        self.cart_items.append(ItemToPurchase)

    # defining item removal
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
            else:
                print('Item not found in cart. Nothing removed.')

    # defining item modification
    def modify_item(self, item):
        for item in self.cart_items:
            if item.item_name == ItemToPurchase.item_name:
                new_quantity = int(input('Enter the new quantity:'))
            else:
                print('Item not found in cart. Nothing modified.')

    # for returning item quantity
    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity = total_quantity + item.item_quantity
            return total_quantity

    # returning total cost
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost = (item.item_price * item.item_quantity)
        return total_cost

    # for printing the total cost of the cart
    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if total_cost == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
            print('Number of items: %d' % self.get_num_items_in_cart())
            for item in self.cart_items:
                total = item.item_price * item.item_quantity
                print('%s %d @  $%d = $%d' % (item.item_name, item.item_quantity, item.item_price, total))
            print('Total: $%d' % total_cost)

    # printing out item descriptions
    def print_descriptions(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.customer_name))
        print('\nItem Descriptions')
        for item in self.cart_items:
            item.print_item_description()


# defining the class to print out the menu of options
def print_menu():

