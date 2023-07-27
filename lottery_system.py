import random

# Number of Players that will play the game
def get_player_num():
    num = ''
    while num.isdigit() == False or int(num) < 6:
        num = input('Enter the number of players that would like to play: ')
        if num.isdigit() == False:
            print('Sorry, but you did not enter an integer. Please try again.')
        elif int(num) < 6:
            print('Please enter at least 6')
    return int(num)

# Getting 3 integers from each Players
def get_num_list(player_num, range_num):
    num_list = []
    for i in range(range_num):
        while True:
            player_input = input(f"Enter integer {i+1} for player {player_num}: ")
            if not player_input.isdigit():
                print("Invalid input! Please enter an integer.")
            else:
                num = int(player_input)
                if 1 <= num <= 100:
                    num_list.append(num)
                    break
                else:
                    print("Invalid input! Please enter an integer between 1 and 100.")
    return num_list


# Getting the stake value from each Players
def get_stake_input(prompt):
    while True:
        try:
            player_input = int(input(prompt))
            return player_input
        except ValueError:
            print("Invalid input! Please enter an integer.")


# Generating Players data
def gen_player_data_list():
    player_nums = get_player_num()
    players_data = []
    for i in range(1,player_nums + 1):
        num_list = get_num_list(i, 3)
        stake_value = get_stake_input(f"Enter stake value for player {i}: ")
        players_data.append({
            'player_id': i,
            'num_list': num_list,
            'stake_value': stake_value
        })
    return players_data

players_data_list = gen_player_data_list()

# Getting random lucky numbers
def get_lucky_nums():
    lucky_nums = []
    for i in range(3):
        lucky_nums.append(random.randint(1, 100))
    return lucky_nums

lucky_nums = get_lucky_nums()

# Checking if there's any winner
def check_winner():
    winner = []
    for player in players_data_list:
        player_num_set = set(player['num_list'])
        lucky_num_set = set(lucky_nums)
        if len(player_num_set.intersection(lucky_num_set)) >=2:
            print(f"Congratulations!!!!\nPlayer {player['player_id']} won!!!!")
            winner.append(player)
    return winner 


def get_winner():
    winners_list = check_winner()
    pool = sum([player['stake_value'] for player in players_data_list])
    if len(winners_list) >= 1:
        average = pool / len(winners_list)
        for winner in winners_list:
            print(f"Player {winner['player_id']} won {average}")
    elif len(winners_list) == 0:
        print(f'The house won the {pool}')

get_winner()

