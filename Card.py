
import numpy as np

EMPTY = 0
DST = 1
ORIGIN = 2

class Card:
	def __init__(self, radius, movs):
		movs = sorted(movs, key=lambda pt:(pt[0],pt[1]))
		self._radius = radius
		self._size = radius * 2 - 1
		self._movs = movs
		self._map = np.zeros((self._size, self._size), dtype=np.int8)
		self._map[radius-1][radius-1] = ORIGIN
		for mov in movs:
			if self._map[tuple(mov+radius-1)] == 1:
				raise RuntimeError("Card with overlapping move detected!")
			self._map[tuple(mov+radius-1)] += DST

	def __repr__(self):
		return str(self._map)


class _5x5Card(Card):
	def __init__(self, movs):
		super().__init__(3, movs)

Tiger = _5x5Card(np.array([
		[2, 0],
		[-1, 0]
	]))

Crab = _5x5Card(np.array([
		[1, 0],
		[0, 2],
		[0, -2]
	]))

Monkey = _5x5Card(np.array([
		[1, 1],
		[1, -1],
		[-1, 1],
		[-1, -1]
	]))


Crane = _5x5Card(np.array([
		[1, 0],
		[-1, 1],
		[-1, -1],
	]))

Dragon = _5x5Card(np.array([
		[1, 2],
		[1, -2],
		[-1, 1],
		[-1, -1]
	]))

Elephent = _5x5Card(np.array([
		[1, 1],
		[1, -1],
		[0, 1],
		[0, -1]
	]))

Mantis = _5x5Card(np.array([
		[1, 1],
		[1, -1],
		[-1, 0]
	]))


Boar = _5x5Card(np.array([
		[1, 0],
		[0, -1],
		[0, 1]
	]))

Frog = _5x5Card(np.array([
		[1, 1],
		[0, 2],
		[-1, -1]
	]))

Goose = _5x5Card(np.array([
		[1, 1],
		[0, 1],
		[0, -1],
		[-1, -1]
	]))

Horse = _5x5Card(np.array([
		[1, 0],
		[0, 1],
		[-1, 0]
	]))

Eel = _5x5Card(np.array([
		[1, 1],
		[0, -1],
		[-1, 1]
	]))

def hflip(card):
	flipped_moves = np.array(list(map(lambda pt: (pt[0],-pt[1]), card._movs)))
	return Card(card._radius, flipped_moves)

Rabbit = hflip(Frog)
Rooster = hflip(Goose)
Ox = hflip(Horse)
Cobra = hflip(Eel)

DefaultDeck = [Tiger, Crab, Monkey, Crane, Dragon, Elephent, Mantis, Boar, Frog, Goose, Horse, Eel, Rabbit, Rooster, Ox, Cobra]
