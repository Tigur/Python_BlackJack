#BlackJack Game : CLASSES
#By Nikodem Celiński 

#file created : 14:00 | 18.09.18 


import random

class Deck():

	possible_figures = [2,3,4,5,6,7,8,9,10,'J','D','K','A']
	cards = possible_figures*4


	def shuffle(self):
		random.shuffle(Deck.cards)

	def pop_top_card(self):
		"""
		INPUT: none
		OUTPUT: first card in deck

		Function deletes returned card from deck.
		"""

		top_card = Deck.cards[0]
		Deck.cards.pop(0)
		return top_card


class Hand():
	"""
	Class represents a participant's hand. 

	hand - a list of cards
	
	"""

	cards = []

	points = 0
	is_busted = False
	bet = 0
	only_one_hit = False

	



class GameParticipant():

	"""
	Class that models every participant of Black Jack game. 
	Player and Croupiers alike.

	hand - This is a class containing info about hand status, points and 

	Every game participant is able to perform :
	Hit - participant draw a card (can drow up to bust or otherwise, if explicitely written)
	Stay - participant don't draw a card

	"""

	is_busted = False
	list_of_hands = []

	

	def initial_bet(self, bet):
		if bet > Player.money : 
			print ( " Well, you can't bet this much money")
			return False


		Player.money = Player.money - bet
		return bet


	def stand(self):
		pass

	def hit(self, hand, deck):
		hand.cards.append(deck.pop_top_card())

	def take_card(self,hand):
		pass

class Player(GameParticipant):

	money = 0 # players avaliable money in game

	def double_down(self, hand):
		"""
		# double the bet and may take only one hit

		#if has only two cards then possible
		#hand.doubled_down = True

		INPUT: hand to double
		OUTPUT: Amount of money after double
		"""

		hand.bet = hand.bet*2
		Player.money = Player.money - hand.bet

		return hand.bet

	def split(self,hand):
		
		"""
		INPUT: hand
		OUTPUT: touple of those cards in separate hands

		split a pair into two hands
		"""

		if not len(hand.cards)  == 2 :

			print("Error, It might be an exception here !")

		if hand.bet > Player.money:

			print("You don't have enough money !")

		new_hand = Hand()
		new_hand.cards.append(hand.cards[0])
		hand.cards.pop(0)
		Player.list_of_hands.append(new_hand) # LEN list of hands

		return {new_hand.cards[0],hand.cards[0]}


