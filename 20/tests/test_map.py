import unittest
from map import create_rooms
from map import furthest_room



class TestMap(unittest.TestCase):
    def test3(self):
        '''
        ^WNE$
        '''
        rooms = create_rooms(regex = '^WNE$')
        print(rooms)
        furthest = furthest_room(rooms)
        self.assertEqual(furthest, 3)


    def test2(self):
        '''
        ^ENWWW(NEEE|SSE(EE|N))$
        '''
        rooms = create_rooms(regex = '^ENWWW(NEEE|SSE(EE|N))$')
        print(rooms)


    def test10(self):
        '''
        ^ENWWW(NEEE|SSE(EE|N))$
        '''
        rooms = create_rooms(regex = '^ENWWW(NEEE|SSE(EE|N))$')
        print(rooms)
        furthest = furthest_room(rooms)
        self.assertEqual(furthest, 10)


    def test18(self):
        '''
        ^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$
        '''
        rooms = create_rooms(regex = '^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$')
        print(rooms)
        furthest = furthest_room(rooms)
        self.assertEqual(furthest, 18)


    def test23(self):
        '''
        ^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$
        '''
        rooms = create_rooms(regex = '^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$')
        print(rooms)
        furthest = furthest_room(rooms)
        self.assertEqual(furthest, 23)


    def test31(self):
        '''
        ^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$
        '''
        rooms = create_rooms(regex = '^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$')
        print(rooms)
        furthest = furthest_room(rooms)
        self.assertEqual(furthest, 31)
