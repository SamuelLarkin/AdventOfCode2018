import unittest
from cave import create_cave
from cave import risk_level
from cave import display_cave
from cave import rescue_target
from cave import rescue_target2
from cave import SearchPosition
from cave import Tool



class TestCave(unittest.TestCase):
    def test1(self):
        cave = create_cave(510, (10,10))
        #display_cave(cave)
        area = cave[1,1]
        #print(area)
        self.assertEqual(area.coordinates, (1,1))
        self.assertEqual(area.depth, 510)
        self.assertEqual(area.geologic_index, 145722555)
        self.assertEqual(area.erosion_level, 1805)
        self.assertEqual(area.type.value-1, 2)


    def test2(self):
        cave = create_cave(510, (10,10))
        #display_cave(cave)
        self.assertEqual(risk_level(cave), 114)


    def test3(self):
        cave = create_cave(510, (10,10), 5)
        display_cave(cave)


    def test_compare_SearchPosition(self):
        a = SearchPosition((0,0), Tool.torch, 7)
        b = SearchPosition((10,10), Tool.torch, 2)
        print(a)
        print(b)
        self.assertTrue(a > b)
        self.assertFalse(a < b)


    def test_rescue1(self):
        target = (10, 10)
        cave = create_cave(510, target, 46)
        #display_cave(cave)
        cost = rescue_target(cave, target)
        self.assertEqual(cost, 45)


    def test_rescue2(self):
        target = (10, 10)
        cave = create_cave(510, target, 46)
        #display_cave(cave)
        cost = rescue_target2(cave, target)
        self.assertEqual(cost, 45)





if __name__ == '__main__':
    a = SearchPosition((0,0), Tool.torch, 7)
    b = SearchPosition((10,10), Tool.torch, 2)
    a < b
    a > b
    target = (10, 10)
    cave = create_cave(510, target, 16)
    print(cave[0,0])
    display_cave(cave)
    cost = rescue_target(cave, target)
