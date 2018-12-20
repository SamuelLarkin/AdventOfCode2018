from collections import defaultdict



roses = {
        'N': (0,1),
        'S': (0,-1),
        'W': (-1,0),
        'E': (1,0),
        }



def _move(position, direction):
    d = roses[direction]
    return (position[0]+d[0], position[1]+d[1])



def furthest_room(rooms):
    return sorted(rooms.items(), key=lambda x: x[1]).pop()[1]



def create_rooms(regex):
    '''
    ^ENWWW(NEEE|SSE(EE|N))$
    ^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$
    '''
    stack = []
    rooms = defaultdict(lambda: 10000)
    distance = 0
    position = (0,0)
    for instruction in regex:
        if instruction == '^':
            pass
        if instruction == '$':
            # We are done parsing.
            return rooms
        elif instruction in 'NEWS':
            distance += 1
            position = _move(position, instruction)
            rooms[position] = min(distance, rooms[position])
        elif instruction == '(':
            stack.append(position)
        elif instruction == ')':
            position = stack.pop()
            distance = rooms[position]
        elif instruction == '|':
            position = stack[-1]
            distance = rooms[position]

    return rooms
