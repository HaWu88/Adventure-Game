# Wu, Hamilton

import time
import random
import numpy as np


def print_pause(text):
    print(text)
    time.sleep(2)


def intro(equip, monsters, items):
    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {monsters} is somewhere around here"
                ", and has been terrifying the nearby village")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                "(but not very effective) dagger.")
    equip.append("tiny dagger")
    field(equip, monsters, items)


def field(equip, monsters, items):
    # Item would be where the highest probabilty
    random.seed(5)
    # Probability of item to be found in cave or forest
    probability = random.random()
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("Enter 3 to enter the forest.")
    num = input("What would you like to do?\n"
                " (Please enter 1 or 2 or 3.): ")
    if num == "1":
        house(equip, monsters, items)
    elif num == "2":
        cave(equip, monsters, items, probability)
    elif num == "3":
        forest(equip, monsters, items, probability)
    else:
        field(equip, monsters, items)


def gg(equip, monsters, items):  # good game, end of the game
    restart = input("Would you like to play again? (y/n): ")
    if restart == "y":
        print_pause("Excellent! Restarting the game ...")
        start_game()
    elif restart == "n":
        print("Thanks for playing! See you next time.")
    else:
        gg(equip, monsters, items)


def choice(equip, monsters, items):
    pick = input("Would you like to (1) fight or (2) run away?: ")
    if pick == "1":
        if "fork" in equip or "lamborghini" in equip:
            print_pause(f"Wait! The {monsters} look carefully at your"
                        "shiny new toy and thought ...")
            print_pause(f"Why am I afraid of that {items} ...")
            print_pause(f"Unfortunately, with your {items}, "
                        "you have been obliterated!")
            gg(equip, monsters, items)
        elif "tiny dagger" in equip:
            print_pause("You do your best...")
            print_pause(f"but your dagger is no match for the {monsters}.")
            print_pause("You have been defeated!")
            gg(equip, monsters, items)
        elif "medallion" in equip and items in equip:
            print_pause(f"As the {monsters} moves to attack, "
                        f"you unsheath your new {items}.")
            print_pause(f"The {items.capitalize()} of Aincrad shines "
                        "brightly in your hand as you brace yourself "
                        "for the attack.")
            print_pause(f"But the {monsters} takes one look at your shiny "
                        "new toy and the Medallion blinds "
                        "it and it runs away!")
            print_pause(f"You have rid the town of the {monsters}. "
                        "You are Victorious!")
            gg(equip, monsters, items)
        else:
            print_pause("The medallion was missing and couldn't "
                        f"blind the {monsters}.")
            print_pause("You have been destroyed!")
            gg(equip, monsters, items)
    elif pick == "2":
        print_pause("You run back into the field. Luckily, "
                    "you dont seem to have been followed.")
        field(equip, monsters, items)
    else:
        choice(equip, monsters, items)


def house(equip, monsters, items):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens "
                f"and out steps a {monsters.capitalize()}.")
    print_pause(f"Eep! This is the {monsters}'s house!")
    print_pause(f"The {monsters} attacks you!")
    if "tiny dagger" in equip:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
    choice(equip, monsters, items)


def change_equip(equip, monsters, items):
    print_pause(f"You have found the magical {items.capitalize()}"
                " of Aincrad!")
    print_pause("You discard your silly old tiny dagger and "
                f"took the {items} with you.")
    equip.remove("tiny dagger")
    equip.append(items)
    back_to_field(equip, monsters, items)


def back_to_field(equip, monsters, items):
    print_pause("You walk back out to the field.")
    field(equip, monsters, items)


def medallion(equip, monsters, items):
    print_pause("You have found the Medallion of Aincrad!")
    equip.append("medallion")
    back_to_field(equip, monsters, items)


def cave(equip, monsters, items, probability):
    print_pause("You peer cautiously into the cave.")
    if probability > 0.5:
        if "tiny dagger" in equip:
            print_pause("It turns out to be only a very small cave.")
            print_pause("Your eye catches a glint of metal behind a rock.")
            change_equip(equip, monsters, items)
        else:
            print_pause("You've been here before, and gotten all the good "
                        "stuff. It's just an empty cave now.")
            back_to_field(equip, monsters, items)
    else:
        if "medallion" in equip:
            print_pause("You've been here before, and gotten all the good "
                        "stuff. It's just an empty cave now.")
            back_to_field(equip, monsters, items)
        else:
            medallion(equip, monsters, items)


def forest(equip, monsters, items, probability):
    print_pause("You walked around the forest carefully.")
    if probability <= 0.5:
        if "tiny dagger" in equip:
            print_pause("You found a huge tree in front of you.")
            print_pause("Your eye catches a glint of metal inside the hole "
                        "in the tree.")
            change_equip(equip, monsters, items)
        else:
            print_pause("You've been here before, and gotten all the good "
                        "stuff. It's just an empty tree now.")
            back_to_field(equip, monsters, items)
    else:
        if "medallion" in equip:
            print_pause("You've been here before, and gotten all the good "
                        "stuff. It's just an empty tree now.")
            back_to_field(equip, monsters, items)
        else:
            medallion(equip, monsters, items)


def start_game():
    equip = []
    monsters = np.random.choice(["dragon", "wicked fairie", "pirate",
                                 "gorgan", "witch"])
    items = np.random.choice(["sword", "bow", "spear", "dagger",
                              "fork", "lamborghini"])
    intro(equip, monsters, items)


if __name__ == "__main__":
    start_game()
