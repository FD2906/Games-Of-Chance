import random

money = 100

#Write your game of chance functions here

def coin_flip(bet, guess): 
    if bet <= 0:
        print("Your bet must be greater than zero. Please try again.\n")

    elif bet > money:
        print("You don't have that much money. Please try again.\n")

    else:
        num = random.randint(1, 2)
        if num == 1 and guess == 'Heads':
            print('You have betted ' + str(bet) + ' on this game!\n\n'+ 'You guessed heads!\n' + 'The outcome was heads!') 
            bet *= 1
            print('You won the bet! You earned ' + str(bet) + '!')
            return bet

        elif num == 1 and guess == 'Tails':
            print('You have betted ' + str(bet) + ' on this game!\n\n'+ 'You guessed heads!\n' + 'The outcome was tails!') 
            bet *= -1
            print('You lost the bet! You lost ' + str(bet) + '!')
            return bet

        elif num == 2 and guess == 'Heads':
            print('You have betted ' + str(bet) + ' on this game!\n\n'+ 'You guessed tails!\n' + 'The outcome was heads!') 
            bet *= -1
            print('You lost the bet! You lost ' + str(bet) + '!')
            return bet

        elif num == 2 and guess == 'Tails':
            print('You have betted ' + str(bet) + ' on this game!\n\n'+ 'You guessed tails!\n' + 'The outcome was tails!') 
            bet *= 1
            print('You won the bet! You earned ' + str(bet) + '!')
            return bet



def cho_han(bet, guess):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    num = (dice1 + dice2) % 2
     
    if bet <= 0:
        print("Your bet must be greater than zero. Please try again.\n")

    elif bet > money:
        print("You don't have that much money. Please try again.\n")

    else:
        if num != 0 and guess == 'Odd':
            print('You have betted ' + str(bet) + ' on this game!\n\n'+ 'You guessed odd!\n' + 'The outcome was odd!') 
            bet *= 1
            print('You won the bet! You earned ' + str(bet) + '!')
            return bet
        
        elif num != 0 and guess == 'Even':
            print('You have betted ' + str(bet) + ' on this game!\n\n'+ 'You guessed even!\n' + 'The outcome was odd!') 
            bet *= -1
            print('You lost the bet! You lost ' + str(bet) + '!')
            return bet
        
        elif num == 0 and guess == 'Odd':
            print('You have betted ' + str(bet) + ' on this game!\n\n'+ 'You guessed odd!\n' + 'The outcome was even!') 
            bet *= -1
            print('You lost the bet! You lost ' + str(bet) + '!')
            return bet

        elif num == 0 and guess == 'Even':
            print('You have betted ' + str(bet) + ' on this game!\n\n'+ 'You guessed even!\n' + 'The outcome was even!') 
            bet *= 1
            print('You won the bet! You won ' + str(bet) + '!')
            return bet
        


def cash_check():
    print('You have ' + str(money) + ' cash.')


#Call your game of chance functions here
money += coin_flip(50, 'Heads')
cash_check()
money += cho_han(50, 'Odd')
cash_check()
