#!/usr/bin/env python

from __future__ import print_function

from collections import Counter

with open('data.txt', 'r') as f:
    data = list(map(lambda x: (x.strip(), Counter(x.strip())), f.readlines()))

#print(data)
def find_words(data):
    for a, (wa, ca) in enumerate(data):
        for b, (wb, cb) in enumerate(data[:a]):
            diff = ca-cb
            if len(diff) == 1 and diff.most_common(1)[0][1] == 1:
                print('Found', wa, wb, diff)
                return wa, wb

word0, word1 = find_words(data)
print(word0, word1)

# The answer is found by removing the differing character from either ID.
answer = ''.join(a for a, b in zip(word0, word1) if a == b)
print('Answer:', answer)
