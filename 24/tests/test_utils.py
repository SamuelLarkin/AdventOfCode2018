import unittest
from utils import parse_army
from utils import parse_group
from utils import Attack
from utils import combat




class TestParseDesc(unittest.TestCase):
    def test_none(self):
        g = parse_group('test_none', '2702 units each with 10159 hit points with an attack that does 7 fire damage at initiative 7')

        self.assertEqual(g.num_units, 2702)
        self.assertEqual(g.hit_points, 10159)
        self.assertEqual(g.attack_damage, 7)
        self.assertEqual(g.initiative, 7)
        self.assertSetEqual(g.weak_to, set())
        self.assertSetEqual(g.immune_to, set())
        self.assertEqual(g.effective_power, 2702*7)


    def test_weak(self):
        g = parse_group('test_weak', '2785 units each with 4474 hit points (weak to cold) with an attack that does 14 fire damage at initiative 20')

        self.assertEqual(g.num_units, 2785)
        self.assertEqual(g.hit_points, 4474)
        self.assertEqual(g.attack_damage, 14)
        self.assertEqual(g.initiative, 20)
        self.assertSetEqual(g.weak_to, set((Attack.cold,)))
        self.assertSetEqual(g.immune_to, set())
        self.assertEqual(g.effective_power, 2785*14)


    def test_immune(self):
        g = parse_group('test_immune', '338 units each with 1378 hit points (immune to radiation) with an attack that does 39 cold damage at initiative 10')

        self.assertEqual(g.num_units, 338)
        self.assertEqual(g.hit_points, 1378)
        self.assertEqual(g.attack_damage, 39)
        self.assertEqual(g.initiative, 10)
        self.assertSetEqual(g.weak_to, set())
        self.assertSetEqual(g.immune_to, set((Attack.radiation,)))
        self.assertEqual(g.effective_power, 338*39)


    def test_immune_weak(self):
        g = parse_group('test_immune_weak', '4674 units each with 7617 hit points (immune to slashing, bludgeoning; weak to fire) with an attack that does 15 slashing damage at initiative 15')

        self.assertEqual(g.num_units, 4674)
        self.assertEqual(g.hit_points, 7617)
        self.assertEqual(g.attack_damage, 15)
        self.assertEqual(g.initiative, 15)
        self.assertSetEqual(g.weak_to, set((Attack.fire,)))
        self.assertSetEqual(g.immune_to, set((Attack.slashing, Attack.bludgeoning,)))
        self.assertEqual(g.effective_power, 4674*15)




test_data_army = '''
Immune System:
17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3

Infection:
801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4
'''
test_data_army = test_data_army.strip().split('\n')
assert len(test_data_army) == 7, test_data_army


class TestGroup(unittest.TestCase):
    def setUp(self):
        data           = iter(test_data_army)
        self.immune    = parse_army(data)
        self.infection = parse_army(data)


    def test_damage_infection(self):
        '''
        Infection group 1 would deal defending group 1 185832 damage
        Infection group 1 would deal defending group 2 185832 damage
        Infection group 2 would deal defending group 2 107640 damage
        '''
        self.assertEqual(self.infection[0].damage(self.immune[0]), 185832)
        self.assertEqual(self.infection[0].damage(self.immune[1]), 185832)
        self.assertEqual(self.infection[1].damage(self.immune[1]), 107640)


    def test_damage_immune(self):
        '''
        Immune System group 1 would deal defending group 1 76619 damage
        Immune System group 1 would deal defending group 2 153238 damage
        Immune System group 2 would deal defending group 1 24725 damage
        '''
        self.assertEqual(self.immune[0].damage(self.infection[0]), 76619)
        self.assertEqual(self.immune[0].damage(self.infection[1]), 153238)
        self.assertEqual(self.immune[1].damage(self.infection[0]), 24725)



class TestArmy(unittest.TestCase):
    def setUp(self):
        data = iter(test_data_army)
        self.immune = parse_army(data)
        self.infection = parse_army(data)


    def test_validate_data(self):
        '''
        Immune System:
        Group 1 contains 17 units
        Group 2 contains 989 units
        Infection:
        Group 1 contains 801 units
        Group 2 contains 4485 units
        '''
        self.assertEqual(len(self.immune), 2)
        self.assertEqual(self.immune[0].num_units, 17)
        self.assertEqual(self.immune[1].num_units, 989)

        self.assertEqual(len(self.infection), 2)
        self.assertEqual(self.infection[0].num_units, 801)
        self.assertEqual(self.infection[1].num_units, 4485)


    def test_target_selection_infection(self):
        '''
        Infection group 2 attacks defending group 2, killing 84 units
        Infection group 1 attacks defending group 1, killing 17 units
        '''
        choice = self.infection.target_selection(self.immune)
        self.assertEqual(choice[self.infection[1]], self.immune[1])
        self.assertEqual(choice[self.infection[0]], self.immune[0])


    def test_target_selection_immune(self):
        '''
        Immune System group 2 attacks defending group 1, killing 4 units
        Immune System group 1 attacks defending group 2, killing 51 units
        '''
        choice = self.immune.target_selection(self.infection)
        self.assertEqual(choice[self.immune[1]], self.infection[0])
        self.assertEqual(choice[self.immune[0]], self.infection[1])



class TestCombat(unittest.TestCase):
    def setUp(self):
        data = iter(test_data_army)
        self.immune = parse_army(data)
        self.infection = parse_army(data)


    def test1(self):
        combat(self.immune, self.infection)
        self.assertEqual(self.immune[0].num_units, 989 - 84)
        self.assertEqual(self.infection[0].num_units, 801 - 4)
        self.assertEqual(self.infection[1].num_units, 4485 - 51)


    def test2(self):
        combat(self.immune, self.infection)
        combat(self.immune, self.infection)
        self.assertEqual(self.immune[0].num_units, 905 - 144)
        self.assertEqual(self.infection[0].num_units, 797 - 4)
        self.assertEqual(self.infection[1].num_units, 4434)


    def test_full(self):
        while len(self.immune) and len(self.infection):
            combat(self.immune, self.infection)
        self.assertEqual(self.infection.score(), 5216)
        self.assertEqual(self.immune.score(), 0)


