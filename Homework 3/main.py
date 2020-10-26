# Alejandra Castillo 1440370
# Soccer team roster (Dictionaries)

# dictionary for players
players = {}
# prompts the user to enter up to five jersey numbers and ratings
for i in range(5):
    jersey_num = int(input("Enter player %d's jersey number: \n" % (i+1)))
    players[jersey_num] = int(input("Enter player %d's rating: \n" % (i+1)))
    print('')

keys = list(players.keys())
keys.sort()
# prints out the roster sorted
print('ROSTER')
for key in keys:
    print('Jersey number: %d, Rating: %d' % (key, players[key]))
