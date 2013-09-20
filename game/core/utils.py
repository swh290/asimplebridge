class Card(object):
	suit = None
	rank = None
	def __init__(self, rank, suit = "None"):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return "suit:" + self.suit + " rank:" + str(self.rank)

class Player(object):
	position = None
	handCard = None
	def __init__(self, position = "None", handCard = []):
		self.position = position
		self.handCard = handCard

	def __str__(self):
		return "position:" + self.position + " handCard:" + str(self.handCard)

class Contract(object):
	"""docstring for Contract"""
	def __init__(self, suit, rank):
		super(Contract, self).__init__()
		self.suit = suit
		self.rank = rank
		isPass = False

class Move(object):
	position = None
	card = None
	"""docstring for Move"""
	def __init__(self, position, card):
		super(Move, self).__init__()
		self.position = position
		self.card = card

class State(object):
	"""docstring for State"""
	NSTrickNeeded = 7
	EWTrickNeeded = 7
	NSTrickCurrent = 0
	EWTrickCurrent = 0
	turn = None
	suitThisTurn = None
	trump = None
	contract = Contract("None", 0)
	gameResult = None
	cardsOnTable = []
	playerN = Player("NORTH")
	playerS = Player("SOUTH")
	playerE = Player("EAST")
	playerW = Player("WEST")
	playerDict = {'NORTH': playerN, 'SOUTH': playerS, 'EAST': playerE, 'WEST': playerW}
	def __init__(self, playerN = Player(), playerS = Player()
				, playerE = Player(), playerW = Player()):
		super(State, self).__init__()
		self.playerN = playerN
		self.playerS = playerS
		self.playerE = playerE
		self.playerW = playerW
		
		


if __name__ == "__main__" :
	card1 = Card(3)
	card2 = Card(5, "Club")
	print(card1.__str__())
	print(card2.__str__())