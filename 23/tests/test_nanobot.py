import unittest
from nanobot import parse
from nanobot import count_in_range
from nanobot import best_coordinates


test_data = '''
pos=<0,0,0>, r=4
pos=<1,0,0>, r=1
pos=<4,0,0>, r=3
pos=<0,2,0>, r=1
pos=<0,5,0>, r=3
pos=<0,0,3>, r=1
pos=<1,1,1>, r=1
pos=<1,1,2>, r=1
pos=<1,3,1>, r=1
'''
test_data = test_data.split('\n')[1:-1]
assert len(test_data) == 9, len(test_data)


test_data2 = '''
pos=<10,12,12>, r=2
pos=<12,14,12>, r=2
pos=<16,12,12>, r=4
pos=<14,14,14>, r=6
pos=<50,50,50>, r=200
pos=<10,10,10>, r=5
'''
test_data2 = test_data2.split('\n')[1:-1]
assert len(test_data2) == 6, len(test_data2)



class TestNanobot(unittest.TestCase):
    def test1(self):
        nanobots = parse(test_data)
        self.assertEqual(len(nanobots), 9)


    def test_ordered(self):
        nanobots = parse(test_data)
        # TODO have a total test
        self.assertTrue(nanobots[0].radius >= nanobots[1].radius)


    def test_in_range(self):
        nanobots = parse(test_data)
        count = count_in_range(nanobots[0], nanobots)
        self.assertEqual(count, 7)


    def test_best_coordinates(self):
        nanobots = parse(test_data)
        coordinates = best_coordinates(nanobots)
        self.assertListEqual(coordinates, [12,12,12])
        self.assertEqual(best_coordinates(nanobots), 36)
