##BlackJack Game : Unit Tests
# By Nikodem Celiński 

# file created : 13:38 | 21.09.18 

import unittest
import black_jack_classes


def check_if_shuffled(deck):
	model_deck = black_jack_classes.Deck()
	i = 0
	is_different = False
	for card in deck.cards:
		if model_deck.cards[i] != card :
			is_different = True
			break
		i+=1

	if i<26 :
		print("probably shuffled ! ")
		return True

	else : 
		print("Probably not shuffled. Check again ! ")
		return False



class DeckTest(unittest.TestCase):

	def test_cards_range(self):
		deck = black_jack_classes.Deck()
		func_output = len(deck.cards)

		print ("LENGTH OF CARDS : {} \n".format(func_output) )

		self. assertEqual(func_output, 52 )

	def test_poping_deck(self):
		deck = black_jack_classes.Deck()
		card_popped = deck.cards[0]
		func_output = deck.pop_top_card()

		self.assertEqual(func_output, card_popped)


	def test_shuffle(self):
		deck = black_jack_classes.Deck()
		deck.shuffle()
		check_if_shuffled(deck)
		self.assertEqual(check_if_shuffled(deck), True)


class PlayerTest(unittest.TestCase):

	


	def test_double_down(self):
		player = black_jack_classes.Player()
		player.list_of_hands.append(black_jack_classes.Hand())
		current_hand = player.list_of_hands[0]

		current_hand.cards.append(10)
		current_hand.cards.append(9)

		player.money = 5000
		
		current_hand.bet = 500
		first_bet=500
		new_bet_on_hand = player.double_down(current_hand)

		self.assertEqual(new_bet_on_hand,first_bet*2)
		self.assertEqual(player.money, 4000)


	def test_split(self):
		player2 = black_jack_classes.Player()
		player2.money = 3000

		player2.list_of_hands.append(black_jack_classes.Hand())
		old_hand = player2.list_of_hands[0]
		old_hand.cards = [8,8]
		old_hand.bet = 500
		new_hands_touple = {8,8}

		func_output = player2.split(old_hand)

		self.assertEqual(func_output, new_hands_touple)
		self.assertEqual(len(player2.list_of_hands), 2)

	def test_make_move(self):
		player = black_jack_classes.Player()
		player.list_of_hands.append(black_jack_classes.Hand())
		hand = player.list_of_hands[0]
		#print(hand)
		deck = black_jack_classes.Deck()
		hand.cards = [8,8]

		print(hand)

		print("TEST MAKE MOVE ")
		func_output = player.make_move(deck, hand)

if __name__ == '__main__':
	unittest.main()

