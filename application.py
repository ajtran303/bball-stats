from constants import (TEAMS as teams,
                       PLAYERS as players)

from itertools import islice


def clean_data(player):
    player = player.copy()
    player['experience'] = _convert_experience(player['experience'])
    player['height'] = _convert_height(player['height'])
    return player


def _convert_height(height):
    return int(height.partition(' ')[0])


def _convert_experience(experience):
    if experience == 'YES':
        return True
    elif experience == 'NO':
        return False


def balance_teams(teams, players):
    team_size = int(len(players) / len(teams))
    rosters = {}

    for index, team in enumerate(teams):
        rosters[team] = list()

        start = int(team_size * index)
        end = start + team_size
        for player in islice(players, start, end):
            rosters[team].append(player)

    return rosters


if __name__ == '__main__':
    pass
