#!/usr/bin/env python

import unittest
from utils import grid
from utils import max_energy
from utils import partII
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



class TestMaxPower3x3(unittest.TestCase):
    def test18(self):
        power_level = grid(grid_serial_number=18, size=300)
        #print(power_level.T[30:35, 44:49])
        most_power_cell = max_energy(power_level)
        self.assertEqual(most_power_cell.size, 3)
        self.assertEqual(most_power_cell.power, 29)
        self.assertEqual(most_power_cell.coordinates, (33, 45))



class TestMaxPower(unittest.TestCase):
   def test18(self):
        power_level = grid(grid_serial_number=18, size=300)
        most_power_cell = partII(power_level)
        self.assertEqual(most_power_cell.coordinates, (90, 269))
        self.assertEqual(most_power_cell.size, 16)
        self.assertEqual(most_power_cell.power, 113)


   def test119(self):
        power_level = grid(grid_serial_number=42, size=300)
        most_power_cell = partII(power_level)
        self.assertEqual(most_power_cell.coordinates, (232, 251))
        self.assertEqual(most_power_cell.size, 12)
        self.assertEqual(most_power_cell.power, 119)
