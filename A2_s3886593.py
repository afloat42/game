#COSC1519 Introduction to Programming
#A2 Programming Project 
#Student name:Sohil Pachbhaiya
#Student number:S3886593


# module import random
import random

# Global Variables
# default/initial value for username
username = 'default'
class_type = "default"
boss_hp = 50.50


# function definition to start game
def start_game():
    # print statement to show text
    print("You are at work")
    print("you receive a strange call", "You answer the call", sep="....")
    # ask user to write input of what to answer phone call
    phone_reply = input("write your reply")


# function definition to scene1
# print a statement to display text
#asks user for input
#print a statement to display text
def scene1():
    print("you hear nothing back", "you reply again", sep="....")
    second_reply = input("write your reply")
    print("Suddenly you see the time on the phone stop", "it looks and feels like everything have been frozen",
          sep="\n")

# function definition to start game
# print a statement to display text
#asks user for input
#print a statement to display text
def scene2():
    global username
    print("After a while, a random pop up comes out", "\n")
    username = input("Asking for a username")
    print("Your username,", username, "is approved")
    print("Your greeted by goblin")


# function definition to start game
# prints a statement to display text
# runs a while loop to display the class you can select
def scene3():
    global class_type
    print("The goblin starts talking......")
    class_selected = True
    while class_selected:
        print("What class do you select")
        print("0-rogue")
        print("1-mage")
        print("? -warrior")
        #runs a try and except tp see of the input is a int
        #runs a if, elif and else statement and based on it prints a statemnet
        try:
            class_input = int(input(""))
            if class_input == 0:
                class_type = "rogue"
                print("you have selected class rogue")
                class_selected = False
            elif class_input == 1:
                class_type = "mage"
                print("you have selected class mage")
                class_selected = False
            else:
                class_type = "warrior"
                print("you have selected class warrior")
                class_selected = False

            print("Your journey starts of", username, "the", class_type)

        except:
            print("unknown class please select from the one listed")


# function definition to start game
# runs a bunch of print statemnet
def scene4():
    print("A quest pin starts of", "you accept it", sep=".......")
    print("Hey", username, "!!!", "it is Drakath", "I have a mission for you", "we need your help", sep="\n")
    print("1.0-Sure, I need the gold and experience")
    print("2.0-<say nothing>")
    print("3.0-No, I reject [game end]")
    #first while loop is to check reply_quest input is 1 or 3 so that it can print its statement
    reply = True
    while reply:
        #second while loop is for when the input is 2 , it repeats the loop again asking the same questions
        try:
            reply_quest = float(input("Come on it is going to be easy are you in?"))
            while reply_quest == 2.0:
                print("1.0-Sure, I need the gold and experience")
                print("2.0-<say nothing>")
                print("3.0-No, I reject [game end]")
                reply_quest = float(input("Come on it is going to be easy are you in?"))
            reply = False
        except:
            print("Please enter from 1-3")
    if reply_quest == 1.0:
        print("Meet Drakath at Drakath fortress @ 1000", "The time fast forwards to 1000",
              "you get ready to make your way to the fortress", sep="\n")
    elif reply_quest == 3.0:
        print("You decided to reject the offer", "GAME END", "\n")
        print("--------------------------------------------------------")
        print("Thank you for playing", username, "!!!")
        print("--------------------------------------------------------")
        quit()


def scene5():
    #prints a statement to display
    #contains a list and display it by printing the statement
    print("Before entering the fortress", "select a weapon", sep="\n")
    weapon_list = ["1-dagger", "2-Staff", "3-Tome of force", "4-board sword"]
    print(weapon_list)
    #while the user have not selected any weapon it runs the while loop asking the user for an input to select the weapon
    #includeds a try and except for when the user does not use int so that it repeats the code again asking the user to write an int
    weapon_select = "default"
    while weapon_select != 1 and weapon_select != 2 and weapon_select != 3 and weapon_select != 4:
        try:
            weapon_select = int(input("What weapon do you wish to use"))
            if weapon_select == 1:
                weapon = "dagger"
                print("you have selected the weapon,", weapon)
            elif weapon_select == 2:
                weapon = "staff"
                print("you have selected the weapon,", weapon)
            elif weapon_select == 3:
                weapon = "Tome of force"
                print("you have selected the weapon,", weapon)
            elif weapon_select == 4:
                weapon = "board sword"
                print("you have selected the weapon,", weapon)
            else:
                print("please choose between 1-4")
        except:
            print("Please enter number from 1-4")


