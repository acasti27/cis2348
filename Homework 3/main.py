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
    jersey_num = int(input("Enter player %d's jersey number:\n" % (i+1)))
    players[jersey_num] = int(input("Enter player %d's rating:\n" % (i+1)))
    print('')
keys = list(players.keys())
keys.sort()
print('ROSTER')
for key in keys:
    print('Jersey number: %d, Rating: %d' % (key, players[key]))
# prints out a menu with quitting being the only working option to select
# added option o as a working option
# added a as a working option
# added d as a working option
# added u as a working option
while True:
    print('\nMENU\na - Add player\nd - Remove player\nu - Update player rating'
          '\nr - Output players above a rating\no - Output roster\nq - Quit')
    option = input('\nChoose an option:\n')
    if option == 'o':
        print_roster()
    elif option == 'a':
        jersey_num = int(input("Enter a new player's jersey number:\n"))
        rating = int(input("Enter the player's rating:\n"))
        players[jersey_num] = rating
    elif option == 'd':
        jersey_num = int(input("Enter a player's jersey number:\n"))
        if jersey_num in list(players.keys()):
            del players[jersey_num]
    elif option == 'u':
        jersey_num = int(input("Enter a player's jersey number:\n"))
        rating = int(input('Enter a new rating for player:\n)'))
        players[jersey_num] = rating
    elif option == 'r':
        rating = int(input('Enter a rating:\n'))
        keys = list(players.keys())
        keys.sort()
        print('\nABOVE %d' % rating)
        count = 0
        for key in keys:
            if players[key] > rating:
                print("Jersey number: %d, Rating: %d" % (key, players[key]))
                count += 1
        if count == 0:
            print('No players found above %d rating' % rating)
    if option == 'q':
        break
