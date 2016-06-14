import unittest
from tournaments import tournaments


class TestTournament(unittest.TestCase):

    def test_minimum(self):
        teams = ('Italia', 'Francia', 'Germania')
        [triangulars] = tournaments(teams)
        self.assertTupleEqual(triangulars, teams)


    def test_tournament(self):
        teams = ('Italia', 'Francia', 'Germania', 'Spagna')
        triangulars = tournaments(teams)
        expected = [
            ('Italia', 'Francia', 'Germania'),
            ('Italia', 'Francia', 'Spagna'),
            ('Italia', 'Germania', 'Spagna'),
            ('Francia', 'Germania', 'Spagna')]
        self.assertListEqual(triangulars, expected)

if __name__ == '__main__':
    unittest.main()
