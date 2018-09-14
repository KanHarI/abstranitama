
import copy
import random

import Card
import Board

class Game:
	def __init__(self, p_cards, deck, boardsize, players):
		self._laws = (p_cards, boardsize, deck)
		
		self._board = Board.Board(*boardsize)
		
		self._deck = copy.deepcopy(deck)
		random.shuffle(self._deck)
		self._deck = self._deck[:p_cards * 2 + 1]
		
		self._players = players
		self._hands = [self._deck[:p_cards], self._deck[p_cards:p_cards*2]]
		
		self._cur_p = random.randint(0, 1)
		

	def step(self):
		player = self._players[self._cur_p]
		legal_moves = self.find_legal_moves()

	def find_legal_moves(self):
		
