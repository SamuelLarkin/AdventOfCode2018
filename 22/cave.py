from collections import defaultdict
from collections import namedtuple
from enum import Enum
from functools import total_ordering
import heapq
import logging



Type = Enum('Type', ('rocky', 'wet', 'narrow'))

Tool = Enum('Tool', ('climbing_gear', 'torch', 'neither'))

Area = namedtuple('Area', ('coordinates', 'depth', 'geologic_index', 'erosion_level', 'type'))

SearchPositionBase = namedtuple('SearchPositionBase', ('cost', 'coordinates', 'tool'))
@total_ordering
class SearchPosition(SearchPositionBase):
    def __cmp__(self, other):
        # heapq uses cmp()
        return cmp(self.cost, other.cost)


    def __eq__(self, other):
        return self.cost == other.cost


    def __lt__(self, other):
        return self.cost < other.cost



def risk_level(cave):
    return sum(b.type.value-1 for b in cave.values())



def _helper(gi, depth):
    el = (gi + depth) % 20183
    t = el % 3
    return gi, el, Type(t+1)
    


def display_cave(cave):
    mapping = { Type.rocky: '.', Type.wet: '=', Type.narrow: '|' }
    mapper = lambda x: mapping[x]
    current_line = 0
    for a in sorted(cave.values(), key=lambda c: (c.coordinates[1], c.coordinates[0])):
        if current_line != a.coordinates[1]:
            current_line = a.coordinates[1]
            print('')
        print(mapper(a.type), sep='', end='')
    print('')



def create_cave(depth, target, padding=0):
    cave_width, cave_height = target
    cave_width += 1 + padding
    cave_height += 1 + padding
    cave = {}

    for x in range(cave_width):
        # At 1,0, because the Y coordinate is 0,
        # - The geologic index is 1 * 16807 = 16807.
        # - The erosion level is (16807 + depth) % 20183 = 17317.
        # - The type is 17317 % 3 = 1, wet.
        gi, el, t = _helper(x* 16807, depth)
        cave[x,0] = Area((x,0), depth, gi, el, t)

    for y in range(cave_height):
        # At 0,1, because the X coordinate is 0,
        # - the geologic index is 1 * 48271 = 48271.
        # - The erosion level is (48271 + depth) % 20183 = 8415.
        # - The type is 8415 % 3 = 0, rocky.
        gi, el, t = _helper(y* 48271, depth)
        cave[0,y] = Area((0,y), depth, gi, el, t)
 
    # At 0,0,
    # - The geologic index is 0.
    # - The erosion level is (0 + depth) % 20183 = 510.
    # - The type is 510 % 3 = 0, rocky.
    gi, el, t = _helper(0, depth)
    cave[0,0] = Area((0,0), depth, gi, el, t)

    # At 10,10, because they are the target's coordinates, the geologic index
    # is 0. The erosion level is (0 + 510) % 20183 = 510. The type is 510 % 3 =
    # 0, rocky.
    gi, el, t = _helper(0, depth)
    cave[target] = Area(target, depth, gi, el, t)

    for y in range(1, cave_height):
        for x in range(1, cave_width):
            # At 1,1, neither coordinate is 0 and it is not the coordinate of the target,
            # - so the geologic index is the erosion level of 0,1 (8415) times
            #   the erosion level of 1,0 (17317), 8415 * 17317 = 145722555.
            # - The erosion level is (145722555 + depth) % 20183 = 1805.
            # - The type is 1805 % 3 = 2, narrow.
            if (x,y) != target:
                gi, el, t = _helper(cave[x-1,y].erosion_level * cave[x,y-1].erosion_level, depth)
                cave[x,y] = Area((x,y), depth, gi, el, t)
    
    return cave



'''
- In rocky regions, you can use the climbing gear or the torch. You cannot use
  neither (you'll likely slip and fall).
- In wet regions, you can use the climbing gear or neither tool. You cannot use
  the torch (if it gets wet, you won't have a light source).
- In narrow regions, you can use the torch or neither tool. You cannot use the
  climbing gear (it's too bulky to fit).
'''
type_tools = {
        # Rocky
        Type.rocky: ( Tool.climbing_gear, Tool.torch ),
        # Wet
        Type.wet: ( Tool.climbing_gear, Tool.neither ),
        # Narrow
        Type.narrow: ( Tool.torch, Tool.neither ),
        }

# What tool are we allowed to change to depending on the Type.
change_tool = {
        (Type.rocky, Tool.climbing_gear): Tool.torch,
        (Type.rocky, Tool.torch): Tool.climbing_gear,
        (Type.wet, Tool.climbing_gear): Tool.neither,
        (Type.wet, Tool.neither): Tool.climbing_gear,
        (Type.narrow, Tool.torch): Tool.neither,
        (Type.narrow, Tool.neither): Tool.torch,
        }

