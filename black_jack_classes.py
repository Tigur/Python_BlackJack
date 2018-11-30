#!/usr/bin/env python
# -*- coding: utf-8 -*-

#BlackJack Game : CLASSES
#By Nikodem Celiński 

#file created : 14:00 | 18.09.18 


import random
from bj_exceptions import MovementFail 

class Deck():



	def __init__(self):
		self.possible_figures = [2,3,4,5,6,7,8,9,10,'J','D','K','A']
		self.cards = self.possible_figures*4


	def shuffle(self):
		random.shuffle(self.cards)

	def pop_top_card(self):
		"""
		INPUT: none
		OUTPUT: first card in deck

		Function deletes returned card from deck.
		"""

		#print(str(self.cards) + "\n KARTY \n")

		top_card = self.cards[0]
		print("NEW CARD : " + str(top_card))
		self.cards.pop(0)
		return top_card

	def new_shuffled_deck():
		self.cards = possible_figures*4
		self.shuffle()


class Hand():
	"""
	Class represents a participant's hand. 

	hand - a list of cards
	
	"""

	def __init__(self):
		self.cards = []

		self.points_hi = 0
		self.points_lo = 0
		self.preferable_points = 0
		self.is_busted = False
		self.hi_busted = False
		self.bet = 0
		self.hit_limit_on = False

	def __str__(self):

		cards_str = str(self.cards)
		pointsHi_str = str(self.points_hi)
		pointsLo_str = str(self.points_lo)
		is_busted_str = str(self.is_busted)
		bet_str = str(self.bet)
		hit_limit_str = str(self.hit_limit_on)

		print("CARDS : " + cards_str)
		print("POINTS (high/low) : " + pointsHi_str +'/'+ pointsLo_str)
		print("IS_BUSTED :" + is_busted_str)
		print("BET : " + bet_str)
		print("HIT_LIMIT : " + hit_limit_str)

		return ''

	def update_points_stats(self):
		points_sum_hi = 0
		points_sum_lo = 0
		for card in self.cards : 
			if isinstance(card, int):
				points_sum_hi += card 
				points_sum_lo += card 
			elif card == 'A' :
				points_sum_lo += 1
				points_sum_hi += 11
			else : 
				points_sum_hi += 10
				points_sum_lo += 10

		self.points_hi = points_sum_hi
		self.points_lo = points_sum_lo

		if points_sum_hi > 21 :
			self.hi_busted = True
			self.preferable_points = points_sum_lo
		else:
			self.preferable_points = points_sum_hi

		if points_sum_lo > 21 : # Change to new class
			self.is_busted = True

		return (self.points_hi, self.points_lo, self.preferable_points)



	



class Participant():

	"""
	Class that models every participant of Black Jack game. 

	Participant is a class modeling every human being involved in playing Black Jack. In this case : Players and Croupier

	hand - This is a class containing info about hand status, points and 

	Every game participant is able to perform :
	Hit - participant draw a card (can drow up to bust or otherwise, if explicitely written)
	Stay - participant don't draw a card

	"""

	

	def __init__(self):

		self.is_busted = False
		self.list_of_hands = []
	

	



	def show_stats(self):
		hand = self.list_of_hands[0]
		print("Croupier : ")
		print("Cards : " + str(hand.cards))
		print('\n')



	def stand(self):
		pass

	def hit(self, hand, deck):
		if hand.hit_limit_on and len(hand.cards) > 2 : 
			raise MovementFail('You could hit only once !!') 
			return False


		hand.cards.append(deck.pop_top_card())
		hand.update_points_stats()
		return True

	

	def get_initial_hand(self,deck): 
		self.list_of_hands.append(Hand())
		initial_hand = self.list_of_hands[0]
		self.hit(initial_hand,deck)
		self.hit(initial_hand,deck)

	def make_move(self, deck, hand):
		while hand.points_lo < 17 :
			self.hit(hand,deck)
			if hand.points_lo > 21 :
				self.is_busted = True
				self.show_stats()
				return False

		self.show_stats()
		self.stand()
		return True

		

