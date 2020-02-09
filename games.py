import random

money = 100

#Write your game of chance functions here
"""
num = random.randint(1,10)
print(num)
"""

def heads_or_tails():
    global money
    call = input("Do you call heads, or tails? ")
    bet = input("How much would you like to bet? ")
    bet_int = int(bet)
    if bet_int > money:
        print("You don't have that much money to bet!")
        heads_or_tails()
#    print(call)
    if call == "heads" or call == "tails":
#        print("you called something")
        flip = random.randint(0,1)
        options = ["heads", "tails"]
        if options[flip] == call:
            print("You called it correctly!")
            print("You win money!")
            money += bet_int
        else:
            print("You got it wrong!")
            print("You lose money!")
            money -= bet_int
        print("you have {0} dollars".format(money))
        return money 
    else:
        print("You have to call heads or tails!")
        heads_or_tails()


def cho_han():
    global money
    call = input("Which do you guess, odd or even? ")
    bet = input ("How much would you like to bet? ")
    bet_int = int(bet)
    if bet_int > money:
        print("You don't have that much money to bet!")
        cho_han() 
    die_one = random.randint(1,6)
    die_two = random.randint(1,6)
    total = (die_one + die_two) % 2
    determiner = ['even', 'odd']
    if call == "even" or call == "odd":   
        if call == determiner[total]:
            print("You guessed correctly! You win {0} dollars!".format(bet_int))
            money += bet_int
            return money
        else:
            print("You guessed incorrectly! You lose {0} dollars!".format(bet_int))
            money -= bet_int
            return money
        print("You have {0} dollars now.".format(money))
    else:
        print("You have to call even or odd!")
        cho_han()

def deck_of_cards():
    global money
    bet = input("How much would you like to bet? ")
    bet_int = int(bet)
    if bet_int > money:
        print("You don't have that much money to bet!")
        deck_of_cards()
    else: 
        deck = []
        for suit in range(1,5):
            for card in range(1,14):
                deck.append(card)
#    print(deck)
#    print(len(deck))
        card_one_index = random.randint(1,len(deck))
        card_one = deck.pop(card_one_index)
        card_two_index = random.randint(1,len(deck))
        card_two = deck.pop(card_two_index)
        print("You got {0}, while the other guy got {1}".format(card_one, card_two))
        if card_one > card_two:
            money += bet_int
            print("You now have {0} dollars!".format(money))
            return money
        elif card_one == card_two:
            print("You tied! Nobody wins!")
        else:
            money -= bet_int
            print("You now have {0} dollars!".format(money))
            return money


    
#Call your game of chance functions here

x =  "y"
while x =="y":
    x = input("Would you like to play a game? y or n? ")
    if x == "y":
        print("You have {0} money left...".format(money))
        print("Which game?")
        print("Heads or Tails [h/t], Cho Han [ch], or Cards [c]?")
        selection = input()
        if selection == "h/c":
            heads_or_tails()
        elif selection == "ch":
            cho_han()
        elif selection == "c":
            deck_of_cards()
        else:
            print("Are you sure you want to play a game? Try picking again...")
    elif x == "n":
        print("You\'re leaving with {0} dollars!".format(money))
        print("Thanks for coming to Nick\'s casino!")
    else:
        print("That's not a valid selection, try again!")
        x = "y"


#heads_or_tails()
#cho_han()
