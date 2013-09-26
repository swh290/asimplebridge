import random
import rules

suitType = ('CLUB', 'DIMOND', 'HEART', 'SPADE')
bidType = ('CLUB', 'DIMOND', 'HEART', 'SPADE', 'NOTRUMP')
positionType = ('NORTH', 'SOUTH', 'EAST', 'WEST')

class Card(object):
	def __init__(self, rank, suit):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return "[suit:" + self.suit + " rank:" + str(self.rank) +"]"

	def __lt__(self, other):
		if self.suit == other.suit:
			return self.rank < other.rank
		else:
			return suitType.index(self.suit) < suitType.index(other.suit)
	def __eq__(self, other):
		return self.suit == other.suit and self.rank == other.rank

cards = []
for t in suitType:
	for i in range(13):
		cards.append(Card(i, t))
random.shuffle(cards)

class Player(object):
	
	def __init__(self, position = None, handCard = None):
		self.position = position
		if handCard is None:
			self.handCard = []
		else:
			self.handCard = handCard

	def __str__(self):
		return "[position:" + self.position + " handCard:" + ','.join(map(str, self.handCard)) + ']'

	def __eq__(self, other):
		return self.position == other.position and set(self.handCard) == set(other.handCard)

class Contract(object):
	"""docstring for Contract"""
	def __init__(self, position, bid = None, rank = None, isPass = True):
		super(Contract, self).__init__()
		self.position = position
		self.bid = bid
		self.rank = rank
		self.isPass = isPass

	def isLargerThan(self, other):
		if other is None or other.isPass: return True
		if self.rank != other.rank:
			return self.rank > other.rank
		else: return bidType.index(self.bid) > bidType.index(other.bid)

	def __str__(self):
		if self.isPass:
			return '[contract pass]'
		else:
			return '[contract position: ' + self.position + ' bid: ' + self.bid + ' rank: ' + str(self.rank) + ']'


class Move(object):
	"""docstring for Move"""
	def __init__(self, position, card):
		super(Move, self).__init__()
		self.position = position
		self.card = card
	def __str__(self):
		return '[Move Position: ' + self.position + ' Card: ' + str(self.card) + ']'

class State(object):
	"""docstring for State"""
	def __init__(self):
		super(State, self).__init__()
		self.NSTrickNeeded = 7
		self.EWTrickNeeded = 7
		self.NSTrickCurrent = 0
		self.EWTrickCurrent = 0
		self.turn = None
		self.bidTurn = None
		self.bidStart = "EAST"
		self.suitThisTurn = None
		self.contract = None
		self.bidding = None
		self.gameResult = None
		self.cardsOnTable = []
		self.contracts = {'NORTH': None, 'SOUTH': None, 'EAST': None, 'WEST': None}
		self.passCount = 0
		self.playerN = Player("NORTH")
		self.playerS = Player("SOUTH")
		self.playerE = Player("EAST")
		self.playerW = Player("WEST")
		self.playerDict = {'NORTH': self.playerN, 'SOUTH': self.playerS, 'EAST': self.playerE, 'WEST': self.playerW}
	def __eq__(self, other):
		return (self.NSTrickNeeded == other.NSTrickNeeded and 
			self.EWTrickNeeded == other.EWTrickNeeded and 
			self.NSTrickCurrent == other.NSTrickCurrent and 
			self.EWTrickCurrent == other.EWTrickCurrent and 
			self.turn == other.turn and 
			self.bidTurn == other.bidTurn and
			self.bidStart == other.bidStart and
			self.suitThisTurn == other.suitThisTurn and
			self.contract == other.contract and
			self.bidding == other.bidding and
			self.gameResult == other.gameResult and
			set(self.cardsOnTable) == set(other.cardsOnTable) and
			set(self.contracts) == set(other.contracts) and
			self.passCount == other.passCount and
			set(self.playerDict) == set(other.playerDict))
	def __str__(self):
		return ('NSTrickNeeded: ' + str(self.NSTrickNeeded) + '\n' +
			'NSTrickCurrent: ' + str(self.NSTrickCurrent) + '\n' +
			'EWTrickNeeded: ' + str(self.EWTrickNeeded) + '\n' +
			'EWTrickCurrent: ' + str(self.EWTrickCurrent) + '\n' +
			'turn: ' + str(self.turn) + '\n' +
			'bidTurn: ' + str(self.bidTurn) + '\n' +
			'bidStart: ' + str(self.bidStart) + '\n' +
			'suitThisTurn: ' + str(self.suitThisTurn) + '\n' +
			'contract: ' + str(self.contract) + '\n' +
			'bidding: ' + str(self.bidding) + '\n' +
			'contracts: ' + '\n'.join(map(str, self.contracts.values())) + '\n' +
			'gameResult: ' + str(self.gameResult) + '\n' +
			'cardsOnTable: ' + ','.join(map(str, [i for i in self.cardsOnTable])) + '\n' +
			'passCount: ' + str(self.passCount) + '\n' +
			'players: ' + '\n'.join(map(str, self.playerDict.values())))


if __name__ == '__main__':
	state = State()
	contract = Contract('NORTH', 'SPADE', 2, False)
	rules.dealer(state)
	rules.makeBid(state, contract)
	state.cardsOnTable.append(Card(3, 'HEART'))
	state.cardsOnTable.append(Card(4, 'DIMOND'))
	print str(state)