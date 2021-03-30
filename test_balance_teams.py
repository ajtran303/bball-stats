import unittest
from application import balance_teams


class TestBalanceTeams(unittest.TestCase):
    def setUp(self):
        self.teams = ['Panthers', 'Bandits', 'Warriors']
        self.players = list(map(lambda x: f'Player {str(x)}', range(1, 19)))
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

        all_unique_1 = set(rosters['Panthers']).isdisjoint(rosters['Bandits'])
        all_unique_2 = set(rosters['Warriors']).isdisjoint(rosters['Panthers'])
        all_unique_3 = set(rosters['Bandits']).isdisjoint(rosters['Warriors'])

        self.assertTrue(all_unique_1 and all_unique_2 and all_unique_3)
