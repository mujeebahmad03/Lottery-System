import random

RULE_OPTION = 1
PLAY_OPTION = 2

# Display the rules of the game
def display_rules():
    rules = f"""
----------WELCOME TO ELITE LOTTERY GAME----------

RULES:
- You must stake before you play.
- You need at least 6 players to play.
- Choose 3 unique numbers between 1 and 100.
- To win, you must match at least 2 numbers.

Press {PLAY_OPTION} to start the game.
    """
    print(rules)

# Ask players for input
def get_integer_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Please enter a valid number greater than or equal to {min_val}.")
            elif max_val is not None and value > max_val:
                print(f"Please enter a valid number less than or equal to {max_val}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Gets the number of players that wants to play
def get_player_num():
    return get_integer_input("Enter the number of players that would like to play (minimum 6): ", min_val=6)

# Gets the numbers of each player
def get_num_list(player_num):
    print(f"\nEnter three unique numbers (1 to 100) for player {player_num}:")
    num_list = []
    for i in range(3):
        while True:
            num = get_integer_input(f"Enter a number {i+1}: ", min_val=1, max_val=100)
            if num in num_list:
                print("Please enter a unique number.")
            else:
                num_list.append(num)
                break
    return num_list

# Get stake amount
def get_stake_input(prompt):
    return get_integer_input(prompt, min_val=1)

# Generates 3 random lucky number
def generate_random_nums():
    return [random.randint(1, 100) for _ in range(3)]

# Checks for winner
def check_winner(players_data_list, lucky_nums):
    winners = []
    for player in players_data_list:
        player_num_set = set(player['num_list'])
        lucky_num_set = set(lucky_nums)
        if len(player_num_set.intersection(lucky_num_set)) >= 2:
            print(f"\nCongratulations! Player {player['player_id']} won!")
            winners.append(player)
    return winners

# Displays winner
def get_winner(winners_list, total_pool):
    if len(winners_list) >= 1:
        total_stake = sum(winner['stake_value'] for winner in winners_list)
        print("\nWinners:")
        for winner in winners_list:
            stake_proportion = winner['stake_value'] / total_stake
            stake_won = stake_proportion * total_pool
            print(f"Player {winner['player_id']} won {stake_won:.2f}")
    else:
        print("\nNo winner. The house won the pool.")

def main():
    while True:
        display_rules()
        user_choice = get_integer_input("> ", RULE_OPTION, PLAY_OPTION)
        if user_choice == PLAY_OPTION:
            player_nums = get_player_num()
            players_data_list = []
            total_pool = 0
            for i in range(1, player_nums + 1):
                stake_value = get_stake_input(f"Enter stake value for player {i}: ")
                num_list = get_num_list(i)
                total_pool += stake_value
                players_data_list.append({
                    'player_id': i,
                    'stake_value': stake_value,
                    'num_list': num_list
                })

            lucky_nums = generate_random_nums()
            print("\nLucky Numbers:", lucky_nums)

            winners_list = check_winner(players_data_list, lucky_nums)
            get_winner(winners_list, total_pool)

        else:
            print("Invalid choice. Please choose again.")

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            break

main()
