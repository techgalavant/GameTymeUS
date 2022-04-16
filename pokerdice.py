#!/usr/bin/env python2
# Poker Dice Game

import random
from itertools import groupby

from pip._vendor.distlib.compat import raw_input

nine = 1
ten = 2
jack = 3
queen = 4
king = 5
ace = 6

names = {nine: "9", ten: "10", jack: "J", queen: "Q", king: "K", ace: "A"}

player_score = 0
computer_score = 0


def start():
    print("Let's play some Poker Dice.")
    while game():
        pass
    scores()


def game():
    print("The computer will help you throw 5 dice.")
    throws()
    return play_again()


def throws():
    roll_number = 5
    dice = roll(roll_number)
    # Sort the dice list so that all the numbers are in ascending order.
    #  dice = dice[0:1] + sorted(dice[1:])
    #  dice.sort()  
    for i in range(len(dice)):
        print("Dice", i + 1, ":", names[dice[i]])

    result = hand(dice)
    print("You currently have", result, ".")

# Ensure the input is an integer value between 1-5
# Reference https://www.tutorialsteacher.com/articles/convert-input-to-number-in-python
    while True:
        rerolls = int(input("How many dice do you want to throw again? "))
        try:
            if rerolls in (1, 2, 3, 4, 5):
                break
        except ValueError:
            pass
        print("Oops! I didn't understand that. Please enter a value between 1-5.")
    if rerolls == 0:
        print("You finish with", result, ".")
    else:
        roll_number = rerolls
        dice_rerolls = roll(roll_number)
        dice_changes = range(rerolls)
        print("Enter the number of a dice to reroll: ")
        iterations = 0
        while iterations < rerolls:
            iterations = iterations + 1
            while True:
                selection = int(input(""))  # Important: ensure this input is an integer.
                try:
                    if selection in (1, 2, 3, 4, 5):
                        break
                except ValueError:
                    pass
                print("Oops! You must enter a number between 1-5.")
            itval = iterations - 1
            dice_changes[itval] = selection - 1
            print("You have changed dice", selection)

        iterations = 0
        while iterations < rerolls:
            iterations = iterations + 1
            replacement = dice_rerolls[iterations - 1]
            dice[dice_changes[iterations - 1]] = replacement

        # Re-sort the dice list so that all the numbers are in ascending order.
        #  dice = dice[0:1] + sorted(dice[1:])
        #  dice.sort()
        for i in range(len(dice)):
            print("Dice", i + 1, ":", names[dice[i]])

        result = hand(dice)
        print("You finish with", result, ".")


def roll(roll_number):
    numbers = range(1, 7)
    dice = range(roll_number)
    iterations = 0
    while iterations < roll_number:
        iterations = iterations + 1
        dice = random.choice(numbers)
        #  dice[iterations-1] = random.choice(numbers)
    return dice


def hand(dice):
    dice_hand = [len(list(group)) for key, group in groupby(dice)]
    dice_hand.sort(reverse=True)
    straight1 = [1, 2, 3, 4, 5]
    straight2 = [2, 3, 4, 5, 6]

    if dice == straight1 or dice == straight2:
        return "a straight!"
    elif dice_hand[0] == 5:
        return "five of a kind!"
    elif dice_hand[0] == 4:
        return "four of a kind!"
    elif dice_hand[0] == 3:
        if dice_hand[1] == 2:
            return "a full house!"
        else:
            return "three of a kind!"
    elif dice_hand[0] == 2:
        if dice_hand[1] == 2:
            return "two pair!"
        else:
            return "a single pair!"
    else:
        return "a high card."


def play_again():
    answer = raw_input("Would you like to play again? y/n: ")
    if answer in ("y", "Y", "yes", "Yes", "Sure", "sure", "OK", "ok", "okay"):
        return answer
    else:
        print("Thank you for playing! See you next time!")


def scores():
    global player_score, computer_score
    print("HIGH SCORES")
    print("Player: ", player_score)
    print("Computer: ", computer_score)


if __name__ == '__main__':
    start()
