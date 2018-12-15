import unittest
from game import Game
from utils import read_map


test_data = [
'''
#########
#G..G..G#
#.......#
#.......#
#G..E..G#
#.......#
#.......#
#G..G..G#
#########
''',

'''
#########
#.G...G.#
#...G...#
#...E..G#
#.G.....#
#.......#
#G..G..G#
#.......#
#########
''',

'''
#########
#..G.G..#
#...G...#
#.G.E.G.#
#.......#
#G..G..G#
#.......#
#.......#
#########
''',

'''
#########
#.......#
#..GGG..#
#..GEG..#
#G..G...#
#......G#
#.......#
#.......#
#########
''',
]

test_data = list(map(lambda m: m.split('\n')[1:-1], test_data))
test_data_game_state = [ Game(m,w,p) for m, p, w in map(read_map, test_data) ]


test_data_battle = '''
#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######
'''
test_data_battle = test_data_battle.split('\n')[1:-1]



class TestMove(unittest.TestCase):
    def test0(self):
        game_state = test_data_game_state[0]

        elf = game_state.players[4]
        self.assertEqual(elf.type_, 'E')
        self.assertEqual(elf.position, (4, 4))


    def test1(self):
        game_state = test_data_game_state[0]
        game_state.step()

        elf = game_state.players[3]
        self.assertEqual(elf.type_, 'E')
        self.assertEqual(elf.position, (3, 4))


    def test2(self):
        game_state = test_data_game_state[1]
        game_state.step()

        elf = game_state.players[4]
        self.assertEqual(elf.type_, 'E')
        self.assertEqual(elf.position, (3, 4))


    def test3(self):
        game_state = test_data_game_state[2]
        game_state.step()

        elf = game_state.players[0]
        self.assertEqual(elf.type_, 'G')
        self.assertEqual(elf.position, (2, 3))

        elf = game_state.players[1]
        self.assertEqual(elf.type_, 'G')
        self.assertEqual(elf.position, (2, 4))

        elf = game_state.players[2]
        self.assertEqual(elf.type_, 'G')
        self.assertEqual(elf.position, (2, 5))

        elf = game_state.players[3]
        self.assertEqual(elf.type_, 'G')
        self.assertEqual(elf.position, (3, 3))

        elf = game_state.players[4]
        self.assertEqual(elf.type_, 'E')
        self.assertEqual(elf.position, (3, 4))

        elf = game_state.players[5]
        self.assertEqual(elf.type_, 'G')
        self.assertEqual(elf.position, (3, 5))

        elf = game_state.players[6]
        self.assertEqual(elf.type_, 'G')
        self.assertEqual(elf.position, (4, 1))

        elf = game_state.players[7]
        self.assertEqual(elf.type_, 'G')
        self.assertEqual(elf.position, (4, 4))

        elf = game_state.players[8]
        self.assertEqual(elf.type_, 'G')
        self.assertEqual(elf.position, (5, 7))


    def test_all(self):
        game_state = test_data_game_state[0]
        for _ in range(len(test_data_game_state)-1):
            game_state.step()

        elf = game_state.players[0]
        self.assertEqual(elf.type_, 'G')
        self.assertEqual(elf.position, (2, 3))

        elf = game_state.players[1]
        self.assertEqual(elf.type_, 'G')
        self.assertEqual(elf.position, (2, 4))

        elf = game_state.players[2]
        self.assertEqual(elf.type_, 'G')
        self.assertEqual(elf.position, (2, 5))

        elf = game_state.players[3]
        self.assertEqual(elf.type_, 'G')
        self.assertEqual(elf.position, (3, 3))

        elf = game_state.players[4]
        self.assertEqual(elf.type_, 'E')
        self.assertEqual(elf.position, (3, 4))

        elf = game_state.players[5]
        self.assertEqual(elf.type_, 'G')
        self.assertEqual(elf.position, (3, 5))

        elf = game_state.players[6]
        self.assertEqual(elf.type_, 'G')
        self.assertEqual(elf.position, (4, 1))

        elf = game_state.players[7]
        self.assertEqual(elf.type_, 'G')
        self.assertEqual(elf.position, (4, 4))

        elf = game_state.players[8]
        self.assertEqual(elf.type_, 'G')
        self.assertEqual(elf.position, (5, 7))




