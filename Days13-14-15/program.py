from game_classes import Player, Roll
import random

def main():
    print_header()

    rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, rolls)

def game_loop(player1, player2, rolls):
    count = 0
    while count < 3:
        p2_roll = random.choice(rolls)
        p1_roll = Roll(input('\nplease choose rock, paper or scissors: '))
        while p1_roll.my_roll not in rolls:
            p1_roll = Roll(input('\nplease choose rock, paper or scissors: '))

        outcome = p1_roll.can_defeat(p2_roll)

        # display throwsPJ
        print(f'\n{player1.name} chooses: {p1_roll.my_roll}, {player2.name} chooses: {p2_roll}')
        # display winner for this round
        if outcome:
            print(f'{player1.name} wins this round!')
            player1.score += 1
        else:
            if p1_roll.my_roll == p2_roll:
                print('This round is a tie!')
            else:
                print(f'{player2.name} wins this round!')
                player2.score += 1
        count +=1
    
    # Compute who won
    print('\n')
    if player1.score > player2.score:
        print(f'{player1.name} wins {player1.score} to {player2.score} points!')
    elif player1.score < player2.score:
        print(f'{player2.name} wins {player2.score} to {player1.score} points!')
    else:
        print(f'It\'s a tie')

        
def print_header():
    print('--------------------------------')
    print('    Rock, Paper, Scissors')
    print('--------------------------------')

def build_the_three_rolls():
    return ['rock', 'paper', 'scissors']

def get_players_name():
    return input('Hi player! Please enter your name: ')

if __name__ == "__main__":
    main()