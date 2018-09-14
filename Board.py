
import numpy as np

EMPTY = 0
SOLDIER_FLAG = 1
KING_FLAG = 2
TEMPLE_FLAG = 8
SOLDIER_1 = 1
SOLDIER_2 = -1
KING_1 = 3
KING_2 = -3
TEMPLE_1 = 8
TEMPLE_2 = -8

class Board:
	def __init__(self, r_width, r_length):
		self._width = r_width * 2 - 1
		self._length = r_length * 2 - 1
		self._map = np.zeros((self._length, self._width), dtype=np.int8)
		for j in range(self._width):
			for i in [0,self._length-1]:
				if  j == r_width-1:
					self._map[i,j] = TEMPLE_1 + KING_1
				else:
					self._map[i,j] = SOLDIER_1
				if i != 0:
					self._map[i,j] *= -1

	def __repr__(self):
		return str(self._map)

	def is_in_board(self, pt):
		pt = tuple(pt)
		return (pt[0] >= 0 and pt[1] >= 0 and pt[0] < self._length and pt[1] < self._width)

	def is_legal_mov(self, src, dst):
		src,dst = tuple(src),tuple(dst)
		return (self.is_in_board(src) and self.is_in_board(dst) and (self._map[src] & 1 == 1) and (self._map[dst] & 1 == 0))

	def mov(self, src, dst):
		src,dst = tuple(src),tuple(dst)
		if not self.is_legal_mov(src, dst):
			raise RuntimeError("Bad move!")
		player = 1 if (self._map[src] % 8) < 4 else -1
		tier = (self._map[src]*player) & 3
		self._map[src] -= tier * player
		self._map[dst] += tier * player

