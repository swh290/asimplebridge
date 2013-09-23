import random
suitType = ('CLUB', 'DIMOND', 'HEART', 'SPADE')
bidType = ('CLUB', 'DIMOND', 'HEART', 'SPADE', 'NOTRUMP')
positionType = ('NORTH', 'SOUTH', 'EAST', 'WEST')

class Card(object):
	suit = None
	rank = None
	def __init__(self, rank, suit = "None"):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return "suit:" + self.suit + " rank:" + str(self.rank)

	def __lt__(self, other):
		if self.suit == other.suit:
			return self.rank < other.rank
		else:
			return suitType.index(self.suit) < suitType.index(other.suit)

cards = []
for t in suitType:
	for i in range(13):
		cards.append(Card(i, t))
random.shuffle(cards)

class Player(object):
	position = None
	handCard = []
	def __init__(self, position = "None"):
		self.position = position
		#self.handCard = handCard

	def __str__(self):
		return "position:" + self.position + " handCard:" + str(self.handCard)

class Contract(object):
	"""docstring for Contract"""
	position = None
	bid = None
	rank = None
	isPass = False
	def __init__(self, position, bid, rank, isPass = False):
		super(Contract, self).__init__()
		self.position = position
		self.bid = bid
		self.rank = rank
		self.isPass = isPass

	def islargerThan(other):
		if other.isPass: return True
		if this.rank != other.rank:
			return self.rank > other.rank
		else: return bidType.index(self.bid) > bidType.index(other.bid)


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
	bidTurn = None
	bidStart = "NORTH"
	suitThisTurn = None
	trump = None
	contract = None
	bidding = None
	gameResult = None
	cardsOnTable = []
	contracts = {'NORTH': None, 'SOUTH': None, 'EAST': None, 'WEST': None}
	passCount = 0
	playerN = Player("NORTH")
	playerS = Player("SOUTH")
	playerE = Player("EAST")
	playerW = Player("WEST")
	playerDict = {'NORTH': playerN, 'SOUTH': playerS, 'EAST': playerE, 'WEST': playerW}
	def __init__(self):
		super(State, self).__init__()

if __name__ == "__main__" :
	
	for c in cards:
		print c.suit + "  " + str(c.rank)