#!/usr/bin/env python

from __future__ import print_function

from utils import grid
from utils import partII





if __name__ == '__main__':
    power_level = grid(grid_serial_number=1788, size=300)
    coordinates, power, size = partII(power_level)
    print('Answer: {},{},{}'.format(coordinates[0], coordinates[1], size))
    #142,265,7
