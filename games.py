import random

money = 100

#Write your game of chance functions here

def coin_flip(bet, guess): 
    if bet <= 0:
        print("Your bet must be greater than $0. Please try again.\n")
        return 0

    elif bet > money:
        print("You don't have that much money. Please try again.\n")
        return 0

    else:
        print('Let\'s flip a coin!')
        num = random.randint(1, 2)
        if num == 1 and guess == 'Heads':
            print('You have betted $' + str(bet) + ' on this game!\n\n'+ 'You guessed heads!\n' + 'The outcome was heads!') 
            bet *= 1
            print('You won the bet! You earned $' + str(bet * 2) + '!\n')
            return bet

        elif num == 1 and guess == 'Tails':
            print('You have betted $' + str(bet) + ' on this game!\n\n'+ 'You guessed heads!\n' + 'The outcome was tails!') 
            bet *= -1
            print('You lost the bet! You lost $' + str(bet) + '!\n')
            return bet

        elif num == 2 and guess == 'Heads':
            print('You have betted $' + str(bet) + ' on this game!\n\n'+ 'You guessed tails!\n' + 'The outcome was heads!') 
            bet *= -1
            print('You lost the bet! You lost $' + str(bet) + '!\n')
            return bet

        elif num == 2 and guess == 'Tails':
            print('You have betted $' + str(bet) + ' on this game!\n\n'+ 'You guessed tails!\n' + 'The outcome was tails!') 
            bet *= 1
            print('You won the bet! You earned $' + str(bet * 2) + '!\n')
            return bet



def cho_han(bet, guess):
    print('Let\'s play Cho-Han!')
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    num = (dice1 + dice2) % 2
     
    if bet <= 0:
        print("Your bet must be greater than $0. Please try again.\n")
        return 0

    elif bet > money:
        print("You don't have that much money. Please try again.\n")
        return 0

    else:
        if num != 0 and guess == 'Odd':
            print('You have betted $' + str(bet) + ' on this game!\n\n'+ 'You guessed odd!\n' + 'The outcome was odd!') 
            bet *= 1
            print('You won the bet! You earned $' + str(bet * 2) + '!\n')
            return bet
        
        elif num != 0 and guess == 'Even':
            print('You have betted $' + str(bet) + ' on this game!\n\n'+ 'You guessed even!\n' + 'The outcome was odd!') 
            bet *= -1
            print('You lost the bet! You lost $' + str(bet) + '!\n')
            return bet
        
        elif num == 0 and guess == 'Odd':
            print('You have betted $' + str(bet) + ' on this game!\n\n'+ 'You guessed odd!\n' + 'The outcome was even!') 
            bet *= -1
            print('You lost the bet! You lost $' + str(bet) + '!\n')
            return bet

        elif num == 0 and guess == 'Even':
            print('You have betted $' + str(bet) + ' on this game!\n\n'+ 'You guessed even!\n' + 'The outcome was even!') 
            bet *= 1
            print('You won the bet! You won $' + str(bet * 2) + '!\n')
            return bet
        
def card_game(bet):
    print('Let\'s play a card game!')
    hearts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    diamonds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    clubs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    spades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    deck = hearts + diamonds + clubs + spades

    player_1_card = random.choice(deck)
    player_2_card = random.choice(deck)

    if bet <= 0:
        print("Your bet must be greater than $0. Please try again.\n")
        return 0

    elif bet > money:
        print("You don't have that much money. Please try again.\n")
        return 0

    else:
        if player_1_card > player_2_card:
            print('You have betted $' + str(bet) + ' on this game!\n\n'+ 'Your card is ' + str(player_1_card) + '!\n' + 'The opponent\'s card is ' + str(player_2_card) + '!') 
            bet *= 1
            print('You won the bet! You earned $' + str(bet * 2) + '!\n')
            return bet
        
        elif player_1_card < player_2_card:
            print('You have betted $' + str(bet) + ' on this game!\n\n'+ 'Your card is ' + str(player_1_card) + '!\n' + 'The opponent\'s card is ' + str(player_2_card) + '!') 
            bet *= -1
            print('You lost the bet! You lost $' + str(bet) + '!\n')
            return bet
        
        elif player_1_card == player_2_card:
            print('You have betted $' + str(bet) + ' on this game!\n\n'+ 'Your card is ' + str(player_1_card) + '!\n' + 'The opponent\'s card is ' + str(player_2_card) + '!') 
            bet *= 0
            print('It was a tie! You won nothing.\n')
            return bet

def roulette(bet, guess):
    print('Let\'s play roulette!')
    outcome_number = random.randint(0, 37)

    if bet <= 0:
        print("Your bet must be greater than $0. Please try again.\n")
        return 0

    elif bet > money:
        print("You don't have that much money. Please try again.\n")
        return 0

    else:
        # generate a random number between 0 to 37, inclusive. if number is 37, the number should be changed to 00
        result = random.randint(0, 37)
        # check if guess, 'even' is equal to even, return 1x bet. if number is 0, player shouldnt win
        if guess == 'Even' and result % 2 == 0 and result != 0:
            print('You have betted $' + str(bet) + ' on this game!\n\n' + 'You guessed that the result would be even!\n' + 'The outcome was ' + str(result) + ', an even number!')
            bet *= 1
            print('You won the bet! You earned $' + str(bet) + '!\n')
            return bet

        # check if guess, 'odd' is equal to odd, return 1x bet. if number is 37, player shouldnt win.
        elif guess == 'Odd' and result % 2 != 0 and result != 37:
            print('You have betted $' + str(bet) + ' on this game!\n\n' + 'You guessed that the result would be odd!\n' + 'The outcome was ' + str(result) + ', an odd number!')
            bet *= 1
            print('You won the bet! You earned $' + str(bet) + '!\n')
            return bet

        # check if guess number is equal to outcome number, return 35x bet.
        elif guess == result:
            print('You have betted $' + str(bet) + ' on this game!\n\n'+ 'You guessed ' + str(guess) + '!\n' + 'The outcome was ' + str(outcome_number) + '!') 
            bet *= 35
            print('You won the bet! You earned $' + str(bet) + '!\n')
            return bet

        # create else for losses.
        else:
            if type(guess) is int:
                print('You guessed ' + str(guess) + '!\n' + 'The outcome was ' + str(outcome_number) + '!\n')
            elif guess == 'Odd':
                print('You have betted ' + str(bet) + ' on this game!\n\n' + 'You guessed that the result would be odd!\n' + 'The outcome was ' + str(result) + ', an even number!')
            elif guess == 'Even':
                print('You have betted ' + str(bet) + ' on this game!\n\n' + 'You guessed that the result would be even!\n' + 'The outcome was ' + str(result) + ', an odd number!')
            bet *= -1
            print('You lost the bet! You lost $' + str(bet) + '!\n')
            return bet
       

def cash_check():
    print('You have $' + str(money) + ' cash.\n\n')


#Call your game of chance functions here

money += coin_flip(10, 'Heads')
cash_check()
money += cho_han(10, 'Odd')
cash_check()
money += card_game(10)
cash_check()
money += roulette(10, 15)
cash_check()
money += roulette(10, 'Even')
cash_check()
money += roulette(10, 'Odd')
cash_check()
