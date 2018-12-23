from collections import namedtuple
import re

NanobotBase = namedtuple('NanobotBase', ('x', 'y', 'z', 'radius'))
class Nanobot(NanobotBase):
    @property
    def c(self):
        return (self.x, self.y, self.z)


    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)


    def count_in_range(self, nanobots):
        return count_in_range(self, nanobots)



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
    #if nanobot is not instanceof(Nanobot):
    #    nanobot = Nanobot(nanobot[0], nanobot[1], nanobot[2], 0)
    return len(list(filter(lambda n: nanobot.distance(n) <= nanobot.radius, nanobots)))



def sphere_intersection(n1, n2):
    # [Circle-Circle Intersection](http://mathworld.wolfram.com/Circle-CircleIntersection.html)
    # [Sphere-Sphere Intersection](http://mathworld.wolfram.com/Sphere-SphereIntersection.html)
    '''
    x = 'frac{d^2 - r^2 + R^2}{2d}
    '''
    d = n2.distance(n1)
    r = n2.r
    R = n1.r
    x = (d**2 - r**2 + R**2) / (2 * d)



def move(c, d):
    return [c[0]+d[0], c[1]+d[1], c[2]+d[2]]



def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])



def best_coordinates(nanobots):
    import heapq
    from itertools import product
    # Best Values
    me = Nanobot(0,0,0,0)
    distance = 0  # distance from current location
    num_in_range = 0

    # PROBLEM heapq is a minimal queue and not a maximum num_in_range!
    heap = [(num_in_range, distance, me)]
    while heap:
        num_in_range, distance, me = heapq.heappop(heap)
        for d in product((-1, 0, 1), repeat=3):
            new_me = Nanobot(*move(me.c, d), 0)
            new_distance = sum(me.distance(n) for n in nanobots) / len(nanobots)
            new_num_in_range = new_me.count_in_range(nanobots)
            if new_num_in_range >= num_in_range:
                heapq.heappush(heap, (new_num_in_range, new_distance, new_me))
                if new_num_in_range > num_in_range:
                    num_in_range = new_num_in_range
                    distance = new_distance
                    me = new_me

    return num_in_range, distance, list(me.c)


def mse(nanobots):
    import numpy as np
    coordinates = np.asarray([[n.x,n.y,n.z] for n in nanobots], dtype=np.int)
    # coordinates.shape = (#nanobots, 3)
    radius = np.asarray([n.radius for n in nanobots], dtype=np.int)
    # radius.shape = (#nanobots, )
    me = np.asarray([12,12,12], dtype=np.int)
    # me.shape = (3, )
    me = np.expand_dims(me, axis=0)
    # me.shape = (1, 3)
    distances = np.sum(np.abs(coordinates- me), axis=1)
    # distances.shape = (#nanobots,)
    t = radius - distances.T
    in_range = np.sum((t>0).astype(np.int))
    # in_range.shape = ()
    dist = np.sum(np.abs(me))
    # dist.shape = ()

    loss = -in_range - dist

    print (coordinates)
    print (radius)
    print(distances)
    print(t)
    print(in_range)
    print(loss)

    import torch
    from torch.autograd import Variable

    coordinates = Variable(torch.Tensor(coordinates))
    radius = Variable(torch.Tensor(radius))
    me = Variable(torch.Tensor(me), requires_grad=True)
    for t in range(10):
        distances = (coordinates - me).abs().sum(1)
        t = radius - distances
        in_range = (t > 0).sum()
        dist = me.abs().sum()
        loss = -in_range - dist - distances.mean()
        print('loss:', loss)
        loss.backward()
        print(distances)
        print(t)
        print(in_range)
        print(dist)
        print('me:', me)
        print(me.grad.data)
        me.data -= torch.round(me.grad.data)
        me.grad.data.zero_()
