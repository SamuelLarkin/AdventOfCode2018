import unittest
import numpy as np
from utils import grow_generation
from utils import grow
from utils import parse


test_data = [
        'initial state: #..#.#..##......###...###',
        '',
        '...## => #',
        '..#.. => #',
        '.#... => #',
        '.#.#. => #',
        '.#.## => #',
        '.##.. => #',
        '.#### => #',
        '#.#.# => #',
        '#.### => #',
        '##.#. => #',
        '##.## => #',
        '###.. => #',
        '###.# => #',
        '####. => #',
        ]

generation_ref = [
        '...#..#.#..##......###...###...........', 
        '...#...#....#.....#..#..#..#...........', 
        '...##..##...##....#..#..#..##..........', 
        '..#.#...#..#.#....#..#..#...#..........', 
        '...#.#..#...#.#...#..#..##..##.........', 
        '....#...##...#.#..#..#...#...#.........', 
        '....##.#.#....#...#..##..##..##........', 
        '...#..###.#...##..#...#...#...#........', 
        '...#....##.#.#.#..##..##..##..##.......', 
        '...##..#..#####....#...#...#...#.......', 
        '..#.#..#...#.##....##..##..##..##......', 
        '...#...##...#.#...#.#...#...#...#......', 
        '...##.#.#....#.#...#.#..##..##..##.....', 
        '..#..###.#....#.#...#....#...#...#.....', 
        '..#....##.#....#.#..##...##..##..##....', 
        '..##..#..#.#....#....#..#.#...#...#....', 
        '.#.#..#...#.#...##...#...#.#..##..##...', 
        '..#...##...#.#.#.#...##...#....#...#...', 
        '..##.#.#....#####.#.#.#...##...##..##..', 
        '.#..###.#..#.#.#######.#.#.#..#.#...#..', 
        '.#....##....#####...#######....#.#..##.', 
        ]




class TestParse(unittest.TestCase):
    def test_initial_state(self):
        initial_state, rules = parse(test_data)
        print(initial_state)
        print(rules)
        # NOTE: We will have to extend indefinetely on both sides.
        # 0: ...#..#.#..##......###...###...........
        # 0: ..#..#.#..##......###...###..
        ref = '...#..#.#..##......###...###...........'
        self.assertEqual(len(initial_state), len(ref))
        self.assertTrue(np.all(initial_state == ref))



class TestGenerator(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestGenerator, self).__init__(*args, **kwargs)
        initial_state, self.rules = parse(test_data)
        self.initial_state = '.'*3 + initial_state + '.'*11


    def test_generation1(self):
        # 1: ...#...#....#.....#..#..#..#...........
        n = 1
        generation = grow_generation(self.initial_state, self.rules, n)
        self.assertTrue(np.all(generation == generation_ref[n]), '\nout: {}\nref: {}'.format(generation, generation_ref[n]))


    def test_generation5(self):
        # 5: ....#...##...#.#..#..#...#...#.........
        n = 5
        generation = grow_generation(self.initial_state, self.rules, n)
        self.assertTrue(np.all(generation == generation_ref[n]), '\nout: {}\nref: {}'.format(generation, generation_ref[n]))


    def test_generation10(self):
        # 10: ..#.#..#...#.##....##..##..##..##......
        n = 10
        generation = grow_generation(self.initial_state, self.rules, n)
        self.assertTrue(np.all(generation == generation_ref[n]), '\nout: {}\nref: {}'.format(generation, generation_ref[n]))


    def test_generation15(self):
        # 15: ..##..#..#.#....#....#..#.#...#...#....
        n = 15
        generation = grow_generation(self.initial_state, self.rules, n)
        self.assertTrue(np.all(generation == generation_ref[n]), '\nout: {}\nref: {}'.format(generation, generation_ref[n]))


    def test_generation20(self):
        # 20: .#....##....#####...#######....#.#..##.
        n = 20
        generation = grow_generation(self.initial_state, self.rules, n)
        self.assertTrue(np.all(generation == generation_ref[n]), '\nout: {}\nref: {}'.format(generation, generation_ref[n]))


    def test_generation(self):
        generation = self.initial_state
        for n in range(20):
            generation = grow(generation, self.rules)
            self.assertTrue(np.all(generation == generation_ref[n+1]), '\n{}\nout: {}\nref: {}'.format(n+1, generation, generation_ref[n]))
