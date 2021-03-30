from constants import (TEAMS as teams,
                       PLAYERS as players)

from itertools import islice


def clean_data(player):
    player = player.copy()
    player['experience'] = convert_experience(player['experience'])
    player['height'] = convert_height(player['height'])
    player['guardians'] = convert_guardians(player['guardians'])
    return player


def convert_height(height):
    return int(height.partition(' ')[0])


def convert_experience(experience):
    if experience == 'YES':
        return True
    elif experience == 'NO':
        return False


def convert_guardians(guardians):
    return guardians.split(' and ')


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


def get_player_names(players):
    names = list(map(lambda player: player['name'], players))
    return f'Players on team:\n  {", ".join(names)}'


def get_guardians(players):
    guardians = list(map(lambda player: ', '.join(player['guardians']), players))
    return f'Guardians:\n  {", ".join(guardians)}'


def get_experienced_players(players):
    return list(filter(lambda player: player['experience'] is True, players))


def get_inexperienced_players(players):
    return list(filter(lambda player: player['experience'] is False, players))


if __name__ == '__main__':

    def main():
        cleaned_players = list(map(lambda player: clean_data(player), players))
        rosters = balance_teams(teams, cleaned_players)
        print('Welcome to the Basketball Stats tool!')
        show_menu(rosters)


    def show_menu(rosters):
        while True:
            print('MAIN MENU\n\n1) Display Team Stats\n2) Quit\n')
            menu_option = input("Enter an option:\n")
            if menu_option not in '12':
                print('That is not a valid option!\n')
            elif menu_option == '2':
                print('Goodbye!')
                break
            elif menu_option == '1':
                team = get_team()
                show_stats(team, rosters[team])
                input('Press Any key to return to main menu:\n')


    def get_team():
        teams = {'1': 'Panthers', '2': 'Bandits', '3': 'Warriors'}
        team = None
        while team is None:
            print('\nSELECT TEAM:\n1) Panthers\n2) Bandits\n3) Warriors\n')
            team_option = input("Enter an option:\n")
            try:
                team = teams[team_option]
            except KeyError:
                print('That is not a valid option!\n')
        return team


    def show_stats(team_name, roster):
        title = f'Team Stats: {team_name}'
        print('\n' + title + '\n' + '-'*len(title) + '\n' +
              f'Total players: {len(roster)}\n\n' +
              f'{get_player_names(roster)}\n\n' +
              f'{get_guardians(roster)}' +
              '\n')


    main()
