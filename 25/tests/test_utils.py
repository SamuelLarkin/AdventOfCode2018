import unittest
from reader import parse
from utils import manhattan_distance_all
from utils import find_constellations


test_data = [
'''
0,0,0,0
3,0,0,0
0,3,0,0
0,0,3,0
0,0,0,3
0,0,0,6
9,0,0,0
12,0,0,0
''',
'''
-1,2,2,0
0,0,2,-2
0,0,0,-2
-1,2,0,0
-2,-2,-2,2
3,0,2,-1
-1,3,2,2
-1,0,-1,0
0,2,1,-2
3,0,0,0
''',
'''
1,-1,0,1
2,0,-1,0
3,2,-1,0
0,0,3,1
0,0,-1,-1
2,3,-2,0
-2,2,0,0
2,-2,0,-1
1,-1,0,-1
3,2,0,2
''',
'''
1,-1,-1,-2
-2,-2,0,1
0,2,1,3
-2,3,-2,1
0,2,3,-2
-1,-1,1,-2
0,-2,-1,0
-2,2,3,-1
1,2,2,0
-1,-2,0,-2
''',
]
test_data = [d.strip().split('\n') for d in test_data]
assert len(test_data) == 4
assert len(test_data[0]) == 8
test_data = list(zip(test_data, (2,4,3,8)))


class TestReader(unittest.TestCase):
    def test1(self):
        data, num_constellation = test_data[0]
        stars = parse(data)
        self.assertEqual(stars.shape, (8, 4))



class TestManhattanDistance(unittest.TestCase):
    def test0(self):
        data, num_constellation = test_data[0]
        stars = parse(data)
        distance = manhattan_distance_all(stars)
        constellations = find_constellations(distance)
        print(constellations)
        self.assertEqual(len(constellations), num_constellation)


    def test1(self):
        data, num_constellation = test_data[1]
        stars = parse(data)
        distance = manhattan_distance_all(stars)
        constellations = find_constellations(distance)
        self.assertEqual(len(constellations), num_constellation)


    def test2(self):
        data, num_constellation = test_data[2]
        stars = parse(data)
        distance = manhattan_distance_all(stars)
        constellations = find_constellations(distance)
        self.assertEqual(len(constellations), num_constellation)


    def test3(self):
        data, num_constellation = test_data[3]
        stars = parse(data)
        distance = manhattan_distance_all(stars)
        constellations = find_constellations(distance)
        self.assertEqual(len(constellations), num_constellation)
