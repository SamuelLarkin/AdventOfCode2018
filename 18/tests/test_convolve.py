import unittest
from utils import convolve
from utils import reader
from utils import step
from .timelapse import timelapse

import numpy as np



class TestStep(unittest.TestCase):
    def test1(self):
        acres = reader(timelapse[0]) 
        new_acres = convolve(acres)
        new_acres_ref = reader(timelapse[1])
        self.assertTrue(np.all(new_acres == new_acres_ref))


    def test2(self):
        acres = reader(timelapse[1]) 
        new_acres = convolve(acres)
        new_acres_ref = reader(timelapse[2])
        self.assertTrue(np.all(new_acres == new_acres_ref))


    def test_final(self):
        new_acres = reader(timelapse[0]) 
        for _ in range(10):
            new_acres = convolve(new_acres)
        new_acres_ref = reader(timelapse[10])
        self.assertTrue(np.all(new_acres == new_acres_ref))
