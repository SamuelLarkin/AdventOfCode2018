from collections import namedtuple
import numpy as np
from numpy import linalg as LA


#Cart = namedtuple('Cart', ('position', 'direction', 'next_move'))
class Cart():
    def __init__(self, position, direction, next_move):
        self._position = position
        self._direction = direction
        self._next_move = next_move
        self._alive = True

    @property
    def p(self):
        return (self.position[0], self.position[1])

    @property
    def position(self):
        return self._position
    @position.setter
    def position(self, value):
        self._position = value
        assert value[0] >= 0
        assert value[1] >= 0

    @property
    def direction(self):
        return self._direction
    @direction.setter
    def direction(self, value):
        self._direction = value
        assert LA.norm(value) == 1

    @property
    def next_move(self):
        return self._next_move
    @next_move.setter
    def next_move(self, value):
        self._next_move = value

    def move_on_track(self, track):
        self.position += self.direction
        t = track[self.position[0]][self.position[1]] 
        if t in '/\\':
            self.direction = corner[t](self.direction)
        elif t == '+':
            self.direction = intersection[self.next_move](self.direction)
            self.next_move = (self.next_move + 1) % 3
        elif t == ' ':
            assert False
        assert t in '+-|><v^/\\', t


    def __repr__(self):
        return 'Cart(position: {} direction: {} next_move: {})'.format(self.position, self.direction, self.next_move)

    def __str__(self):
        return 'position: {} direction: {} next_move: {}'.format(self.position, self.direction, self.next_move)



moves = {
        '>': np.asarray((0, 1), dtype=np.int),
        '<': np.asarray((0, -1), dtype=np.int),
        '^': np.asarray((-1, 0), dtype=np.int),
        'v': np.asarray((1, 0), dtype=np.int),
        }



corner = {
        '/': lambda d: -np.flip(d),
        '\\': lambda d: np.flip(d),
        }



# Left, Straight, Right
leftTurn  = np.asarray([[0, -1],[1, 0]], dtype=np.int)
rightTurn = np.asarray([[0, 1],[-1, 0]], dtype=np.int)
if True:
    intersection = [
            lambda d: np.matmul(leftTurn, d),
            lambda d: d,
            lambda d: np.matmul(rightTurn, d),
            ]
else:
    intersection = [
            lambda d: np.matmul(d, leftTurn),
            lambda d: d,
            lambda d: np.matmul(d, rightTurn),
            ]



def parse(f):
    track = [l.strip('\n') for l in f]
    carts = []
    for i, t in enumerate(track):
        for j, d in enumerate(t):
            if d in '<>^v':
                carts.append(Cart(np.asarray([i,j]), moves[d], 0))

    return track, carts
