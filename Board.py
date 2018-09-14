
import numpy as np

EMPTY = 0
SOLDIER_FLAG = 1
KING_FLAG = 2
TEMPLE_FLAG = 4
P2_FLAG = 8
P2_TEMPLE_FLAG = 16


class Board:
	def __init__(self, r_width, r_length):
		self._width = r_width * 2 - 1
		self._length = r_length * 2 - 1
		self._map = np.zeros((self._length, self._width), dtype=np.int8)
		
		self._items = {
			"p1s":[],
			"p2s":[],
			"p1k":[],
			"p2k":[],
			"p1t":[],
			"p2t":[]
			}

		for j in range(self._width):
			for i in [0,self._length-1]:
				if  j == r_width-1:
					self._map[i,j] = TEMPLE_FLAG + KING_FLAG
					if i == 0:
						self._items["p1k"].append((i,j))
						self._items["p1t"].append((i,j))
					else:
						self._items["p2k"].append((i,j))
						self._items["p2t"].append((i,j))
						self._map[i,j] += P2_TEMPLE_FLAG
				self._map[i,j] += SOLDIER_FLAG
				if i == 0:
					self._items["p1s"].append((i,j))
				if i != 0:
					self._items["p2s"].append((i,j))
					self._map[i,j] += P2_FLAG

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
		player = 1 if (self._map[src] & P2_FLAG) else 0
		tier = self._map[src] & (SOLDIER_FLAG + KING_FLAG)
		
		self._map[src] -= tier
		self._map[src] &= ~P2_FLAG

		self._map[dst] = (self._map[dst] & (~(SOLDIER_FLAG + KING_FLAG))) + tier
		self._map[dst] &= ~P2_FLAG
		self._map[dst] |= player*P2_FLAG

	def get_filtered_map(self, flag):
		assert flag in [SOLDIER_FLAG, KING_FLAG, TEMPLE_FLAG]
		if flag == TEMPLE_FLAG:
			return (self._map & flag) * np.sign(P2_TEMPLE_FLAG/2 - (self._map & P2_TEMPLE_FLAG))
		return (self._map & flag) * np.sign(P2_FLAG/2 - (self._map & P2_FLAG))

