from random import randint

def win():
    print ('You win!')

def lose():
    print ('You lose!')

while True:
    player = input('What do you pick? (rock, paper, scissors)')
    player.strip()
    random_move = randint(0, 2)
    moves = ['rock', 'paper', 'scissors']
    comp = moves[random_move]

    if player == comp:
        print ('Draw!')
    elif player  == ('rock') and comp == ('scissors'):
        print("win")
    elif player == ('paper') and comp == ('scissors'):
        print('lose')
    elif player == ('scissors') and comp == ('paper'):
        print('win')
    elif player == ('scissors') and comp == ('rock'):
        print('lose')
    elif player == ('paper') and comp == ('rock'):
        print('win')
    elif player == ('rock') and comp == ('paper'):
        print('lose')
    again = input('Do you want to play again? (y or n)').strip()
    if again == ('n'):
        break