class TestBattle(unittest.TestCase):
    def test1(self):
        '''
        #######
        #..G..#   G(200)
        #...EG#   E(197), G(197)
        #.#G#G#   G(200), G(197)
        #...#E#   E(197)
        #.....#
        #######
        '''
        m, p, w = read_map(test_data_battle)
        game = Game(m,w,p)
        for _ in range(1):
            game.step()
        game.display()
        print(game)

        self.assertEqual(game.players[0].hit_point, 200)
        self.assertEqual(game.players[1].hit_point, 197)
        self.assertEqual(game.players[2].hit_point, 197)
        self.assertEqual(game.players[3].hit_point, 200)
        self.assertEqual(game.players[4].hit_point, 197)
        self.assertEqual(game.players[5].hit_point, 197)


    def test2(self):
        '''
        #######
        #...G.#   G(200)
        #..GEG#   G(200), E(188), G(194)
        #.#.#G#   G(194)
        #...#E#   E(194)
        #.....#
        #######
        '''
        m, p, w = read_map(test_data_battle)
        game = Game(m,w,p)
        for _ in range(2):
            game.step()
        game.display()
        print(game)

        self.assertEqual(game.players[0].hit_point, 200)
        self.assertEqual(game.players[1].hit_point, 200)
        self.assertEqual(game.players[2].hit_point, 188)
        self.assertEqual(game.players[3].hit_point, 194)
        self.assertEqual(game.players[4].hit_point, 194)
        self.assertEqual(game.players[5].hit_point, 194)


    def test23(self):
        '''
        After 23 rounds:
        #######
        #...G.#   G(200)
        #..G.G#   G(200), G(131)
        #.#.#G#   G(131)
        #...#E#   E(131)
        #.....#
        #######
        '''
        m, p, w = read_map(test_data_battle)
        game = Game(m,w,p)
        for _ in range(23):
            game.step()
        game.display()
        print(game)

        self.assertEqual(len(game.players), 5)
        self.assertEqual(game.players[0].hit_point, 200)
        self.assertEqual(game.players[1].hit_point, 200)
        self.assertEqual(game.players[2].hit_point, 131)
        self.assertEqual(game.players[3].hit_point, 131)
        self.assertEqual(game.players[4].hit_point, 131)


    def test27pre(self):
        '''
        #######
        #G....#   G(200)
        #.G...#   G(131)
        #.#.#G#   G(119)
        #...#E#   E(119)
        #...G.#   G(200)
        #######
        '''
        m, p, w = read_map(test_data_battle)
        game = Game(m,w,p)
        for step in range(22):
            print(step)
            game.step()

        for i in range(5):
            print(step+i)
            game.step()
            game.display()

        self.assertEqual(len(game.players), 5)
        self.assertEqual(game.players[0].hit_point, 200)
        self.assertEqual(game.players[1].hit_point, 131)
        self.assertEqual(game.players[2].hit_point, 119)
        self.assertEqual(game.players[3].hit_point, 119)
        self.assertEqual(game.players[4].hit_point, 200)


    def test27(self):
        '''
        #######
        #G....#   G(200)
        #.G...#   G(131)
        #.#.#G#   G(119)
        #...#E#   E(119)
        #...G.#   G(200)
        #######
        '''
        m, p, w = read_map(test_data_battle)
        game = Game(m,w,p)
        for step in range(27):
            print(step)
            game.step()
        game.display()
        print(game)

        self.assertEqual(len(game.players), 5)
        self.assertEqual(game.players[0].hit_point, 200)
        self.assertEqual(game.players[1].hit_point, 131)
        self.assertEqual(game.players[2].hit_point, 119)
        self.assertEqual(game.players[3].hit_point, 119)
        self.assertEqual(game.players[4].hit_point, 200)
        self.assertFalse(game.done())


    def test47(self):
        '''
        #######
        #G....#   G(200)
        #.G...#   G(131)
        #.#.#G#   G(59)
        #...#.#
        #....G#   G(200)
        #######
        '''
        m, p, w = read_map(test_data_battle)
        game = Game(m,w,p)
        for step in range(47):
            print(step)
            game.step()
        game.display()
        print(game)

        self.assertEqual(len(game.players), 4)
        self.assertEqual(game.players[0].hit_point, 200)
        self.assertEqual(game.players[1].hit_point, 131)
        self.assertEqual(game.players[2].hit_point, 59)
        self.assertEqual(game.players[3].hit_point, 200)
        self.assertTrue(game.done())



