from random import randint


class fiftyfiveby2():
    def __init__(self, coins):
        print(f"Welcome to 55x2! This is the game where we roll a 100 sided die!\nIf you roll greater than 55 you double your coins!\nYou are currently gambling {coins} coins.")
        usercoins = coins

        userinput = input("Are you ready to lock in your bet? Y/N: ").upper()
        if userinput == "Y":
            roll = randint(1, 100)
            if roll > 55:
                usercoins = (usercoins*2)
                print(f"You rolled a {roll} congrats you now have {usercoins} coins!")
            else:
                print(f"You rolled a {roll} sorry you lost :(")
        else:
            print("Bye!")


class blackjack():
    def __init__(self, coins):
        print("Welcome to blackjack! Black jack normally is to 21, but on this game you're trying to get the closest to 100 without a bust\nA bust is when you Rolling over 100 with your combined rolls")

        usercoins = coins
        totalroll = 0
        currentRoll = 0

        BOTtotalroll = 0
        BOTcurrentroll = 0
        hitorstay = "h"

        userinput = input("Are you ready to lock in your bet? Y/N: ").upper()
        if userinput == 'Y':

            while hitorstay == "h" and totalroll < 100:
                currentRoll = randint(1, 100)
                totalroll = totalroll + currentRoll
                print(f"You rolled a {currentRoll}")
                print(f"Your total at the moment is {totalroll}")
                if totalroll < 100:
                    hitorstay = input("HIT or STAY (h/s)?: ")
                else:
                    print("You busted bad luck!")
                    exit()
            print("Bot will play his turn now...")
            hitorstay = "h"

            while hitorstay == "h" and BOTtotalroll < 100:
                BOTcurrentRoll = randint(1, 100)
                BOTtotalroll = BOTtotalroll + BOTcurrentRoll
                print(f"BOT rolled a {BOTcurrentRoll}")
                print(f"BOT total at the moment is {BOTtotalroll}")
                if BOTtotalroll < totalroll:
                    hitorstay = "h"
                elif BOTtotalroll > totalroll:
                    hitorstay = "s"
                else:
                    print("BOT busted bad luck!")

            if totalroll > BOTtotalroll:
                print("You have won!")
            elif (BOTtotalroll > totalroll) and (BOTtotalroll > 100):
                print("YOU HAVE WON! (the bot busted)")
            else:
                print("You have lost! Better next time!")


askgame = int(
    input("What game you want to play?\n(1) 55 x 2 \n(2) blackjack\n"))
userinput = int(input("How many coins are you going to gamble?: "))

if askgame == 1:
    fiftyfiveby2(userinput)
elif askgame == 2:
    blackjack(userinput)


print("THANKS FOR PLAYING!")
