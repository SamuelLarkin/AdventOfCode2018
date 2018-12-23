from collections import namedtuple
import re

NanobotBase = namedtuple('NanobotBase', ('x', 'y', 'z', 'radius'))
class Nanobot(NanobotBase):
    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)



def parse(f):
    # pos=<-29190031,25416717,35666685>, r=64801770
    nanobot_re = re.compile(r'pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)')
    nanobots = []
    for l in f:
        m = nanobot_re.match(l.strip())
        assert m, l
        x,y,z,r = list(map(int, m.group(1,2,3,4)))
        nanobots.append(Nanobot(x,y,z,r))

    return sorted(nanobots, key=lambda n: n.radius, reverse=True)



def count_in_range(nanobot, nanobots):
    return len(list(filter(lambda n: nanobot.distance(n) <= nanobot.radius, nanobots)))



def best_coordinates(nanobots):
    return [0,0,0]
