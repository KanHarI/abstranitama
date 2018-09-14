
import numpy as np

EMPTY = 0
DST = 1
ORIGIN = 2

class Card:
	def __init__(self, radius, movs):
		movs = sorted(movs)
		self._radius = radius
		self._size = radius * 2 - 1
		self._movs = movs
		self._map = np.zeros((self._size, self._size), dtype=np.int8)
		self._map[radius-1][radius-1] = ORIGIN
		for mov in movs:
			self._map[tuple(mov-radius)] += DST

	def __repr__(self):
		return str(self._map)
