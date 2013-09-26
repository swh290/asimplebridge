import unittest
#from utils import *
from rules import *
import copy

class RuleTest(unittest.TestCase):
	def setUp(self):
		self.state = State()
		#dealer(self.state)

	def test_state_eq(self):
		expstate = State()
		self.assertEqual(self.state, expstate)

	def test_bid_1(self):
		contract = Contract('NORTH', 'SPADE', 2, True)
		expstate = State()
		expstate.bidTurn = 'WEST'
		expstate.bidStart = 'NORTH'
		expstate.passCount = 1
		expstate.contracts['NORTH'] = contract
		dealer(self.state)
		makeBid(self.state, contract)
		self.assertEqual(self.state, expstate)

	def test_bid_2(self):
		contract = Contract('NORTH', 'SPADE', 2, False)
		expstate = State()
		expstate.bidTurn = 'WEST'
		expstate.bidStart = 'NORTH'
		expstate.bidding = contract
		expstate.passCount = 0
		expstate.contracts['NORTH'] = contract
		dealer(self.state)
		makeBid(self.state, contract)
		self.assertEqual(self.state, expstate)

	def test_bid_3(self):
		contract1 = Contract('NORTH', 'SPADE', 2, False)
		contract2 = Contract('WEST', 'CLUB', 3, False)
		expstate = State()
		expstate.bidTurn = 'SOUTH'
		expstate.bidStart = 'NORTH'
		expstate.bidding = contract2
		expstate.passCount = 0
		expstate.contracts['NORTH'] = contract1
		expstate.contracts['WEST'] = contract2
		dealer(self.state)
		makeBid(self.state, contract1)
		makeBid(self.state, contract2)
		self.assertEqual(self.state, expstate)

	def test_bid_4(self):
		contract1 = Contract('NORTH', 'SPADE', 2, False)
		contract2 = Contract('WEST', 'CLUB', 3, False)
		contract3 = Contract('SOUTH', 'CLUB', 3, True)
		expstate = State()
		expstate.bidTurn = 'EAST'
		expstate.bidStart = 'NORTH'
		expstate.bidding = contract2
		expstate.passCount = 1
		expstate.contracts['NORTH'] = contract1
		expstate.contracts['WEST'] = contract2
		expstate.contracts['SOUTH'] = contract3
		dealer(self.state)
		makeBid(self.state, contract1)
		makeBid(self.state, contract2)
		makeBid(self.state, contract3)
		self.assertEqual(self.state, expstate)

	def test_bid_5(self):
		contract1 = Contract('NORTH', 'SPADE', 2, False)
		contract2 = Contract('WEST', 'CLUB', 3, False)
		contract3 = Contract('SOUTH', 'CLUB', 3, True)
		contract4 = Contract('EAST', 'CLUB', 3, True)
		contract5 = Contract('NORTH', 'CLUB', 3, True)
		expstate = State()
		expstate.bidTurn = 'WEST'
		expstate.bidStart = 'NORTH'
		expstate.turn = 'NORTH'
		expstate.bidding = contract2
		expstate.contract = contract2
		expstate.passCount = 0
		expstate.contracts['NORTH'] = contract5
		expstate.contracts['WEST'] = contract2
		expstate.contracts['SOUTH'] = contract3
		expstate.contracts['SOUTH'] = contract4
		dealer(self.state)
		makeBid(self.state, contract1)
		makeBid(self.state, contract2)
		makeBid(self.state, contract3)
		makeBid(self.state, contract4)
		makeBid(self.state, contract5)
		self.assertEqual(self.state, expstate)

if __name__ == '__main__':
	state = State()
	dealer(state)
	state.turn = 'EAST'
	#state.NSTrickCurrent = 6
	state.contract = Contract('WEST', 'NOTRUMP', 3, False)
	
	makeMove(state, Move('EAST', Card(3, 'HEART')))
	makeMove(state, Move('SOUTH', Card(3, 'DIMOND')))
	makeMove(state, Move('WEST', Card(3, 'SPADE')))
	makeMove(state, Move('NORTH', Card(3, 'CLUB')))
	print str(state)
	unittest.main()

	
