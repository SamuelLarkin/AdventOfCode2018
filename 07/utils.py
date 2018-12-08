# -*- coding: utf-8 -*-

try:
    from functools import reduce
except:
    pass



test_data = [
        'Step C must be finished before step A can begin.',
        'Step C must be finished before step F can begin.',
        'Step A must be finished before step B can begin.',
        'Step A must be finished before step D can begin.',
        'Step B must be finished before step E can begin.',
        'Step D must be finished before step E can begin.',
        'Step F must be finished before step E can begin.',
        ]



def parse_dependencies(f):
    deps = []
    for l in f:
        p = l.strip().split()
        deps.append((p[1], p[7]))
    return deps



def complete_graph(data):
    # Convert from defaultdict to dict
    data = dict(data)
    # Ignore self dependencies
    for k, v in data.items():
        v.discard(k)
    # Add node with no dependencies
    # Make sure all node have a set of incoming edges, or an empty set for the starting nodes.
    extra_items_in_deps = reduce(set.union, data.values()) - set(data.keys())
    data.update({item:set() for item in extra_items_in_deps})

    return data

# https://rosettacode.org/wiki/Category:Python
def topological_sort_generator(data):
    """
    L ← Empty list that will contain the sorted elements
    S ← Set of all nodes with no incoming edge
    while S is non-empty do
	remove a node n from S
	add n to tail of L
	for each node m with an edge e from n to m do
	    remove edge e from the graph
	    if m has no other incoming edges then
		insert m into S
    if graph has edges then
	return error   (graph has at least one cycle)
    else
	return L   (a topologically sorted order)
    """
    data = complete_graph(data)
    while True:
        #print('a', data)
        ordered = set(item for item,dep in data.items() if not dep)
        if not ordered:
            break
        # From the available nodes, with want the one that comes first alphabetically.
        ordered = sorted(ordered)[0]
        yield ordered
        ordered = set(ordered)
        data = {
                item: (dep - ordered) for item,dep in data.items()
                if item not in ordered
                }
    assert not data, "A cyclic dependency exists amongst %r" % data



def toposort2(data):
    #print ('\n'.join( toposort2(data) ))
    for k, v in data.items():
        v.discard(k) # Ignore self dependencies
    extra_items_in_deps = reduce(set.union, data.values()) - set(data.keys())
    data.update({item:set() for item in extra_items_in_deps})
    while True:
        ordered = set(item for item,dep in data.items() if not dep)
        if not ordered:
            break
        yield ' '.join(sorted(ordered))
        data = {item: (dep - ordered) for item,dep in data.items()
                if item not in ordered}
    assert not data, "A cyclic dependency exists amongst %r" % data
 
