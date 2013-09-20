from utils import *

class Rules(object):
	"""docstring for Rules"""
	def __init__(self, arg):
		super(Rules, self).__init__()
		self.arg = arg

	def stateChanger(self, state, move):
		if state.gameResult is not None:
			return
		if state.turn != move.turn:
			return
		nextCard = move.card
		position = move.position
		player = state.playerDict[position]
		onTable = state.cardsOnTable
		onTable.append(move)
		cardCounts = len[onTable]
		if cardCounts == 0:
			state.suitThisTurn = nextCard.suit
		if nextCard.suit != state.suitThisTurn:
			for c in player.handCard:
					if c.suit == state.suitThisTurn:
						return
		onTable.append(move)
		player.handCard.remove(nextCard)


		cardCounts = len[onTable]
		if cardCounts == 4: #clean table and next round
			winner = None
			for m in cardsOnTable:
				c = m.card
				if c.suit == state.suitThisTurn:
					if winner is None:
						winner = m
					else:
						w = winner.card
						if c.rank > w.rank:
							winner = m
			for m in cardsOnTable:
				c = m.card
				if c.suit == state.trump:
					w = winner.card
					if w.suit != state.trump:
						winner = m
					elif c.rank > w.rank:
						winner = m
			winPos = winner.position
			if winPos == 'NORTH' or winPos == 'SOUTH':
				state.NSTrickCurrent += 1
				if state.NSTrickCurrent == state.NSTrickNeeded:
					state.gameResult = "NS_WIN"
			else:
				state.EWTrickCurrent += 1
				if state.EWTrickCurrent == state.NSTrickNeeded:
					state.gameResult = "EW_WIN"
			cardsOnTable[:] = []
			state.suitThisTurn = None




		





if __name__ == '__main__':
	state = State()
	onTable = state.cardsOnTable
	onTable.append(Card(5, "Heart"))

	print onTable[0]
		
