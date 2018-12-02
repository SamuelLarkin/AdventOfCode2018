#!/usr/bin/env python

from __future__ import print_function

import numpy as np

with open('data.txt', 'r') as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

# Let's load the data into numpy arrays of char->int
data_np = np.asarray(list(map(list, data)), 'c')
# https://gist.github.com/tkf/2276773
data_int = data_np.view(np.uint8)
print(data_int.shape, data_int)

# Reshape our arrays to allow computing how many letters are different between two strings.
a = np.expand_dims(data_int, axis=-1)
# a.shape == 250, 26, 1
b = np.transpose(a, (2,1,0))
# b.shape == 1, 26, 250

# Count how many letters are different between two strings.
diff = np.sum((a != b).astype(np.int), axis=1)
# diff.shape == 250, 250
print(diff.shape, diff)

# Make sure when we compared a string with itself, it must have all its letters in common aka no differences.
assert np.all(np.diagonal(diff) == 0)

# Figure out what pair of strings have exactly one difference.
matches = np.where(diff == 1)[0].tolist()
print(matches)
print(data[matches[0]], data[matches[1]])

# The answer is found by removing the differing character from either ID.
answer = ''.join(a for a, b in zip(data[matches[0]], data[matches[1]]) if a == b)
print('Answer:', answer)
