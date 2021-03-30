import unittest
from application import get_player_names


class TestTeamStats(unittest.TestCase):
    def setUp(self):
        self.player_1 = {
            'name': 'Chloe Alaska',
            'guardians': ['David Alaska', 'Jamie Alaska'],
            'experience': False,
            'height': 47
        }
        self.player_2 = {
            'name': 'Les Clay',
            'guardians': ['Wynonna Brown'],
            'experience': True,
            'height': 42
        }
        self.team = [self.player_1, self.player_2]

    def test_it_gets_player_names(self):
        names = get_player_names(self.team)
        expected = 'Players on team:\n  Chloe Alaska, Les Clay'
        self.assertEqual(expected, names)

    def test_it_does_not_change_original_data(self):
        player_1 = self.player_1.copy()
        player_2 = self.player_2.copy()
        team = self.team.copy()

        get_player_names(self.team)

        self.assertEqual(player_1, self.player_1)
        self.assertEqual(player_2, self.player_2)
        self.assertEqual(team, self.team)
        
