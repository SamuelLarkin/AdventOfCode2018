from enum import Enum
from collections import namedtuple
import re

import networkx as nx
from networkx.algorithms import bipartite
from itertools import chain



Attack = Enum('Attack', ('cold', 'fire', 'slashing', 'bludgeoning', 'radiation'))

Base = namedtuple('Base', ('title', 'hit_points', 'immune_to', 'weak_to', 'attack_type', 'attack_damage', 'initiative'))

class Unit(Base):
    pass



class Group(Base):
    def __new__(cls, title, num_units, hit_points, immune_to, weak_to, attack_type, attack_damage, initiative):
        self = super(Group, cls).__new__(cls, title, hit_points, immune_to, weak_to, attack_type, attack_damage, initiative)
        self.num_units = num_units

        return self


#    def __init__(self, *args, **kwargs):
#        super(Group, self).__init__(*args, **kwargs)
#        self.hit_points    = hit_points
#        self.immune_to     = set(immune_to or [])
#        self.weak_to       = set(weak_to or [])
#        self.attack_type   = attack_type
#        self.attack_damage = attack_damage
#        self.initiative    = initiative
#        self.units        = []


    @property
    def effective_power(self):
        '''
        Each group also has an effective power: the number of units in that
        group multiplied by their attack damage. The above group has an
        effective power of 18 * 8 = 144. Groups never have zero or negative
        units; instead, the group is removed from combat.
        '''
        return self.num_units * self.attack_damage


    def damage(self, other):
        '''
        The damage an attacking group deals to a defending group depends on the
        attacking group's attack type and the defending group's immunities and
        weaknesses. By default, an attacking group would deal damage equal to
        its effective power to the defending group. However, if the defending
        group is immune to the attacking group's attack type, the defending
        group instead takes no damage; if the defending group is weak to the
        attacking group's attack type, the defending group instead takes double
        damage.
        '''
        if self.attack_type in other.immune_to:
            damage = 0
        elif self.attack_type in other.weak_to:
            damage = 2 * self.attack_damage
        else:
            damage = self.attack_damage

        return damage * self.num_units


    def received(self, damage):
        self.num_units = max(0, self.num_units - damage // self.hit_points)



class Army:
    def __init__(self, title, *args, **kwargs):
        super(Army, self).__init__(*args, **kwargs)
        self.title = title
        self.groups = []


    def __len__(self):
        return len(self.groups)


    def __iter__(self):
        return iter(self.groups)


    def __getitem__(self, index):
        return self.groups[index]


    def append(self, group):
        self.groups.append(group)


    def boost(self, boost):
        self.boost = boost


    def target_selection(self, other_army):
        '''
        During the target selection phase, each group attempts to choose one
        target. In decreasing order of effective power, groups choose their
        targets; in a tie, the group with the higher initiative chooses first.
        The attacking group chooses to target the group in the enemy army to
        which it would deal the most damage (after accounting for weaknesses
        and immunities, but not accounting for whether the defending group has
        enough units to actually receive all of that damage).

        If an attacking group is considering two defending groups to which it
        would deal equal damage, it chooses to target the defending group with
        the largest effective power; if there is still a tie, it chooses the
        defending group with the highest initiative. If it cannot deal any
        defending groups damage, it does not choose a target. Defending groups
        can only be chosen as a target by one attacking group.

        At the end of the target selection phase, each group has selected zero
        or one groups to attack, and each group is being attacked by zero or
        one groups.
        '''
        used = set()
        choice = {}
        for g in sorted(self, key=lambda g: (g.effective_power, g.initiative), reverse=True):
            targets = sorted(
                    # todo skip group that have no units
                    filter(lambda a: a[1] not in used and a[0] > 0,
                        map(lambda b: (g.damage(b), b), other_army)), 
                    key=lambda og: (og[0], og[1].effective_power, og[1].initiative))
            if len(targets) > 0:
                target = targets[-1][1]
                used.add(target)
                choice[g] = target

        return choice



    def target_selection_graph(self, other_army):
        '''
        During the target selection phase, each group attempts to choose one
        target. In decreasing order of effective power, groups choose their
        targets; in a tie, the group with the higher initiative chooses first.
        The attacking group chooses to target the group in the enemy army to
        which it would deal the most damage (after accounting for weaknesses
        and immunities, but not accounting for whether the defending group has
        enough units to actually receive all of that damage).

        If an attacking group is considering two defending groups to which it
        would deal equal damage, it chooses to target the defending group with
        the largest effective power; if there is still a tie, it chooses the
        defending group with the highest initiative. If it cannot deal any
        defending groups damage, it does not choose a target. Defending groups
        can only be chosen as a target by one attacking group.

        At the end of the target selection phase, each group has selected zero
        or one groups to attack, and each group is being attacked by zero or
        one groups.
        '''
        B = nx.Graph()
        for g in sorted(self, key=lambda g: (g.effective_power, g.initiative), reverse=True):
            for og in other_army:
                damage = g.damage(og)
                if damage > 0:
                    B.add_edge(g, og, weight=(damage, og.effective_power, og.initiative))

        #print(B.edges())
        #bottom_nodes, top_nodes = bipartite.sets(B)
        #print(bottom_nodes)
        #print(top_nodes)

        #match = nx.bipartite.maximum_matching(B)
        match = nx.algorithms.matching.max_weight_matching(B)
        for k, v in match.items():
            print(k, '=>', v)


    def prune(self):
        a = len(self.groups)
        self.groups = list(filter(lambda g: g.num_units > 0, self.groups))
        return a != len(self.groups)


    def score(self):
        return sum(g.num_units for g in self.groups)



def combat(immune, infection):
    '''
    During the attacking phase, each group deals damage to the target it
    selected, if any. Groups attack in decreasing order of initiative,
    regardless of whether they are part of the infection or the immune system.
    (If a group contains no units, it cannot attack.)
    '''
    immune_choice    = immune.target_selection(infection)
    infection_choice = infection.target_selection(immune)

    for g, og in sorted(chain(immune_choice.items(), infection_choice.items()),
            key=lambda a: a[0].initiative,
            reverse=True):
        og.received(g.damage(og))

    return immune.prune() or infection.prune()



def parse_group(title, line, boost):
    '''
    4674 units each with 7617 hit points (immune to slashing, bludgeoning; weak to fire) with an attack that does 15 slashing damage at initiative 15
    2785 units each with 4474 hit points (weak to cold) with an attack that does 14 fire damage at initiative 20
    2702 units each with 10159 hit points with an attack that does 7 fire damage at initiative 7
    '''

    boost = max(1, boost)

    desc = re.compile(r'(\d+) units each with (\d+) hit points(?: \((.+)\))? with an attack that does (\d+) (\w+) damage at initiative (\d+)')
    line = line.strip()
    m = desc.match(line)
    assert m, line
    num_units     = int(m.group(1))
    hit_points    = int(m.group(2))
    attack_damage = int(m.group(4))
    attack_type   = Attack[m.group(5)]
    initiative    = int(m.group(6))
    parts         = m.group(3).split(';') if m.group(3) != None else []
    immune_to     = None
    weak_to       = None
    for part in parts:
        part = part.strip()
        if part.startswith('immune to'):
            immune_to = frozenset(map(lambda s: Attack[s.strip()], part[10:].split(',')))
        elif part.startswith('weak to'):
            weak_to = frozenset(map(lambda s: Attack[s.strip()], part[8:].split(',')))
        else:
            assert False, part

    g = Group(title,
            num_units,
            hit_points,
            immune_to or frozenset(),
            weak_to or frozenset(),
            attack_type,
            attack_damage + boost,
            initiative)

    return g



def parse_army(f, boost=1):
    f = iter(f)
    title = next(f)[:-1]
    army = Army(title)
    for l in f:
        l = l.strip()
        if l == '':
            break
        army.append(parse_group(title, l, boost))

    return army



def parse(f, boost = 1):
    immune = parse_army(f, boost)
    infection = parse_army(f)

    return immune, infection