class Player(Participant):

	


	def __init__(self):
		self.money = 10000 
		#self.is_busted = False
		self.list_of_hands = []
	 



	def show_stats(self):
		for hand in self.list_of_hands:
			print("Hand " + str(self.list_of_hands.index(hand)) + " :")
			print("cards : " + str(hand.cards))
			print("bet : " + str(hand.bet))
			print("busted ? : " + str(hand.is_busted))

		print("money : " + str(self.money))
		print("\n")
	

	def initial_bet(self, bet):
		if bet > self.money : 
			print ( " Well, you can't bet this much money\n")
			return False


		self.money = self.money - bet

	def double_down(self, hand):
		"""
		 func doubling the bet, after that may take only one hit, Return : bet on doubled hand

		double_down is possible only when len(hand.cards) == 2. 

		INPUT: hand to double
		OUTPUT: Amount of money after double
		"""
		print("DOUBLE_DOWN !!!!!!!!!!!!!\n")
		print(hand)
		if not len(hand.cards) == 2 :
			raise MovementFail("you can't double with more than 2 cards !\n")
			return False #?? Will it run ?

		hand.bet = hand.bet*2
		self.money = self.money - hand.bet
		hand.hit_limit_on = True

		return hand.bet

	def split(self,hand):
		
		"""
		INPUT: hand
		OUTPUT: touple of those cards in separate hands

		split a pair into two hands
		"""

		if not len(hand.cards)  == 2 :

			print("Error, It might be an exception here !\n")
			return False

		if not hand.cards[0] == hand.cards[1]:

			print("Error : You can only split cards if you have pair !\n")
			return False

		if hand.bet > self.money:

			print("You don't have enough money !\n")
			return False

		
		#print(self.list_of_hands[1])


		new_hand = Hand()
		new_hand.cards.append(hand.cards[0])
		new_hand.bet = hand.bet
		self.money = self.money - hand.bet
		hand.cards.pop(0)
		self.list_of_hands.append(new_hand) # LEN list of hands

		hand.update_points_stats()
		new_hand.update_points_stats()


		return {self.list_of_hands[0].cards[0], self.list_of_hands[1].cards[0]}


	def execute_move(self, choosen_move, hand, deck ):
		if choosen_move == "hit":
			self.hit(hand, deck)
			return True
		if choosen_move == "double down" :
			self.double_down(hand)
			return True
		if choosen_move == "split" :
			self.split(hand)
			return True
		if choosen_move == "status" :
			self.show_stats()

		return False


	def make_move(self, deck, hand): 
		move_str = None # move place_holder (choosing)



		while not ((move_str == 'stand') or (hand.is_busted)):
			while True :
				move_str = input("")
				try:
					self.execute_move(move_str,hand, deck)
					print("\n")
					self.show_stats()
					break


				except MovementFail:
					print("There is something wrong ! Try again... \n") 
					continue

		if hand.is_busted:
			print("BUSTED !")







class Game():

	def __init__(self):
		self.game_end = False
		self.players_number = 0
		self.all_players = []
		self.croupier = Participant()
		self.deck = Deck()

	def init(self):
		self.players_number = int(input("How many players will play ? \n"))
		for player in range(self.players_number): 
			self.all_players.append(Player()) # create players
			self.deck.shuffle()

	def kick_bancrupt_players(self):
		self.all_players = [x for x in self.all_players if x.lost == False] # It  take all players that didn't lose.
		if not self.all_players : 
			self.game_end = True

			return self.all_players



	def prize_for(self,player,hand):
		player.money += hand.bet 
		hand.bet = 0

		return player.money

	def remove_bet(self,player,hand):
		hand.bet = 0
		if player.money == 0:
			player.lost = True

	def manage_bets_after_deal(self): # need to iterate through hand  | check who wins >> Give them prize stack, remove bet stack from all players
		if self.croupier.is_busted: # IF Croupier busted >> prize all not-busted hands.
			for player in self.all_players:	
				for hand in player.list_of_hands:
					if  not hand.is_busted:
						self.prize_for(player,hand)
						print("player " + str(self.all_players.index(player)) + " WON")



		for player in self.all_players:
			for hand in player.list_of_hands:
				if not hand.is_busted and hand.preferable_points > self.croupier.list_of_hands[0].preferable_points:
					self.prize_for(player,hand)
					print("player " + str(self.all_players.index(player)) + " WON")

		for player in self.all_players: # Can be optimalised by rewriting in Hand Class
			for hand in player.list_of_hands:
				self.remove_bet(player,hand)

	def show_table(self):
		print('CROUPIER : ')
		print( "card : " + str(self.croupier.list_of_hands[0].cards[0]) + '\n\n')

		

		for player in self.all_players:
			print('player  ' + str(self.all_players.index(player)) + ' :' )
			for hand in player.list_of_hands:
				print( "hand " +  str(player.list_of_hands.index(hand)) + ' :'  + str(hand.cards) )

	def clear_hands(self):
		for player in self.all_players:
			player.list_of_hands = []

		self.croupier.list_of_hands = []








		# NEW CLASS -->  "Game" with general rules functions
		# test new functions !! (GAME CLASS)



