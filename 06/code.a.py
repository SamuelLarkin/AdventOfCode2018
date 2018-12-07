#!/usr/bin/env python

from __future__ import print_function

from coordinates import get_coordinates
from coordinates import calculate_distances
from coordinates import get_mask_equidistant
from coordinates import find_id_of_infinite_area
from collections import Counter
import numpy as np

np.set_printoptions(linewidth=100)



if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        coordinates = get_coordinates(f)

    debug = False
    if debug:
        from coordinates import test_data
        coordinates = get_coordinates(test_data)

    # coordinates.shape = (#coords, 2)

    distance = calculate_distances(coordinates)
    # distance.shape == (#coords, x_max, y_min)

    # https://stackoverflow.com/questions/46706426/changing-values-on-the-edges-of-an-array-in-numpy
    areas = np.argmin(distance, axis=0)
    # areas.shape = (x_max, y_max)

    # Remove coordinates that are share by two groups
    mask = get_mask_equidistant(distance)
    # mask.shape = (x_max, y_max)
    # for a given coordinate on the grid, is there more than one point that is at equi-distance?
    # If so, this grid coordinate cannot be part of any group.
    areas[mask] = -2

    # Remove areas that touch the border
    for v in find_id_of_infinite_area(areas):
        areas[areas == v] = -3
    #print('removed border areas:', areas)

    # Remove infinite and neutral areas before counting the superficie of each area.
    area_superficie = Counter(areas[areas >= 0].ravel().tolist())
    print('area_superficie:', area_superficie)
    answer = area_superficie.most_common(1)[0][1]

    print('Answer:', answer)
    # 3276
