import unittest
from partII import Cube



class TestCube(unittest.TestCase):
    def test_iter(self):
        '''
        '''
        cube = Cube(0,0,0,16)
        cubeit = iter(cube)

        #Cube(x1=0, y1=0, z1=0, s=8)
        subcube = next(cubeit)
        self.assertEqual(subcube.x1, 0)
        self.assertEqual(subcube.y1, 0)
        self.assertEqual(subcube.z1, 0)
        self.assertEqual(subcube.s, 8)

        #Cube(x1=0, y1=0, z1=8, s=8)
        subcube = next(cubeit)
        self.assertEqual(subcube.x1, 0)
        self.assertEqual(subcube.y1, 0)
        self.assertEqual(subcube.z1, 8)
        self.assertEqual(subcube.s, 8)

        #Cube(x1=0, y1=8, z1=0, s=8)
        subcube = next(cubeit)
        self.assertEqual(subcube.x1, 0)
        self.assertEqual(subcube.y1, 8)
        self.assertEqual(subcube.z1, 0)
        self.assertEqual(subcube.s, 8)

        #Cube(x1=0, y1=8, z1=8, s=8)
        subcube = next(cubeit)
        self.assertEqual(subcube.x1, 0)
        self.assertEqual(subcube.y1, 8)
        self.assertEqual(subcube.z1, 8)
        self.assertEqual(subcube.s, 8)

        #Cube(x1=8, y1=0, z1=0, s=8)
        subcube = next(cubeit)
        self.assertEqual(subcube.x1, 8)
        self.assertEqual(subcube.y1, 0)
        self.assertEqual(subcube.z1, 0)
        self.assertEqual(subcube.s, 8)

        #Cube(x1=8, y1=0, z1=8, s=8)
        subcube = next(cubeit)
        self.assertEqual(subcube.x1, 8)
        self.assertEqual(subcube.y1, 0)
        self.assertEqual(subcube.z1, 8)
        self.assertEqual(subcube.s, 8)

        #Cube(x1=8, y1=8, z1=0, s=8)
        subcube = next(cubeit)
        self.assertEqual(subcube.x1, 8)
        self.assertEqual(subcube.y1, 8)
        self.assertEqual(subcube.z1, 0)
        self.assertEqual(subcube.s, 8)

        #Cube(x1=8, y1=8, z1=8, s=8)
        subcube = next(cubeit)
        self.assertEqual(subcube.x1, 8)
        self.assertEqual(subcube.y1, 8)
        self.assertEqual(subcube.z1, 8)
        self.assertEqual(subcube.s, 8)

        with self.assertRaises(StopIteration):
            next(cubeit)
