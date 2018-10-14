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

		top_card = self.cards[0]
		self.cards.pop(0)
		return top_card


class Hand():
	"""
	Class represents a participant's hand. 

	hand - a list of cards
	
	"""

	def __init__(self):
		self.cards = []

		self.points = 0
		self.is_busted = False
		self.bet = 0
		self.hit_limit_on = False

	def __str__(self):

		cards_str = str(self.cards)
		points_str = str(self.points)
		is_busted_str = str(self.is_busted)
		bet_str = str(self.bet)
		hit_limit_str = str(self.hit_limit_on)

		print("CARDS : " + cards_str)
		print("POINTS : " + points_str)
		print("IS_BUSTED :" + is_busted_str)
		print("BET : " + bet_str)
		print("HIT_LIMIT : " + hit_limit_str)

		return ''



	



class GameParticipant():

	"""
	Class that models every participant of Black Jack game. 
	Player and Croupiers alike.

	hand - This is a class containing info about hand status, points and 

	Every game participant is able to perform :
	Hit - participant draw a card (can drow up to bust or otherwise, if explicitely written)
	Stay - participant don't draw a card

	"""

	

	def __init__(self):

		self.is_busted = False
		self.list_of_hands = []
	

	


	def stand(self):
		pass

	def hit(self, hand, deck):
		if hand.hit_limit_on and len(hand.cards) > 2 : 
			raise MovementFail('You could hit only once !!') # can I just return this exception ? 
			return False


		hand.cards.append(deck.pop_top_card())
		return True

	

	def get_initial_hand(self,deck): ####### NEED TO BE TESTED
		self.list_of_hands.append(Hand())
		initial_hand = self.list_of_hands[0]
		self.hit(initial_hand,deck)
		self.hit(initial_hand,deck)

	def make_move(self, deck, hand):
		while hand.points < 17 :
			self.hit(hand,deck)
			if hand.points > 21 :
				self.is_busted = True
				return False

		self.stay()
		return True

		

class Player(GameParticipant):

	def __init__(self):
		self.money = 10000 
		self.is_busted = False
		self.list_of_hands = []
	 



	

	

	def initial_bet(self, bet):
		if bet > self.money : 
			print ( " Well, you can't bet this much money")
			return False


		self.money = self.money - bet

	def double_down(self, hand):
		"""
		# double the bet and may take only one hit

		#if has only two cards then possible
		#hand.doubled_down = True

		INPUT: hand to double
		OUTPUT: Amount of money after double
		"""
		print("DOUBLE_DOWN !!!!!!!!!!!!!")
		print(hand)
		if not len(hand.cards) == 2 :
			raise MovementFail("you can't double with more than 2 cards !")
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

			print("Error, It might be an exception here !")
			return False

		if hand.bet > self.money:

			print("You don't have enough money !")
			return False

		
		#print(self.list_of_hands[1])


		new_hand = Hand()
		new_hand.cards.append(hand.cards[0])
		new_hand.bet = hand.bet
		self.money = self.money - hand.bet
		hand.cards.pop(0)
		self.list_of_hands.append(new_hand) # LEN list of hands


		return {self.list_of_hands[0].cards[0], self.list_of_hands[1].cards[0]}


		def execute_move(self, choosen_move, hand, deck ):
			if choosen_move == "hit":
				hit(hand, deck)
				return True
			if choosen_move == "double down" :
				double_down(hand)
				return True
			if choosen_move == "split" :
				split(hand)
				return True

			return False


		def make_move(self, deck, hand): ####### NEED TO BE TESTED 
			move_str = None # move place_holder (choosing)

			player_possible_moves = {

				'stand' :  stand,
				'hit' :  hit,
				'double down' :  double_down,
				'split':  split
		


				}

			while not move_str == 'stand':
				while True :
					move_str = input("")
					try:
						self.execute_move(move_str,hand, deck)
						break


					except MovementFail:
						print("There is something wrong ! Try again...") 
						continue





		# Need to know : 
			# can I return an exception ? It can be catched out of func 
			# can I define self.money out of __init__ and it will be specific objec value ? NOPE

		# Need to be tested : 
			# make_move
			# get_initial_hand
			# all of that exceptions and my new one 


		# features : 
			# Deck shouldn't be passed
			#

