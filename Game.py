
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
		self._mid_card = self._deck[-1]
		
		self._cur_p = random.randint(0, 1)
		

	def step(self):
		player = self._players[self._cur_p]
		legal_moves = self.find_legal_moves()
		if len(legal_moves) == 0:
			# Lose due to no legal moves
			return 1 - self._cur_p
		mov = player.choose_move(legal_moves, self._cur_p, self._laws, self._board, self._hands, self._mid_card)
		

	def find_legal_moves(self):
		raise NotImplemented()
