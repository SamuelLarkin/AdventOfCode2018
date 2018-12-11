#!/usr/bin/env python

from __future__ import print_function

from utils import grid
from utils import max_energy_coordinates





if __name__ == '__main__':
    power_level = grid(grid_serial_number=1788, size=300)
    coordinates, power = max_energy_coordinates(power_level)
    print('Answer:', coordinates)
    # 235, 35 WRONG
