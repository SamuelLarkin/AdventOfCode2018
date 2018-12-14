#!/usr/bin/env python

from __future__ import print_function

from utils import generate_scores
from utils import score
from utils import find_score





if __name__ == '__main__':
    answer = find_score(generate_scores(21633601), '633601')
    print('Answer:', answer)
    # 20310465
