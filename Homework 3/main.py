# Alejandra Castillo 1440370
# Online shopping cart (Part 2)

# defining the class for purchasing items
# adding on item description
# rewriting in a different format
class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

# defining item cost formula and print
    def print_item_cost(self):
        cost_output = '{} {} @ ${} = {}'.format(self.item_name, self.item_quantity, self.item_price,
                                                (self.item_quantity * self.item_price))
        return cost_output

# defining item description
# will print out in the order of item name and then description
    def print_item_description(self):
        description_output = '{}: {}, %d oz.'.format(self.item_name, self.print_item_description, self.item_quantity)
        print(description_output)
        return description_output


# defining the shopping cart class
class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    # defining adding an item
    def add_item(self):
        print('ADD ITEM TO CART')
        item_name = input('Enter the item name:\n')
        item_description = input('Enter the item description:\n')
        item_price = int(input('Enter the item price:\n'))
        item_quantity = int(input('Enter the item quantity:\n'))

        self.cart_items.append(ItemToPurchase(item_name, item_price, item_quantity, item_description))

    # defining item removal
    def remove_item(self):
        print('REMOVE ITEM FROM CART')
        remove_item = input('Enter name of item to remove:\n')
        i = 0
        for item in self.cart_items:
            if item.item_name == remove_item:
                del self.cart_items[i]
                flag = True
                break
            else:
                flag = True
                i += 1
        if flag == False:
            print('Item not found in cart. Nothing removed.')

    # defining item modification
    def modify_item(self, item):
        print('CHANGE ITEM QUANTITY')
        name = input('Enter the item name:\n')
        for item in item.cart_items:
            if item.item_name == name:
                quantity = input('Enter the new quantity:\n')
                break
            else:
                print('Item not found in cart. Nothing modified.\n')

    # for returning item quantity
    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity = total_quantity + item.item_quantity
            return total_quantity

    # returning total cost
    def get_cost_of_cart(self):
        total_cost = 0
        cost = 0
        for item in self.cart_items:
            cost = item.item_price * item.item_quantity
            total_cost += cost
        return total_cost

    # for printing the total cost of the cart
    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if total_cost == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            self.output_cart()

    # printing out item descriptions
    def print_descriptions(self):
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.customer_name))
        print('\nItem Descriptions')
        for item in self.cart_items:
            print('{}: {}'.format(item.item_name, item.item_description))


# defining the class to print out the menu of options
# each references to its respective calling
def print_menu(obj):
    menu = ('\nMENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\n'
            "i - Output items' descriptions\no - Output shopping cart\nq - Quit\n")
    option = ''
    while option != 'q':
        print(menu)
        option = input('Choose an option:\n')
        while (option != 'a' and option != 'o' and option != 'i' and option != 'r'
                and option != 'c' and option != 'q'):
            option = input('Choose an option:\n')
            if option == 'a':
                obj.add_item()
            elif option == 'o':
                obj.output_cart()
            elif option == 'i':
                obj.print_descriptions()
            elif option == 'r':
                obj.remove_item()
            elif option == 'c':
                obj.modify_items()


# redefining the main code
# adding in printing format
if __name__ == '__main__':
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print('\nCustomer name:', customer_name, end='\n')
    print("Today's date:", current_date, end='\n')
    new_cart = ShoppingCart(customer_name, current_date)
    print_menu(new_cart)
