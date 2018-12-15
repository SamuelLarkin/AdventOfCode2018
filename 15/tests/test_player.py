import unittest
from player import Player
from utils import read_map



test_data = '''
#######
#.G.E.#
#E.G.E#
#.G.E.#
#######
'''
test_data = test_data.split('\n')[1:-1]

# Targets:      In range:     Reachable:    Nearest:      Chosen:
# #######       #######       #######       #######       #######
# #E..G.#       #E.?G?#       #E.@G.#       #E.!G.#       #E.+G.#
# #...#.#  -->  #.?.#?#  -->  #.@.#.#  -->  #.!.#.#  -->  #...#.#
# #.G.#G#       #?G?#G#       #@G@#G#       #!G.#G#       #.G.#G#
# #######       #######       #######       #######       #######
test_data_chosen = '''
#######
#E..G.#
#...#.#
#.G.#G#
####### 
'''
test_data_chosen = test_data_chosen.split('\n')[1:-1]

# In range:     Nearest:      Chosen:       Distance:     Step:
# #######       #######       #######       #######       #######
# #.E...#       #.E...#       #.E...#       #4E212#       #..E..#
# #...?.#  -->  #...!.#  -->  #...+.#  -->  #32101#  -->  #.....#
# #..?G?#       #..!G.#       #...G.#       #432G2#       #...G.#
# #######       #######       #######       #######       #######
test_data_step = '''
#######
#.E...#
#.....#
#...G.#
#######
'''
test_data_step = test_data_step.split('\n')[1:-1]



class TestPlayer(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestPlayer, self).__init__(*args, **kwargs)

    def test_adjacent(self):
        """
        all players always have 4 adjacent cells which doesn't me they are reachable
        """
        map_, players, walls = read_map(test_data)

        player = players[1]
        print(player)
        self.assertEqual(len(player.adjacent), 4)

        player = players[3]
        self.assertEqual(len(player.adjacent), 4)


    def test_find_in_range(self):
        map_, players, walls = read_map(test_data)

        player = players[1]
        player.find_in_range(walls, players)
        self.assertListEqual(player.in_range, [(1,3),(1,5),(2,4)])

        player = players[3]
        player.find_in_range(walls, players)
        self.assertListEqual(player.in_range, [(1, 3), (2, 2), (2, 4), (3, 3)])


    def test_find_in_range2(self):
        """
        Targets:      In range:     Reachable:    Nearest:      Chosen:
        #######       #######       #######       #######       #######
        #E..G.#       #E.?G?#       #E.@G.#       #E.!G.#       #E.+G.#
        #...#.#  -->  #.?.#?#  -->  #.@.#.#  -->  #.!.#.#  -->  #...#.#
        #.G.#G#       #?G?#G#       #@G@#G#       #!G.#G#       #.G.#G#
        #######       #######       #######       #######       #######
        """
        map_, players, walls = read_map(test_data_chosen)

        player = players[1]
        player.find_in_range(walls, players)
        self.assertEqual(len(player.in_range), 2)
        self.assertListEqual(player.in_range, [(1,3),(1,5)])

        player = players[2]
        player.find_in_range(walls, players)
        self.assertEqual(len(player.in_range), 3)
        self.assertListEqual(player.in_range, [(2, 2), (3, 1), (3, 3)])

        player = players[3]
        player.find_in_range(walls, players)
        self.assertEqual(len(player.in_range), 1)
        self.assertListEqual(player.in_range, [(2, 5)])


    def test_distance(self):
        """
        Targets:      In range:     Reachable:    Nearest:      Chosen:
        #######       #######       #######       #######       #######
        #E..G.#       #E.?G?#       #E.@G.#       #E.!G.#       #E.+G.#
        #...#.#  -->  #.?.#?#  -->  #.@.#.#  -->  #.!.#.#  -->  #...#.#
        #.G.#G#       #?G?#G#       #@G@#G#       #!G.#G#       #.G.#G#
        #######       #######       #######       #######       #######
        """
        map_, players, walls = read_map(test_data_chosen)

        player = players[0]
        distance = player.calculate_reachable_bfs(map_, walls, players)
        print(distance)


    def test_chosen(self):
        """
        Targets:      In range:     Reachable:    Nearest:      Chosen:
        #######       #######       #######       #######       #######
        #E..G.#       #E.?G?#       #E.@G.#       #E.!G.#       #E.+G.#
        #...#.#  -->  #.?.#?#  -->  #.@.#.#  -->  #.!.#.#  -->  #...#.#
        #.G.#G#       #?G?#G#       #@G@#G#       #!G.#G#       #.G.#G#
        #######       #######       #######       #######       #######
        """
        map_, players, walls = read_map(test_data_chosen)

        player = players[0]
        distance, chosen = player.chosen(map_, walls, players)
        self.assertEqual(distance, 2)
        self.assertEqual(chosen, (1,3))


    def test_step(self):
        """
        In range:     Nearest:      Chosen:       Distance:     Step:
        #######       #######       #######       #######       #######
        #.E...#       #.E...#       #.E...#       #4E212#       #..E..#
        #...?.#  -->  #...!.#  -->  #...+.#  -->  #32101#  -->  #.....#
        #..?G?#       #..!G.#       #...G.#       #432G2#       #...G.#
        #######       #######       #######       #######       #######
        """
        map_, players, walls = read_map(test_data_step)

        player = players[0]
        distances = player.step(map_, walls, players)
        print(distances)
        self.assertEqual(player.position, (1,3))
