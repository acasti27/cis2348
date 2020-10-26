# Alejandra Castillo 1440370
# Soccer team roster (Dictionaries)

# rearranged the keys to define the roster
def print_roster():
    keys = list(players.keys())
    keys.sort()
    # prints out the roster sorted
    print('ROSTER')
    for key in keys:
        print('Jersey number: %d, Rating: %d' % (key, players[key]))


# dictionary for players
players = {}
# prompts the user to enter up to five jersey numbers and ratings
for i in range(5):
    jersey_num = int(input("Enter player %d's jersey number: \n" % (i+1)))
    players[jersey_num] = int(input("Enter player %d's rating: \n" % (i+1)))
    print('')


# prints out a menu with quitting being the only working option to select
# added option o as a working option
# added a as a working option
while True:
    print('\n MENU \n a - Add player \n d - Remove player \n u - Update player rating'
          '\n r - Output players above a rating \n o - Output roster \n q - Quit')
    option = input('\n Choose an option:')
    if option == 'o':
        print_roster()
    elif option == 'a':
        jersey_num = int(input("Enter a new player's jersey number: \n"))
        rating = int(input("Enter the player's rating: \n"))
        players[jersey_num] = rating
    if option == 'q':
        break
