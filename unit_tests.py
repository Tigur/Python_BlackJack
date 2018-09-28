##BlackJack Game : Unit Tests
# By Nikodem Celiński 

# file created : 13:38 | 21.09.18 

import unittest
import black_jack_classes

class DeckTest(unittest.TestCase):

	def test_poping_deck(self):
		deck = black_jack_classes.Deck()
		card_popped = deck.cards[0]
		func_output = deck.pop_top_card()

		self.assertEqual(func_output, card_popped)



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

if __name__ == '__main__':
	unittest.main()

