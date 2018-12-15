from player import Player



def read_map(f):
    map_ = [list(l.strip()) for l in f]
    players = []
    walls = set()
    for i, r in enumerate(map_):
        for j, c in enumerate(r):
            if c in 'EG':
                players.append(Player(c, (i, j)))
                map_[i][j] = '.'
            if c == '#':
                walls.add((i,j))

    return map_, players, walls
