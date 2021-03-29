from constants import (TEAMS as teams,
                       PLAYERS as players)


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


if __name__ == '__main__':
    pass
