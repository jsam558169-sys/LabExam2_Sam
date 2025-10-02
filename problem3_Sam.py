import random

# generate 6 numbers
def draw_winning_numbers():
    return sorted(random.sample(range(1, 61), 6))

# check matches
def check_card(player_name, player_card, winning_numbers):
    matches = set(player_card).intersection(set(winning_numbers))
    match_count = len(matches)

    # compute prizes
    if match_count == 6:
        print(f"Congratulations, Jackpot prize!! {player_name}'s card {player_card} has 6 matched numbers. "
              f"You won 1 million pesos!!\n")
    elif match_count > 0:
        prize = match_count * 1000
        print(f"{player_name}'s card {player_card} has {match_count} matched numbers {matches}. "
              f"You won {prize} pesos!\n")
    else:
        print(f"{player_name}'s card {player_card}: No match!!\n")

# main menu
if __name__ == "__main__":
    # draw winning numbers
    winning_numbers = draw_winning_numbers()
    print(f"\nWinning numbers: {winning_numbers}\n")

    players = {}

    # how many players will join
    num_players = int(input("Enter number of players: "))

    for i in range(num_players):
        name = input(f"\nEnter name of player {i+1}: ")
        print("Enter 6 numbers between 1 and 60 (separated by spaces): ")
        numbers = list(map(int, input().split()))

        # validate input
        while len(numbers) != 6 or any(n < 1 or n > 60 for n in numbers):
            print("Invalid input!! Please enter exactly 6 numbers between 1 and 60.")
            numbers = list(map(int, input().split()))

        players[name] = numbers
    print("\n||||| RESULTS |||||\n")
    for name, card in players.items():
        check_card(name, card, winning_numbers)