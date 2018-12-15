from player import Player
import numpy as np



class Game:
    def __init__(self, map_, walls, players):
        self.map_ = map_
        self.walls = walls
        self.players = players


    def step(self):
        # The order in which units take their turns within a round is the
        # reading order of their starting positions in that round, regardless
        # of the type of unit or whether other units have moved after the round
        # started.
        self.players = sorted(self.players, key=lambda p: p.position)
        for p in self.players:
            p.step(self.map_, self.walls, self.players)


    def display(self):
        a = np.asarray(self.map_)
        for p in self.players:
            a[p.i][p.j] = p.type_
        for r in a:
            print(''.join(r))


    def done(self):
        elf = set(p for p in self.players if p.type_ == 'E')
        goblin = set(p for p in self.players if p.type_ == 'G')
        return not elf or not goblin


    def _score(self):
        return sum(map(lambda p: p.hit_point, self.players))


    def combat(self, n=1000):
        for step in range(n):
            if self.done():
                break
            self.step()
        step -= 1
        return step, step*self._score()


    def __repr__(self):
        return 'Game(players: {p}\nwalls: {w})'.format(
                p = sorted(self.players, key=lambda p: p.position),
                w = ''.join(map(str, self.walls)))
