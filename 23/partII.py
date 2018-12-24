from collections import namedtuple
from heapq import heapify, heappush, heappop
from itertools import product
import logging



CubeBase = namedtuple('CubeBase', ('x1', 'y1', 'z1', 's'))
class Cube(CubeBase):
    @property
    def x2(self):
        return self.x1 + self.s - 1


    @property
    def y2(self):
        return self.y1 + self.s - 1


    @property
    def z2(self):
        return self.z1 + self.s - 1


    @property
    def distance(self):
        return (min(abs(self.x1), abs(self.x2))
                + min(abs(self.y1), abs(self.y2))
                + min(abs(self.z1), abs(self.z2)))


    def __iter__(self):
        '''
        Iterates of 8 sub cubes.
        '''
        s = self.s // 2
        for dx, dy, dz in product((0, s), repeat=3):
            yield Cube(self.x1 + dx, self.y1 + dy, self.z1 + dz, s)



BotBase = namedtuple('BotBase', ('x', 'y', 'z', 'r'))
class Bot(BotBase):
    def range_clips_with_cube(self, cube):
        # Does the octahedron defined by this bot
        # overlap with the cube (x1,y1,z1)-(x2,y2,z2)?
        dist = 0
        if self.x < cube.x1:   dist += cube.x1 - self.x
        elif self.x > cube.x2: dist += self.x - cube.x2

        if self.y < cube.y1:   dist += cube.y1 - self.y
        elif self.y > cube.y2: dist += self.y - cube.y2

        if self.z < cube.z1:   dist += cube.z1 - self.z
        elif self.z > cube.z2: dist += self.z - cube.z2

        return dist <= self.r



class PriorityQueue:
    def __init__(self, bots):
        self.q = []
        self.bots = bots


    def add(self, cube):
        in_range = len(list(filter(lambda b: b.range_clips_with_cube(cube), self.bots)))
        if in_range > 0:
            # Distance from (0,0,0) to the closest corner of the cube
            heappush(self.q, (-in_range, cube.distance, cube.s, cube))

        #logging.getLogger(__name__).debug('queue len: {}'.format(len(self.q)))
        #print('queue len: {}'.format(len(self.q)))


    def pop(self):
        return heappop(self.q)



def master_cube(bots):
    '''
    Creates a cube that will box all nanobots.  The cube will have a size power of 2.
    '''
    min_x = min(b.x for b in bots)
    max_x = max(b.x for b in bots)
    min_y = min(b.y for b in bots)
    max_y = max(b.y for b in bots)
    min_z = min(b.z for b in bots)
    max_z = max(b.z for b in bots)

    s = 1  # size of the cube, a power of two
    while s < max(max_x - min_x, max_y - min_y, max_z - min_z):
        s *= 2
    print('Initial size:', s)

    return Cube(min_x, min_y, min_z, s)


