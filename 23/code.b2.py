#!/usr/bin/env python

'''
[Day 23 Part 2 - Any provably correct fast solution?](https://www.reddit.com/r/adventofcode/comments/a8sqov/help_day_23_part_2_any_provably_correct_fast/)
[pdewacht](https://www.reddit.com/r/adventofcode/comments/a8sqov/help_day_23_part_2_any_provably_correct_fast/ecen3wd)
[pdewacht/23-part-two.py](https://gist.github.com/pdewacht/fa7aa7e60952c6d67956599d6d4af360)
Answet location: (18374829, 41219174, 34232290)
bots in range: 970/1000
distance from origin: 93826293
: 93826293
'''

from partII import Bot
from partII import PriorityQueue
from partII import master_cube
import re
import sys






if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        #bots = [Bot(*map(int, re.findall(r'-?\d+', line, re.ASCII)))
        #        for line in sys.stdin]
        bots = [Bot(*map(int, re.findall(r'-?\d+', line, re.ASCII)))
                for line in f]
    assert len(bots) > 0

    q = PriorityQueue(bots)  # min-heap

    q.add(master_cube(bots))
    while q:
        score, dist, s, cube = q.pop()
        #print(score, dist, s, cube.x1, cube.y1, cube.z1, cube.s, q.q)
        if cube.s == 1:
            print("best location:", (cube.x1, cube.y1, cube.z1))
            print("bots in range: {}/{}".format(-score, len(bots)))
            print("distance from origin:", dist)
            print('Answer:', dist)
            break

        for subcube in iter(cube):
            q.add(subcube)
