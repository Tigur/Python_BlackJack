#BlackJack Game : CLASSES
#By Nikodem Celiński 

#file created : 14:00 | 18.09.18 


import random
from bj_exceptions import MovementFail 

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

	def __init__(self):
		self.cards = []

		self.points = 0
		self.is_busted = False
		self.bet = 0
		self.only_one_hit = False

	def __str__(self):

		cards_str = str(self.cards)
		points_str = str(self.points)
		is_busted_str = str(self.is_busted)
		bet_str = str(self.bet)
		one_hit_str = str(self.only_one_hit)

		print("CARDS : " + cards_str)
		print("POINTS : " + points_str)
		print("IS_BUSTED :" + is_busted_str)
		print("BET : " + bet_str)
		print("ONE_HIT : " + one_hit_str)

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
		if hand.only_one_hit and len(hand.cards) > 2 : 
			raise MovementFail('You could hit only once !!') # can I just return this exception ? 
			return False


		hand.cards.append(deck.pop_top_card())
		return True

	def take_card(self,hand):
		pass

	def get_initial_hand(self,deck): ####### NEED TO BE TESTED
		self.list_of_hands.append(Hand())
		initial_hand = self.list_of_hands[0]
		self.hit(initial_hand,deck)
		self.hit(initial_hand,deck)

	def make_move(self,hand,deck):
		while self.hand.points < 17 :
			self.hit(hand,deck)
			if self.points > 21 :
				self.is_busted = True
				return False

		self.stay()
		return True

		

class Player(GameParticipant):

	def __init__(self):
		self.money = 10000 
		self.is_busted = False
		self.list_of_hands = []
	 



	def make_move(self, hand,deck): ####### NEED TO BE TESTED 
		move = None

		player_possible_moves = {

			'stand' : 1,# self.stand(),
			'hit' : 2,# self.hit(hand,deck),
			'double down' : 3,# self.double_down(hand),
			'split': 4# self.split(hand)
	


			}

		while not move == 'stand':
			while True :
				move = input("")
				try:
					player_possible_moves[move]
					break


				except KeyError:
					print("There is something wrong ! Try again...") 
					continue


	

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
		hand.only_one_hit = True

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




		# Need to know : 
			# can I return an exception ? 
			# can I define self.money out of __init__ and it will be specific objec value ? 

		# Need to be tested : 
			# make_move
			# get_initial_hand
			# all of that exceptions and my new one 


