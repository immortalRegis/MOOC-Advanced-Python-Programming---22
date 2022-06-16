# Write your solution here
import json

def search_for_player(name: str, player_info: list):
    player = [pl for pl in player_info if pl['name'] == name]
    if len(player) != 0:
        player_in_correct_format(player[0])

def player_in_correct_format(player:dict):
        player_name = player['name']
        team = player['team']
        goals = player['goals']
        assists = player['assists']
        ga = goals + assists
        print(f'{player_name:21}{team:5}{goals:2} +{assists:3} = {ga:3}')


def print_teams(passed_data:list):
    teams = [pd['team'] for pd in passed_data]
    unique_teams = list(set(teams))
    unique_teams.sort()
    for ut in unique_teams:
        print(ut)

def print_countries(passed_data:list):
    countries = [pd['nationality'] for pd in passed_data]
    unique_countries = list(set(countries))
    unique_countries.sort()
    for uc in unique_countries:
        print(uc)

def get_info_for_team(team_name: str, general_info:list):
    players_in_team = [player_info for player_info in general_info if player_info['team'] == team_name]
    ranked_players = sorted(players_in_team, key= lambda player: player['goals'] + player['assists'], reverse=True)
    for player in ranked_players:
        player_in_correct_format(player)


def get_info_for_country(country:str, general_info:list):
    players_from_country = [player_info for player_info in general_info if player_info['nationality'] == country]
    ranked_players = sorted(players_from_country, key= lambda player: player['goals'] + player['assists'], reverse=True)
    for player in ranked_players:
        player_in_correct_format(player)

def get_player_rankings(number:int, general_info:list):
    ranked_list = sorted(general_info.copy(), key=lambda player_info: ((player_info['goals'] + player_info['assists']), player_info['goals']), reverse= True)
    for i in range(number):
        player_in_correct_format(ranked_list[i])

def get_goal_ranking(number:int, general_info:list):
    ranked_list = sorted(general_info.copy(), key= lambda player_info:(player_info['goals'], -player_info['games']), reverse=True)
   #use '-' in the 'games' ranking to reverse the order. Neat trick! 
    for i in range(number):
        player_in_correct_format(ranked_list[i])

#main app starts here
file_name = input('file name: ')
with open(file_name) as my_file:
    raw_data = my_file.read()

info = json.loads(raw_data)
info = list(info)
print(f'read the data of {len(info)} players')

print('commands:')
print('0 quit')
print('1 search for player')
print('2 teams')
print('3 countries')
print('4 players in team')
print('5 players from country')
print('6 most points')
print('7 most goals')

while(True):
    print()
    command = input('command: ')
    if command == '0':
        break
    elif command == '1':
        name = input('name: ')
        print()
        search_for_player(name, info)
    elif command == '2':
        print_teams(info)
    elif command == '3':
        print_countries(info)
    elif command == '4':
        team_name = input('team: ')
        print()
        get_info_for_team(team_name, info)
    elif command == '5':
        country = input('country: ')
        print()
        get_info_for_country(country, info)
    elif command == '6':
        number = int(input('how many: '))
        print()
        get_player_rankings(number, info)
    elif command == '7':
        number = int(input('how many: '))
        print()
        get_goal_ranking(number, info)
    else:
        continue


        
    