# Where can we go with a certain Tool.
allowed_moves = {
        # Rocky & Wet
        Tool.climbing_gear: { Type.rocky, Type.wet },
        # Rocky & Narrow
        Tool.torch: { Type.rocky, Type.narrow },
        # Wet & Narrow
        Tool.neither: { Type.wet, Type.narrow },
        }


def is_a_rock_wall(position):
    '''
    The regions with negative X or Y are solid rock and cannot be traversed.
    '''
    return position[0] < 0 or position[1] < 0



def move(position, direction):
    return (position[0] + direction[0], position[1] + direction[1])



def manhattan_distance(position, target):
    return abs(position[0] - target[0]) + abs(position[1] - target[1])



def display_visited(visited):
    print(tool)
    for y in range(15):
        for x in range(15):
            print('(', sep='', end='')
            for tool in Tool:
                if ((x,y), tool) in visited:
                    print('{:2d}'.format(visited[(x,y), tool]), end='')
                else:
                    print('__', end='')
            print(')', sep='', end='')
        print('')
    print('')



def rescue_target(cave, target, start = SearchPosition(0, (0,0), Tool.torch)):
    # Holds the best cost to get to a certain coordinate
    visited = defaultdict(lambda: 10000)
    #cave    = { c.coordinates: c for a in cave for c in a }

    assert cave[target].type == Type.rocky
    assert start.tool == Tool.torch
    assert cave[(0,0)].geologic_index == 0
    assert cave[(0,0)].type == Type.rocky

    heap = [(start.cost, manhattan_distance(start.coordinates, target), start)]
    while len(heap) > 0:
        #print('heap.len:', len(heap))
        #print(heap)
        cost, distance, current_search_position = heapq.heappop(heap)

        # Finally, once you reach the target, you need the torch equipped
        # before you can find him in the dark. The target is always in a rocky
        # region, so if you arrive there with climbing gear equipped, you will
        # need to spend seven minutes switching to your torch.
        if current_search_position.coordinates == target and current_search_position.tool == Tool.torch:
            logging.getLogger(__name__).info('Reached the target')
            #display_visited(visited)
            return current_search_position.cost

        # Moving between regions without changing tool.
        for d in ((0,1), (0,-1), (1,0), (-1,0)):
            next_position = move(current_search_position.coordinates, d)
            if is_a_rock_wall(next_position):
                continue
            # You can move to an adjacent region (up, down, left, or right;
            # never diagonally) if your currently equipped tool allows you to
            # enter that region.
            if next_position in cave and cave[next_position].type in allowed_moves[current_search_position.tool]:
                newSearchPosition = SearchPosition(
                        current_search_position.cost + 1,
                        next_position,
                        current_search_position.tool)
                if newSearchPosition.cost < visited[newSearchPosition.coordinates, newSearchPosition.tool]:
                    visited[newSearchPosition.coordinates, newSearchPosition.tool] = newSearchPosition.cost
                    heapq.heappush(
                            heap,
                            (
                                newSearchPosition.cost,
                                manhattan_distance(newSearchPosition.coordinates, target),
                                newSearchPosition))

        # Changing tool
        # Switching to using the climbing gear, torch, or neither always takes
        # seven minutes, regardless of which tools you start with.
        cost = current_search_position.cost + 7
        # You can change your currently equipped tool or put both away if your
        # new equipment would be valid for your current region.
        new_tool = change_tool[(cave[current_search_position.coordinates].type, current_search_position.tool)]
        newSearchPosition = SearchPosition(cost, current_search_position.coordinates, new_tool)
        if newSearchPosition.cost < visited[newSearchPosition.coordinates, newSearchPosition.tool]:
            visited[newSearchPosition.coordinates, newSearchPosition.tool] = newSearchPosition.cost
            heapq.heappush(
                    heap,
                    (
                        newSearchPosition.cost,
                        manhattan_distance(current_search_position.coordinates, target),
                        newSearchPosition))

    assert (target, Tool.torch) in visited, "We haven't reach the target"

    return visited[target]



def rescue_target2(cave, target):
    import networkx as nx
    graph = nx.Graph()
    for c in cave.values():
        tools = type_tools[cave[c.coordinates].type]
        graph.add_edge((c.coordinates, tools[0]), (c.coordinates, tools[1]), weight=7)
        graph.add_edge((c.coordinates, tools[1]), (c.coordinates, tools[0]), weight=7)

        # Moving between regions without changing tool.
        for d in ((0,1), (0,-1), (1,0), (-1,0)):
            next_position = move(c.coordinates, d)
            # You can move to an adjacent region (up, down, left, or right;
            # never diagonally) if your currently equipped tool allows you to
            # enter that region.
            for tool in tools:
                # next_position might be negative or outside the computed cave.
                if next_position in cave:
                    if cave[next_position].type in allowed_moves[tool]:
                        graph.add_edge((c.coordinates, tool), (next_position, tool), weight=1)

    return nx.dijkstra_path_length(graph, ((0, 0), Tool.torch), (target, Tool.torch))
