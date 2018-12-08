from collections import namedtuple

"""
2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
A----------------------------------
    B----------- C-----------
                     D-----
"""
test_data = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'


Node = namedtuple('Node', ('children', 'metadata'))

def parse(f):
    result = []
    def subparser(data):
        num_children = data.pop(0)
        num_metadata = data.pop(0)
        children = [ subparser(data) for _ in range(num_children) ]
        metadata = [ data.pop(0) for _ in range(num_metadata) ]

        return Node(children, metadata)

    data = list(map(int, f.strip().split()))
    result = subparser(data)
    return result



def chain(nodes):
    # chain('ABC', 'DEF') --> A B C D E F
    for it in nodes:
        for element in it.metadata:
            yield element
