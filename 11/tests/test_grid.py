#!/usr/bin/env python

import unittest
from utils import grid
from utils import max_energy_coordinates
import numpy as np

np.set_printoptions(linewidth=400)


class TestGrid(unittest.TestCase):
    def test8(self):
        power_level = grid(grid_serial_number=8, size=10)
        self.assertEqual(power_level[3-1,5-1], 4)


    def test57(self):
        power_level = grid(grid_serial_number=57, size=200)
        self.assertEqual(power_level[122-1,79-1], -5)


    def test39(self):
        power_level = grid(grid_serial_number=39, size=300)
        self.assertEqual(power_level[217-1,196-1], 0)


    def test71(self):
        power_level = grid(grid_serial_number=71, size=200)
        self.assertEqual(power_level[101-1,153-1], 4)


    def test18(self):
        power_level = grid(grid_serial_number=18, size=300)
        #print(power_level.T[30:35, 44:49])
        ind, power = max_energy_coordinates(power_level)
        self.assertEqual(power, 29)
        self.assertAlmostEqual(ind, (33, 45))
