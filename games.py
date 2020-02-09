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



#Call your game of chance functions here


heads_or_tails()
cho_han()

print(money)
