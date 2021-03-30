import unittest
from application import balance_teams


class TestBalanceTeams(unittest.TestCase):
    def setUp(self):
        self.teams = ['Panthers', 'Bandits', 'Warriors']
        self.players = [
            {
                'name': 'Herschel Krustofski',
                'experience': True
            },
            {
                'name': 'Eva Gordon',
                'experience': False
            },
            {
                'name': 'Ben Finkelstein',
                'experience': False
            },
            {
                'name': 'Joe Smith',
                'experience': True
            },
            {
                'name': 'Diego Soto',
                'experience': True
            },
            {
                'name': 'Kimmy Stein',
                'experience': False
            }
        ]
        self.num_players_team = len(self.players) / len(self.teams)

    def test_it_does_not_change_original_data(self):
        teams_data = self.teams.copy()
        players_data = self.players.copy()

        balance_teams(self.teams, self.players)

        self.assertEqual(teams_data, self.teams)
        self.assertEqual(players_data, self.players)

    def test_it_balances_teams(self):
        rosters = balance_teams(self.teams, self.players)
        self.assertEqual(dict, type(rosters))

        self.assertEqual(rosters.keys(),
                         frozenset({'Panthers', 'Bandits', 'Warriors'}))

        for roster in rosters.values():
            self.assertEqual(list, type(roster))
            self.assertEqual(self.num_players_team, len(roster))

    def test_it_puts_each_player_on_only_one_team(self):
        rosters = balance_teams(self.teams, self.players)

        panthers = list(map(lambda player: player['name'], rosters['Panthers']))
        bandits = list(map(lambda player: player['name'], rosters['Bandits']))
        warriors = list(map(lambda player: player['name'], rosters['Warriors']))

        all_unique_1 = set(panthers).isdisjoint(bandits)
        all_unique_2 = set(warriors).isdisjoint(panthers)
        all_unique_3 = set(bandits).isdisjoint(warriors)

        self.assertTrue(all_unique_1 and all_unique_2 and all_unique_3)
