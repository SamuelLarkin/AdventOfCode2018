from collections import Counter
from sklearn.feature_extraction.image import extract_patches_2d
import numpy as np


# open ground (.), trees (|), or a lumberyard (#).


def generate_patches(x):
    """
    [Extract blocks or patches from NumPy Array](https://stackoverflow.com/a/31529389)
    """
    return  x.reshape(x.shape[0]//2, 2, x.shape[1]//2, 2).swapaxes(1, 2).reshape(-1, 2, 2)



def convolve(acres):
    w, h = acres.shape
    # We need to augment the area with border.
    a = (np.zeros((w+2, h+2)) + 65).astype(acres.dtype)
    a[1:-1, 1:-1] = acres
    new_acre = np.asarray([ step(p) for p in extract_patches_2d(a, (3,3)) ]).reshape(w,h)

    return new_acre



def step(patch):
    assert len(patch) == 3
    counts = Counter(patch.ravel().tolist())

    if patch[1,1] == '.':
        # An open acre will become filled with trees if three or more adjacent
        # acres contained trees. Otherwise, nothing happens.
        if counts['|'] >= 3:
            return '|'
    if patch[1,1] == '|':
        # An acre filled with trees will become a lumberyard if three or more
        # adjacent acres were lumberyards. Otherwise, nothing happens.
        if counts['#'] >= 3:
            return '#'
    if patch[1,1] == '#':
        # An acre containing a lumberyard will remain a lumberyard if it was
        # adjacent to at least one other lumberyard and at least one acre
        # containing trees. Otherwise, it becomes open.
        # NOTE: counts has at least one lumber yard aka the center tile.
        if counts['#'] >= 1+1 and counts['|'] >= 1:
            return '#'
        else:
            return '.'

    return patch[1,1]




def score(acres):
    counts = Counter(acres.ravel().tolist())

    return counts['|'] * counts['#']



def reader(f):
    acres = [list(l.strip()) for l in f]
    acres = np.asarray(acres)

    return acres
