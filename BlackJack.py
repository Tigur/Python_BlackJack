#BlackJack Game 
# By Nikodem Celiński 

# file created : 12:50 | 18.09.18 


import black_jack_classes

"""
This code represents logic of the Game.

"""
# -------------------------------------------------------------------------------------------------------

# INIT : 
	# deck
	# players
	# croupier

# GAME LOOP :
	# round begining
	# each player does a move (after each check if busted)
	# croupier does a move (check if busted)
	# declare wins/loses and manage money
	# Check if it's over for every player, If not - >>NEXT ROUND (LOOP)<<


# TO DO LIST : 
	# INIT 1 2 3 
	# GAME LOOP 1 2 3 4 5 

# Additional features : 
	# setting amount of money 



# --------------------------------------------------------------------------------------------------------

game_end = False
players_number = raw_input("How many players will play ?")
players_list = []

for player in range(players_number):
	players_list.append(black_jack_classes.Player())

croupier = black_jack_classes.GameParticipant()
deck = black_jack_classes.Deck()
# HERE GAME LOOP 

while not game_end:
	for player in players_list :
		player.get_initial_hand(deck)
	croupier.get_initial_hand(deck)

	# players ought to see first card in croupiers hand before their move

	# players make move

	for player in players_list : 
		for hand in player.list_of_hands :
			player.make_move(hand,deck)


	