# function definition to start game
def scene6():
    print("you spot many  doors", "only 1 door opens to the boss", sep="\n")
    replay = True
    #runs a while to get a random number between 0 to 5
    while replay:
        correct_number = random.randint(0, 5)
        game_over = False
        attempt = 0
        # runs a while loop to check if the user input is equal to the correct_number.
        #try and except is used to check incase the user does not input an int
        # conditions of if and else if run to check if the user_guess is correct 
        while not game_over:
            try:
                user_guess = int(input("guess the door number"))
                if user_guess == correct_number:
                    print("You found the door however it is locked")
                    game_over = True
                    replay = False
                    door_code()
                else:
                    print("No, boss in this door!")
                    attempt = attempt + 1
                if attempt == 3:
                    print("max attempt")
                    game_over = True
                    replay = True
            except:
                print("numbers only")

def door_code():
    #assigns the variable x and y a random float value
    x = round(random.uniform(10.1,100.8),1)
    y = round(random.uniform(10.1,100.8),1)
    door_password = 0
    #this while loop will loop to check if the door_password answer is correct. 
    while door_password != x+y:
        try:
            print("what is", x, "+", y)
            door_password = float(input())
            if door_password != x+y:
                print("Wrong answer!! try again")
        except:
            print("Wrong input, Please answer the question")
    else:
        print("Congrats you managed to unlock the door")

