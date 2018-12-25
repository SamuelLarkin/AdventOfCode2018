import numpy as np



def parse(f):
    return np.asarray([list(map(int, l.strip().split(','))) for l in f], dtype=np.int)
