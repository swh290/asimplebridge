from utils import *

def makeMove(state, move):
	if state.gameResult is not None:
		return # throw exception
	if state.turn != move.turn:
		return # throw exception
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
					return # throw exception
	onTable.append(move)
	player.handCard.remove(nextCard)
	state.turn = getLeftPlayer(state.turn)
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
		state.turn = winPos

def dealer(state):
	state.NSTrickNeeded = 7
	state.EWTrickNeeded = 7
	state.NSTrickCurrent = 0
	state.EWTrickCurrent = 0
	state.turn = None
	state.bidTurn = None
	state.bidStart = getRightPlayer(state.bidStart)
	state.suitThisTurn = None
	state.trump = None
	state.contract = None
	for k,v in state.contracts.iteritems():
		v = None
	state.gameResult = None
	state.cardsOnTable[:] = []
	random.shuffle(cards)
	for i in range(4):
		player = state.playerDict.get(positionType[i])
		handCard = player.handCard
		handCard[:] = []
		for j in range(13):
			handCard.append(cards[i + 4*j])
		handCard.sort()
		
		

def makeBid(state, contract):
	if state.contract is not None:
		return # throw exception
	contracts = state.contracts
	position = contract.position
	if position != state.bidTurn:
		return # throw exception
	bid = contract.bid
	rank = contract.rank
	isPass = contract.isPass
	if isPass:
		state.passCount += 1
		if state.passCount == 3 and state.bidding is not None:
			state.contract = state.bidding
			state.passCount = 0
		if state.passCount == 4:
			dealer(state)
	else:
		if contract.isLargerThan(state.bidding):
			state.passCount = 0
			state.bidding = contract
		else: 
			return # throw exception

	contracts[position] = contract
		

def getRightPlayer(pos):
	if pos == 'NORTH':
		return 'WEST'
	elif pos == 'WEST':
		return 'SOUTH'
	elif pos == 'SOUTH':
		return 'EAST'
	else: return 'NORTH'

def getLeftPlayer(pos):
	if pos == 'NORTH':
		return 'EAST'
	elif pos == 'EAST':
		return 'SOUTH'
	elif pos == 'SOUTH':
		return 'WEST'
	else: return 'NORTH'
	





		





if __name__ == '__main__':
	state = State()

	dealer(state)
	
	for k,v in state.playerDict.iteritems():
		for c in v.handCard:
			print c.__str__()
		print "^^^^^^^^^^^^^^^^^"
	
		
