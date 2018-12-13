import numpy as np
from scipy import signal

from itertools import tee
from tqdm import trange

try:
    from itertools import izip as zip
except ImportError:
    pass


np.set_printoptions(linewidth=200)



def parse(f):
    f = iter(f)
    l = next(f)
    l = l.strip()
    initial_state = l.split()[-1]
    l = next(f)
    rules = { tuple(pattern): r for pattern, _, r in map(lambda x: x.strip().split(), f) }

    return initial_state, rules



# NGRAM
def ngram(iterable, n=2):
    """s -> (s0,s1), (s1,s2), (s2, s3), ..."""
    assert n > 0, 'Cannot create negative n-grams.'
    l = tee(iterable, n)
    for i, s in enumerate(l):
        for _ in range(i):
            next(s, None)
    return zip(*l)



def grow(generation, rules):
    next_generation = '.'*2 + ''.join(rules.get(p, '.') for p in ngram(generation, n=5)) + '.'*2

    return next_generation



def grow_generation(initial_state, rules, n=20):
    current_generation = initial_state
    for i in trange(n):
        current_generation = grow(current_generation, rules)

    return current_generation
