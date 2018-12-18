import random



def version1(edges):
    """
    [Matching (graph theory)](https://en.wikipedia.org/wiki/Matching_(graph_theory))
    [](https://www.reddit.com/r/adventofcode/comments/a6p5ih/day_16_part_2_solving_opcodes/ebwsivn)
    # [11, 6, 0, 8, 4, 7, 10, 12, 3, 2, 5, 1, 15, 13, 9, 14]
    # [4, 0, 15, 6, 8, 7, 2, 12, 10, 5, 11, 3, 9, 14, 13, 1]
    """
    association = [-1] * len(opcodes) # their number -> my number
    def assign(v):
        w = random.choice(list(edges[v]))
        u, association[w] = association[w], v
        if u != -1: assign(u)

    for i in range(len(opcodes)):
        assign(i)

    return association



def bipartite_perfect_matching(edges):
    """
    [Matching (graph theory)](https://en.wikipedia.org/wiki/Matching_(graph_theory))
    [](https://www.reddit.com/r/adventofcode/comments/a6p5ih/day_16_part_2_solving_opcodes/ebwsivn)
    opcodes number read from the data.txt file is match to my opcodes which are in opcodes.opcodes
    opcode 0 is match to my opcode 11
    opcode 5 is match to my opcode 7
    [4, 0, 15, 6, 8, 7, 2, 12, 10, 5, 11, 3, 9, 14, 13, 1]
    This is a better method since the previous method hits a maximum recursion limit.
    """

    association = [-1] * len(edges) # their number -> my number
    for v in range(len(edges)):
        while v != -1:
            w = random.choice(edges[v])
            v, association[w] = association[w], v

    return association
