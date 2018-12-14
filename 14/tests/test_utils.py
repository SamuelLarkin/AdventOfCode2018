import unittest
from utils import generate_scores
from utils import score
from utils import find_score


class TestScoreGeneration(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestScoreGeneration, self).__init__(*args, **kwargs)
        self.scores = generate_scores(3000)


    def score(self, n):
        return score(self.scores, n)


    def test9(self):
        self.assertEqual(self.score(9), '5158916779')


    def test5(self):
        self.assertEqual(self.score(5), '0124515891')


    def test18(self):
        self.assertEqual(self.score(18), '9251071085')


    def test2018(self):
        self.assertEqual(self.score(2018), '5941429882')




class TestFindPattern(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestFindPattern, self).__init__(*args, **kwargs)
        self.scores = generate_scores(3000)


    def test51589(self):
        result = find_score(self.scores, '51589')
        self.assertEqual(result, 9)


    def test01245(self):
        result = find_score(self.scores, '01245')
        self.assertEqual(result, 5)


    def test92510(self):
        result = find_score(self.scores, '92510')
        self.assertEqual(result, 18)


    def test59414(self):
        result = find_score(self.scores, '59414')
        self.assertEqual(result, 2018)
