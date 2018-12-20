#!/usr/bin/env python

from __future__ import print_function

from map import create_rooms
from map import furthest_room





if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        regex = f.readline().strip()

    rooms = create_rooms(regex)
    furthest = furthest_room(rooms)


    print('Answer:', furthest)
    # 3885
