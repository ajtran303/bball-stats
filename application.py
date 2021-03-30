from constants import (TEAMS as teams,
                       PLAYERS as players)

from itertools import islice
from statistics import mean


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
    experienced = get_experienced_players(players)
    inexperienced = get_inexperienced_players(players)

    rosters = {}

    for index, team in enumerate(teams):
        rosters[team] = list()

        for players_by_experience in [experienced, inexperienced]:
            team_limit = int(len(players_by_experience) / len(teams))
            start = int(team_limit * index)
            end = start + team_limit

            for player in islice(players_by_experience, start, end):
                rosters[team].append(player)

    return rosters


def get_player_names(players):
    names = list(map(lambda player: player['name'], players))
    return ', '.join(names)


def get_guardians(players):
    guards = list(map(lambda player: ', '.join(player['guardians']), players))
    return ', '.join(guards)


def get_experienced_players(players):
    return list(filter(lambda player: player['experience'] is True, players))


def get_inexperienced_players(players):
    return list(filter(lambda player: player['experience'] is False, players))


def get_average_height(players):
    heights = list(map(lambda player: player['height'], players))
    return mean(heights)




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
              f'Total players: {len(roster)}\n' +
              f'Total experienced: {len(get_experienced_players(roster))}\n' +
              f'Total inexperienced: {len(get_inexperienced_players(roster))}\n' +
              f'Average height: {round(get_average_height(roster), 2)}\n\n' +
              f'Players on team:\n  {get_player_names(roster)}\n\n' +
              f'Guardians:\n  {get_guardians(roster)}' +
              '\n')


    main()
