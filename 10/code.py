#!/usr/bin/env python

from __future__ import print_function

from utils import test_data
from utils import parse
from tqdm import trange
import matplotlib.pyplot as plt
import time
import numpy as np
from collections import namedtuple


Frame = namedtuple('Frame', ('area', 'coordinates', 'elapased_time'))

def area(positions):
    sizes = np.amax(positions, axis=0) - np.amin(positions, axis=0)
    return sizes[0] * sizes[1]


if __name__ == '__main__':
    debug = False

    with open('data.txt', 'r') as f:
        positions, velocities = parse(f)
        max_iter = int(2e4)

    if debug:
        positions, velocities = parse(test_data)
        max_iter = int(1e1)

    print('positions:', positions)
    print('velocities:', velocities)
    least_area = Frame(area(positions), positions, 0)
    for i in trange(1, max_iter):
        positions = positions + velocities
        least_area = min(least_area, Frame(area(positions), positions, i), key=lambda x: x.area)

    print('min:', least_area)
    fig, ax = plt.subplots()
    ax.scatter(least_area.coordinates[:,0], -least_area.coordinates[:,1])
    plt.show()

    print('Answer II:', least_area.elapased_time)

    # part I:
    # PANLPAPR

    # part II:
    # 10304
