from constants import (TEAMS as teams,
                       PLAYERS as players)

from itertools import islice


def clean_data(player):
    player = player.copy()
    player['experience'] = convert_experience(player['experience'])
    player['height'] = convert_height(player['height'])
    return player


def convert_height(height):
    return int(height.partition(' ')[0])


def convert_experience(experience):
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

    def main():
        cleaned_players = list(map(lambda player: clean_data(player), players))
        rosters = balance_teams(teams, cleaned_players)
        print('Welcome to the Basketball Stats tool!')
        show_menu(rosters)


    def show_menu(rosters):
        while True:
            print('MAIN MENU\n\nA) Display Team Stats\nB) Quit\n')
            menu_option = input("Enter an option:\n").upper()
            if menu_option not in 'AB':
                print('That is not a valid option!\n')
            elif menu_option == 'B':
                print('Goodbye!')
                break
            elif menu_option == 'A':
                team = get_team()
                show_stats(team, rosters[team])
                input('Press Any key to return to main menu:\n')


    def get_team():
        teams = {'A': 'Panthers', 'B': 'Bandits', 'C': 'Warriors'}
        team = None
        while team is None:
            print('\nSELECT TEAM:\nA) Panthers\nB) Bandits\nC) Warriors\n')
            team_option = input("Enter an option:\n")
            try:
                team = teams[team_option.upper()]
            except KeyError:
                print('That is not a valid option!\n')
        return team


    def show_stats(team_name, roster):
        title = f'Team Stats: {team_name}'
        names = list(map(lambda player: player['name'], roster))
        print('\n' + title + '\n' + '-'*len(title) + '\n'
              f'Total players: {len(roster)}\n\n' +
              'Players on team:\n' +
              '  ' + ', '.join(names) + '\n')


    main()
