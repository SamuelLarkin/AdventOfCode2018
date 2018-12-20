#!/usr/bin/env python

from __future__ import print_function

from map import create_rooms
from map import furthest_room





if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        regex = f.readline().strip()

    rooms = create_rooms(regex)
    far_rooms = list(filter(lambda r: r[1] >= 1000, rooms.items()))
    print(far_rooms)


    print('Answer:', len(far_rooms))
    # 8677
