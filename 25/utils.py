import numpy as np



def manhattan_distance_all(stars):
    a = np.expand_dims(stars, axis=0)
    b = np.expand_dims(stars, axis=1)
    return np.sum(np.abs(a-b), axis=2)



def find_constellations(distances):
    closest = []
    for row in distances:
        closest.append(set(map(lambda a: a[0], filter(lambda d: d[1]<=3, enumerate(row)))))

    def helper(a, closest):
        c = set(a)
        for b in a:
            c |= closest[b]
        if len(c) == len(a):
            return c
        else:
            return helper(c, closest)

    return set(frozenset(helper(a, closest)) for a in closest)



def find_constellations2(distances):
    closest = []
    for row in distances:
        closest.append(set(map(lambda a: a[0], filter(lambda d: d[1]<=3, enumerate(row)))))

    i = 0
    while i < len(closest):
        ref = closest.pop(i)
        next_loop = [ref]
        for other in closest:
            if ref & other:
                ref |= other
            else:
                next_loop.append(other)
        closest = next_loop
        i += 1

    return closest