# function definition to start game
def scene7():
    global boss_hp
    print("You enter the door", "prepare to attack it", "the boss have 50.5 HP", sep="\n")
    turn = 0
    # gives the user 4 turns to kill the boss if failed by 4 turns, a defeat scene will display
    while boss_hp > 0:
        if turn > 4:
            print("Failed to kill boss")
            boss_hp = 0
            scene8(False)
        else:
            # check class type as each class have differnt attack list
            if class_type == "rogue":
                rogue_attack_list = ["0- basic attack (5.5)", "1-ambush (10.5)", "2- shiv (15.5)", "3-fient(20.5)"]
                # show damage listhi
                ratk_damage = [5.5, 10.5, 15.5, 20.5]
                # print the list to display
                print(rogue_attack_list)
                # ask the user for a input to select the spell
                # if statment to see what skill user asked for
                # calculates the damage done to boss
                # if boss is deafeated goes to next scene
                try:
                    rogue_attack = int(input("what attack do you want to use?"))
                    if rogue_attack == 0:
                        print("you used,", rogue_attack_list[rogue_attack], "You have damage",
                              ratk_damage[rogue_attack], "damage", )
                        turn = turn + 1
                        result = calc(ratk_damage[rogue_attack])
                        if result == True:
                            scene8(True)
                    elif rogue_attack == 1:
                        print("you used,", rogue_attack_list[rogue_attack], "You have damage",
                              ratk_damage[rogue_attack], "damage", )
                        turn = turn + 1
                        result = calc(ratk_damage[rogue_attack])
                        if result == True:
                            scene8(True)
                    elif rogue_attack == 2:
                        print("you used,", rogue_attack_list[rogue_attack], "You have damage",
                              ratk_damage[rogue_attack], "damage", )
                        turn = turn + 1
                        result = calc(ratk_damage[rogue_attack])
                        if result == True:
                            scene8(True)
                    elif rogue_attack == 3:
                        print("you used,", rogue_attack_list[rogue_attack], "You have damage",
                              ratk_damage[rogue_attack], "damage", )
                        turn = turn + 1
                        result = calc(ratk_damage[rogue_attack])
                        if result == True:
                            scene8(True)
                except:
                    print("numbers from 0-3 only")
            # check class type as each class have differnt attack list
            if class_type == "mage":
                mage_attack_list = ["0- basic attack (3.2)", "1-fire (9.2)", "2-forst (14.2)", "3-thunder (19.2)"]
                matk_damage = [3.2, 9.2, 14.2, 19.2]
                print(mage_attack_list)
                # ask the user for a input to select the spell
                # if statment to see what skill user asked for
                # calculates the damage done to boss
                # if boss is deafeated goes to next scene
                try:
                    mage_attack = int(input("what attack do you want to use?"))
                    if mage_attack == 0:
                        print("you used,", mage_attack_list[mage_attack], "You have damaged", matk_damage[mage_attack],
                              "damage", )
                        turn = turn + 1
                        result = calc(matk_damage[mage_attack])
                        if result == True:
                            scene8(True)
                    elif mage_attack == 1:
                        print("you used,", mage_attack_list[mage_attack], "You have damage", matk_damage[mage_attack],
                              "damage", )
                        turn = turn + 1
                        result = calc(matk_damage[mage_attack])
                        if result:
                            scene8(True)
                    elif mage_attack == 2:
                        print("you used,", mage_attack_list[mage_attack], "You have damage", matk_damage[mage_attack],
                              "damage", )
                        turn = turn + 1
                        result = calc(matk_damage[mage_attack])
                        if result == True:
                            scene8(True)
                    elif mage_attack == 3:
                        print("you used,", mage_attack_list[mage_attack], "You have damage", matk_damage[mage_attack],
                              "damage", )
                        turn = turn + 1
                        result = calc(matk_damage[mage_attack])
                        if result == True:
                            scene8(True)
                except:
                    print("numbers from 0-3 only")
            # check class type as each class have differnt attack list
            if class_type == "warrior":
                warrior_attack_list = ["0- basic attack (5)", "1-Charge (10)", "2-berserker rage (15)",
                                       "3-heroic leap (20)"]
                watk_damage = [5, 10, 15, 20]
                print(warrior_attack_list)
                try:
                    warrior_attack = int(input("what attack do you want to use?"))
                    # ask the user for a input to select the spell
                    # if statment to see what skill user asked for
                    # calculates the damage done to boss
                    # if boss is deafeated goes to next scene
                    if warrior_attack == 0:
                        print("you used,", warrior_attack_list[warrior_attack], "You have damage",
                              watk_damage[warrior_attack], "damage", )
                        turn = turn + 1
                        result = calc(watk_damage[warrior_attack])
                        if result == True:
                            scene8(True)
                    elif warrior_attack == 1:
                        print("you used,", warrior_attack_list[warrior_attack], "You have damage",
                              watk_damage[warrior_attack], "damage", )
                        turn = turn + 1
                        result = calc(watk_damage[warrior_attack])
                        if result == True:
                            scene8(True)
                    elif warrior_attack == 2:
                        print("you used,", warrior_attack_list[warrior_attack], "You have damage",
                              watk_damage[warrior_attack], "damage", )
                        turn = turn + 1
                        result = calc(watk_damage[warrior_attack])
                        if result == True:
                            scene8(True)
                    elif warrior_attack == 3:
                        print("you used,", warrior_attack_list[warrior_attack], "You have damage",
                              watk_damage[warrior_attack], "damage", )
                        turn = turn + 1
                        result = calc(watk_damage[warrior_attack])
                        if result == True:
                            scene8(True)
                except:
                    print("numbers from 0-3 only")


def calc(dmg):
    global boss_hp
    #checks if the boss_hp is above 0 and if it is, it will damage the boss hp
    #if the boss_hp drops below 0, it prints ( boss defeated)
    if boss_hp > 0:
        boss_hp = boss_hp - dmg
        if boss_hp < 0:
            print("Boss defeated")
            return True
        else:
            print("the boss HP drops to", boss_hp)
        return False
    elif boss_hp < 0:
        print("Boss defeated")
        return True


def scene8(x):
    # checks if boss is defeated, it prints a certain statement, if not it prints the other statement 
    if x is True:
        print("Congrats!!!!!! You have defeated the boss", "Here is your reward", "1000G")
        print("--------------------------------------------------------")
        print("Thank you for playing!!!", username)
        print("--------------------------------------------------------")
    else:
        print("Defeat!!!")
        print("--------------------------------------------------------")
        print("Thank you for playing!!!", username)
        print("--------------------------------------------------------")


# main code
start_game()
scene1()
scene2()
scene3()
scene4()
scene5()
scene6()
scene7()