class TestCombat(unittest.TestCase):
    def test1(self):
        '''
        #######       #######
        #G..#E#       #...#E#   E(200)
        #E#E.E#       #E#...#   E(197)
        #G.##.#  -->  #.E##.#   E(185)
        #...#E#       #E..#E#   E(200), E(200)
        #...E.#       #.....#
        #######       #######

        Combat ends after 37 full rounds
        Elves win with 982 total hit points left
        Outcome: 37 * 982 = 36334
        '''
        initial_data = '''
        #######
        #G..#E#
        #E#E.E#
        #G.##.#
        #...#E#
        #...E.#
        #######
        '''
        m,p,w = read_map(initial_data.split('\n')[1:-1])
        game = Game(m,w,p)
        step, score = game.combat()
        print(step, game)
        game.display()
        self.assertEqual(step, 37)
        self.assertEqual(score, 36334)


    def test2(self):
        '''
        #######       #######
        #E..EG#       #.E.E.#   E(164), E(197)
        #.#G.E#       #.#E..#   E(200)
        #E.##E#  -->  #E.##.#   E(98)
        #G..#.#       #.E.#.#   E(200)
        #..E#.#       #...#.#
        #######       #######

        Combat ends after 46 full rounds
        Elves win with 859 total hit points left
        Outcome: 46 * 859 = 39514
        '''
        initial_data = '''
        #######
        #E..EG#
        #.#G.E#
        #E.##E#
        #G..#.#
        #..E#.#
        #######
        '''
        m,p,w = read_map(initial_data.split('\n')[1:-1])
        game = Game(m,w,p)
        step, score = game.combat()
        print(step, game)
        game.display()
        self.assertEqual(step, 46)
        self.assertEqual(score, 39514)


    def test3(self):
        '''
        #######       #######
        #E.G#.#       #G.G#.#   G(200), G(98)
        #.#G..#       #.#G..#   G(200)
        #G.#.G#  -->  #..#..#
        #G..#.#       #...#G#   G(95)
        #...E.#       #...G.#   G(200)
        #######       #######

        Combat ends after 35 full rounds
        Goblins win with 793 total hit points left
        Outcome: 35 * 793 = 27755
        '''
        initial_data = '''
        #######
        #E.G#.#
        #.#G..#
        #G.#.G#
        #G..#.#
        #...E.#
        #######
        '''
        m,p,w = read_map(initial_data.split('\n')[1:-1])
        game = Game(m,w,p)
        step, score = game.combat()
        print(step, game)
        game.display()
        self.assertEqual(step, 35)
        self.assertEqual(score, 27755)



    def test4(self):
        '''
        #######       #######
        #.E...#       #.....#
        #.#..G#       #.#G..#   G(200)
        #.###.#  -->  #.###.#
        #E#G#G#       #.#.#.#
        #...#G#       #G.G#G#   G(98), G(38), G(200)
        #######       #######

        Combat ends after 54 full rounds
        Goblins win with 536 total hit points left
        Outcome: 54 * 536 = 28944
        '''
        initial_data = '''
        #######
        #.E...#
        #.#..G#
        #.###.#
        #E#G#G#
        #...#G#
        #######
        '''
        m,p,w = read_map(initial_data.split('\n')[1:-1])
        game = Game(m,w,p)
        step, score = game.combat()
        print(step, game)
        game.display()
        self.assertEqual(step, 54)
        self.assertEqual(score, 28944)


    def test5(self):
        '''
        #########       #########
        #G......#       #.G.....#   G(137)
        #.E.#...#       #G.G#...#   G(200), G(200)
        #..##..G#       #.G##...#   G(200)
        #...##..#  -->  #...##..#
        #...#...#       #.G.#...#   G(200)
        #.G...G.#       #.......#
        #.....G.#       #.......#
        #########       #########

        Combat ends after 20 full rounds
        Goblins win with 937 total hit points left
        Outcome: 20 * 937 = 18740
        '''
        initial_data = '''
        #########
        #G......#
        #.E.#...#
        #..##..G#
        #...##..#
        #...#...#
        #.G...G.#
        #.....G.#
        #########
        '''
        m,p,w = read_map(initial_data.split('\n')[1:-1])
        game = Game(m,w,p)
        step, score = game.combat()
        print(step, game)
        game.display()
        self.assertEqual(step, 20)
        self.assertEqual(score, 18740)
