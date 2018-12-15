import numpy as np



def adjacent(position):
    i, j = position
    return set((
            (i - 1, j),
            (i, j + 1),
            (i + 1, j),
            (i, j - 1),
            ))



def player_positions(players):
    return set(p.position for p in players)



def calculate_reachable_bfs(start, map_, invalid_positions):
    # http://rosettacode.org/wiki/Maze_generation#Python
    visited = np.zeros((len(map_), len(map_[0])), dtype=np.int)
    distance = np.ones_like(visited) * Player.unreachable_distance
    queue = [(start, 0)]
    while len(queue) > 0:
        p, d = queue.pop(0)
        i, j = p
        if visited[i][j] == 1: continue
        visited[i][j] = 1
        distance[i][j] = d
        queue.extend(sorted((ap, d+1) for ap in adjacent(p) - invalid_positions))

    return distance



class Player:
    unreachable_distance = 1e3

    def __init__(self, type_, position, attack_power = 3, hit_point = 200):
        self.type_ = type_
        self.position = position
        self.attack_power = attack_power
        self.hit_point = hit_point
        self.in_range = None


    @property
    def i(self):
        return self.position[0]
    @property
    def j(self):
        return self.position[1]

    @property
    def adjacent(self):
        return adjacent(self.position)


    def find_in_range(self, walls, players):
        invalid_positions = walls | player_positions(players)
        self.in_range = sorted(self.adjacent - invalid_positions)


    def calculate_reachable_bfs(self, map_, walls, players):
        return calculate_reachable_bfs(self.position,
                map_,
                invalid_positions = walls | player_positions(players))


    def chosen(self, map_, walls, players):
        in_range = set(ap for p in players for ap in adjacent(p.position) if p.type_ != self.type_)
        in_range -= walls
        in_range -= player_positions(players)

        distance = self.calculate_reachable_bfs(map_, walls, players)
        reachable = set(p for p in in_range if distance[p] != Player.unreachable_distance)

        # If multiple steps would put the unit equally closer to its
        # destination, the unit chooses the step which is first in reading
        # order. (This requires knowing when there is more than one shortest
        # path so that you can consider the first step of each such path.)
        nearest = sorted((distance[p], p) for p in reachable)

        if len(nearest):
            chosen = nearest[0]
        else:
            # don't move
            chosen = (0, self.position)

        return chosen


    def move(self, map_, walls, players):
        distance, chosen = self.chosen(map_, walls, players)

        if distance > 0:
            distances = calculate_reachable_bfs(chosen,
                    map_,
                    invalid_positions = walls | player_positions(players))

            d, new_position = min((distances[p], p) for p in adjacent(self.position))
            self.position = new_position


    def attack(self, players):
        opponents = adjacent(self.position) - player_positions(p for p in players if p.type_ == self.type_)
        opponents = list(filter(lambda p: p.position in opponents, players))
        #opponents = sorted(opponents, key=lambda p: p.position)
        if len(opponents) > 0:
            # The adjacent target with the fewest hit points is selected; in a
            # tie, the adjacent target with the fewest hit points which is
            # first in reading order is selected.
            weakest = min(opponents, key=lambda p: (p.hit_point, p.position))
            #weakest = list(filter(lambda p: p in opponents, players))[0]
            weakest.hit_point -= self.attack_power
            if weakest.hit_point <= 0:
                print(weakest, 'dies')
                players.remove(weakest)


    def step(self, map_, walls, players):
        if adjacent(self.position) & player_positions(filter(lambda p: p.type_ != self.type_, players)):
            # Attack
            self.attack(players)
        else:
            # Move
            self.move(map_, walls, players)
            if adjacent(self.position) & player_positions(filter(lambda p: p.type_ != self.type_, players)):
                # Attack
                self.attack(players)


    def __repr__(self):
        return 'Player(type={t}, position={p} , attack_power={a}, hit_point={h})'.format(
                t=self.type_,
                p=self.position,
                a=self.attack_power,
                h=self.hit_point)
