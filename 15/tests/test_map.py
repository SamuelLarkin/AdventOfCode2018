import unittest
from utils import read_map


class TestReadMap(unittest.TestCase):
    def test1(self):
        test_data = '''
        #######
        #.G.E.#
        #E.G.E#
        #.G.E.#
        #######
        '''
        test_data = test_data.split('\n')[1:-1]
        map_, players, walls = read_map(test_data)

        self.assertEqual(map_[0][0], '#')
        self.assertEqual(map_[1][2], 'G')
        self.assertEqual(map_[2][5], 'E')

        self.assertEqual(len(players), 7)

        self.assertEqual(players[5].type_, 'G')
        self.assertEqual(players[5].position, (3,2))

        self.assertEqual(players[1].type_, 'E')
        self.assertEqual(players[1].position, (1,4))
