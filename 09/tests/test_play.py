import unittest
import play


class TestPlay(unittest.TestCase):
    def test_9players_lastmarble25(self):
        self.assertEqual(play.play(number_player=9, last_marble=25), 32)

    def test_10players_lastmarble1618(self):
        self.assertEqual(play.play(number_player=10, last_marble=1618), 8317)

    def test_13players_lastmarble7999(self):
        self.assertEqual(play.play(number_player=13, last_marble=7999), 146373)

    def test_17players_lastmarble1104(self):
        self.assertEqual(play.play(number_player=17, last_marble=1104), 2764)

    def test_21players_lastmarble6111(self):
        self.assertEqual(play.play(number_player=21, last_marble=6111), 54718)

    def test_30players_lastmarble5807(self):
        self.assertEqual(play.play(number_player=30, last_marble=5807), 37305)

