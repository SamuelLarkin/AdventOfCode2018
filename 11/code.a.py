#!/usr/bin/env python

from __future__ import print_function

from utils import grid
from utils import max_energy





if __name__ == '__main__':
    power_level = grid(grid_serial_number=1788, size=300)
    coordinates, power = max_energy(power_level)
    print('Answer: {},{}'.format(coordinates[0], coordinates[1]))
    # Who would've thought that spaces would skrew the result?!
    #235,35
