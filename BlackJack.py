#!/usr/bin/env python
# -*- coding: utf-8 -*-


# BlackJack Game 
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
	# __str__ of "player" class | or "player" title

# Additional features : 
	# setting amount of money 



# --------------------------------------------------------------------------------------------------------

Game = black_jack_classes.Game()




Game.init()
# HERE GAME LOOP 

while not Game.game_end:
	for player in Game.all_players :
		player.get_initial_hand(Game.deck)
		player.make_bet()
	Game.croupier.get_initial_hand(Game.deck)

	# players ought to see first card in croupiers hand before their move

	# players make move
	Game.show_table()

	for player in Game.all_players : 
		for hand in player.list_of_hands :
			player.make_move(Game.deck,hand)
			#player.show_stats()

	#print ("THESE WERE PLAYERSSS ------------------------")
	Game.croupier.make_move(Game.deck, Game.croupier.list_of_hands[0])
	#print("THIS WAS CROUPIER **************************************")

	Game.manage_bets_after_deal()
	Game.clear_hands()
	print("TABLE CLEARED !")
	Game.kick_bancrupt_players()


	if len(Game.deck.cards) < 25:
		Game.deck.new_shuffled_deck()
		print("\n Hey, That's a new DECK ! \n")

	

	# check who wins $$$$$ - probably done 
	# manage money  $$$$   - probebly done 11

	# giving player a steer.
	# asking for player name and using it.  ++++++++++
	# AI for computer. Based on tactics. ++++++++
	# making some functions to write tests easly !!!!!!!
	# Write tests for Game Class !!!!!

if not Game.all_players :
	print("ALL PLAYERS ARE BANCRUPT ! \n GAME OVER ! ")

else : 
	print("The Game has ended")




	

