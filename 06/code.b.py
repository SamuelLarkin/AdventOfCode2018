#!/usr/bin/env python

from __future__ import print_function

from coordinates import get_coordinates
from coordinates import calculate_distances
import numpy as np
np.set_printoptions(linewidth=100)





if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        coordinates = get_coordinates(f)
        part_2_max = 10000

    debug = False
    if debug:
        from coordinates import test_data
        coordinates = get_coordinates(test_data)
        part_2_max = 32

    # coordinates.shape = (#coords, 2)

    distance = calculate_distances(coordinates)
    # distance.shape == (#coords, x_max, y_min)

    if debug:
        # This should yield the answer from the example on AoC.
        print(distance[:,4,3])

    cumulative_distance = np.sum(distance, axis=0)
    # cumulative_distance.shape = (x_max, y_max)

    print(cumulative_distance)
    coordinates_within_constraint = np.argwhere(cumulative_distance < part_2_max)
    print('np.argwhere:', coordinates_within_constraint)

    answer = len(coordinates_within_constraint)
    print('Answer:', answer)
    # 38380 
