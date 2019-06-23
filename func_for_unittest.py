import black_jack_classes

def player_init(money,hands):
	player = black_jack_classes.Player()
	player.money = money
	player.list_of_hands = hands

	return player

def hand_init(cards,bet):
	hand = black_jack_classes.Hand()
	hand.cards = cards
	hand.bet = bet
	hand.update_points_stats()

	return hand
def croupier_init(game,cards):
	game.croupier.list_of_hands = [hand_init(cards, 0)]

	return game.croupier
	


