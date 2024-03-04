import sys
import cmd
import os
import time
# from PIL import Image

currentplace="s1"
health=100
inventory=[]

def typewriter_writer(message):
    os.system('cls' if os.name == 'nt' else 'clear')
    for char in message:
        if char!= "\n":
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.06)
        elif char=="\n":
            time.sleep(1)
            print("")
#p= princesses zanda -
def introofgame():
    os.system('cls' if os.name == 'nt' else 'clear')

    x="You woke up with sand in your eyes and mud everywhere else, wearing nothing but a pair of of pants. You have nowhere to go so you start with exploring the place where you stand.You have no energy and you see a bright sun shining above you, your body will need energy soon.You see this person covered in kevlar and with huge automatic guns.You decide to take the risk and come through with your hands up in the air, as soon as you approach towards him a girl who had a sniper and an smg in her hand shot him, she took his food, ammo and everything else which she found useful.Now you don't have a lot of options and you need to survive on your own and get over your fears and fight for your living. So let's begin the battle for survival!!! "
    typewriter_writer(x)
    time.sleep(5)
    print()
    choose=input("Would you like to continue? (Yes or No) >").strip()
    if choose=="yes":
        start_game()
    else:
        title_screen()

def input_screen_selections():
    option= input(">").strip()
    if option.lower()==("play"):
        introofgame()
    elif option.lower()==("help"):
        help_menu()
    elif option.lower()==("quit"):
        sys.exit()
    while option.lower() not in ['play','help','quit']:
        print("Please enter a valid command")
        option=input('>').strip()
        if option.lower()==("play"):
            introofgame()
        elif option.lower()==("help"):
            help_menu()
        elif option.lower()==("quit"):
            sys.exit()
def help_menu():
    print()
    os.system('cls' if os.name == 'nt' else 'clear')
    print("#############################")
    print("######Welcome to  I-Land#####")
    print("#############################")
    print("-Use Up,Down,Left,Right to move")
    print("-Type your commands to implement them.")
    print("Command Syntax:")
    print("go [direction]")
    print("get [item]")
    print("examine(Please examine each and every place for some more insight)")
    print("-Good luck and have fun guys.")
    print()
    time.sleep(10)

    (title_screen())
def title_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("###################################")
    print("############--(I-land)--###########")
    print("###################################")
    print("#              -Play-             #")
    print("#              -Help-             #")
    print("#              -Quit-             #")
    print("###################################")
    (input_screen_selections())

def show_status():
    print()
    print('--------STATUS BAR--------')
    print('You are in the '+ zonemap[currentplace]["ZONENAME"])
    print('Health points-',health)
    directions_available=["right","left","up","down"]
    directions=[]
    for dirs in directions_available:
        if dirs in zonemap[currentplace]:
            directions.append(dirs)
    print("Directions Available= ", directions)
    print("Inventory= ",str(inventory))
    print("""Commands Syntax:
             -->examine
             -->get item name - example= >get adrenaline_shot_and_knife
             -->go direction - example= >go right """)
    # itemsavailable=[]
    # if "item1" in zonemap[currentplace]:
    #     itemsavailable.append(zonemap[currentplace][item1])
    # if "item2" in zonemap[currentplace]:
    #     itemsavailable.append(zonemap[currentplace][item2])
    # print("Items Available are:", str(itemsavailable))

    print("--------------------------")

def position_meter():
    global inventory
    global currentplace
    while True:
        x=1
        while x==1:
            show_status()
            x+=1
        print()
        move=input("Enter command >")
        move=move.lower().split()


        if move[0]=="go":
            if move[1] in zonemap[currentplace]:
                currentplace= zonemap[currentplace][move[1]]
                x=("Welcome to the new place.")
                typewriter_writer(x)
                time.sleep(2)
                break
            else:
                print("You can't go that way!")
                time.sleep(2)

        # elif move[0]=="get" and currentplace=="s1":
        #     if "iteam1" in zonemap[currentplace]:
        #         inventory+= [zonemap[currentplace]["iteam1"]]
        #         print()
        #
        #         print('--------Item Picked Up--------')
        #         print(zonemap[currentplace]["iteam1"]+ " " + 'added to the inventory.')
        #         print('-----------------------------')
        #         print()
        #         time.sleep(2)
        #         # show_status()
        #         del zonemap[currentplace]["iteam1"]
        elif move[0]=="get":
            if "iteam1" in zonemap[currentplace] and (move[1] == zonemap[currentplace]["iteam1"]):
                inventory+= [move[1]]
                print()
                print('--------Item Picked Up--------')
                print(move[1]+ " " + 'added to the inventory.')
                print('------------------------------')
                print()
                time.sleep(2)
                del zonemap[currentplace]["iteam1"]
                if "iteam2" in zonemap[currentplace]:
                    del zonemap[currentplace]["iteam2"]
            elif "iteam2" in zonemap[currentplace] and (move[1] ==zonemap[currentplace]['iteam2']):
                inventory += [move[1]]
                print()
                print('--------Item Picked Up--------')
                print(move[1]+ " " + 'added to the inventory.')
                print('------------------------------')
                print()

                time.sleep(2)
                del zonemap[currentplace]["iteam2"]
                if "iteam1" in zonemap[currentplace]:
                    del zonemap[currentplace]["iteam1"]
            else:
                print("Can't get" + " " + move[1]+ ' !')
                time.sleep(2)
        elif move[0]=="examine":
            examine_0=(zonemap[currentplace]["examine"])

            iteams_list=[]
            if "iteam1" in zonemap[currentplace]:
                iteams_list.append(zonemap[currentplace]['iteam1'])
            if "iteam2" in zonemap[currentplace]:
                iteams_list.append(zonemap[currentplace]['iteam2'])

            typewriter_writer(examine_0)
            print()
            print()
            print('--------Item List--------')
            print("Items available are= ",iteams_list)
            print('-------------------------')
            print()
            time.sleep(2)
        elif move[0]=="exit":
           sys.exit()
        else:
            print("Wrong syntax")
        # if move[0]=="get":


def start_game():
    d="You stare at his dead body lying in the sand with blood all over.You decide to inspect his body if you can find anything left to your use.  Use the examine command to inspect the place and to find anything of use."
    typewriter_writer(d)
    position_meter()
    if currentplace=="s2":
        global health
        d="You're now in a glade like place where you see lots of fruits ,you walk towards them, suddenly you felt a cold hard piece of metal against the back of your head and a shrill voice came from back there “Drop everything you have and put your hands in air”.\nNow you've got two options either you run to save yourself or man up and fight back.  "
        typewriter_writer(d)
        option=input("Would you like to fight back[fight] or run away[run] > ").strip()
        if option.lower()=="run":
            d="Since you decided to run, the man with the gun shot you.\nSo you lost the game....Better Luck Next Time....GAME OVER !"
            typewriter_writer(d)
            time.sleep(12)
            sys.exit()

        elif option.lower()=="fight":
            if("adrenaline_shot_and_knife" in inventory):
                manhealth=100
                while manhealth>0:
                    check=True
                    print()
                    print("""You have two attack types-
                    1)stab(Hard hit)
                    2)slash(Quick hit) """)
                    print()
                    time.sleep(1)
                    print("Enemy's health= ",manhealth)
                    attack=input("How do you want to attack >").strip()
                    attacklist=["stab","slash"]
                    while attack not in attacklist:
                        attack=input(">").strip()

                    if attack=="stab":

                        time.sleep(2)
                        health-=30
                        print("# The man damaged you for 30 hp")
                        print('# Health-',health)
                        print()
                        time.sleep(3)
                        manhealth-=40
                        print("# You stabbed the Enemy for 40 damage with knife")
                        print("# Man Health-",manhealth)
                        print()
                    elif attack=="slash":
                        health-=20
                        print("# The man damaged you for 20 hp")
                        print('# Health-',health)
                        print()
                        time.sleep(2)
                        manhealth-=30
                        print("# You slashed the Enemy for 30 damage with knife")
                        print("# Man Health-",manhealth)
                        print()
                        time.sleep(2)

                    if manhealth<60:
                        if check==True:
                            print("# You were shot in the leg by the man. You are bleeding heavily")
                            print('')
                            check=False
                            time.sleep(2)
                else:

                    at2="""Congratulations! You killed the man\nBut you are heavily injured"""
                    typewriter_writer(at2)
                    time.sleep(2)
                    revival()



            else:
                d1="You dont have the knife, you didnt pick it up at the starting.\nYou lost the game......Better Luck Next Time....GAME OVER !!!"
                typewriter_writer(d1)
                time.sleep(12)

                sys.exit()
def c2():
    d="You're at the FINAL STAGE of the game, THE IRON THRONE where you'll have to fight The Mad Man, head of The Targaryen army, useing the flame throwers. "
    typewriter_writer(d)
    print()
    print("Inventory= ",str(inventory))
    choose=input("Would you like to fight or run away ? You wouldn't want to give up on this level of the game. >").strip()
    if choose !="rpg":
        d="You played really well but you need an rpg to defeat the large Targaryen army equipped with flame throwers."
        typewriter_writer(d)
    else:
        if "rpg" in inventory:
            manhealth=100
            while manhealth>0:
                check=True
                print()
                print("""You have two attack types-
                1)Big - (20kg load but takes time reloading)
                2)Small - (10kg load but is takes less time reloading)""")
                print()
                time.sleep(1)
                print("Mad Man's health= ",manhealth)
                attack=input("How do you want to attack >").strip().lower()
                if attack=="big":
                    manhealth-=40
                    print("# You hit the Mad Man for 40 damage with smg")
                    print("# Mad Man's Health-",manhealth)
                    print('')
                    time.sleep(3)
                    health-=30
                    print("# The Mad Man damaged you for 30 hp")
                    print('# Health-',health)
                    print('')
                    time.sleep(3)
                elif attack=="small":
                    manhealth-=30
                    print("# You hit the Mad Man for 30 damage with smg")
                    print("# Mad Man Health-",manhealth)
                    print('')
                    time.sleep(3)
                    health-=20
                    print("# The Mad Man damaged you for 20 hp")
                    print('# Health-',health)
                    print('')
                    time.sleep(3)
                if manhealth<60:
                    if check==True:
                        print(" You just missed getting burnt by the flame thrower. Be Carefull")
                        print('')
                        check=False
                        time.sleep(3)
            else:
                d="CONGRATULATIONS YOU'VE WON THE GAME BY PLAYING WISELY AND CHOOSING THE RIGHT PATH WHICH LEAD YOU TO YOUR SUCCESS!!!"
                typewriter_writer(d)
                time.sleep(5)
def c1():
    d="You are now standing in front of the caribbean sea. You'll have to face the Great Captain Jack Sparrow and fight with him to cross the sea and reach the FINAL LEVEL of the game. "
    typewriter_writer(d)
    weapons=['smg','ak47','sniper','sword']
    print()
    print("Inventory= ",str(inventory))
    choose=input("Would you like to fight or run away ? >").strip()
    if choose=="fight":
        choice=input("Choose a weapon from your inventory through which you would like to fight >").strip()
        while choice not in inventory:
            choice=input("Choose a weapon from your inventory through which you would like to fight >").strip()
        if choice in inventory:
            if choice=="sniper":
                d="You chose the wrong weapon to fight, snipers cant be used in close combact.\nYou lost the game....Better Luck Next Time....GAME OVER !!!"
                typewriter_writer(d)
                time.sleep(15)
                sys.exit()
            elif choice=="smg":
                d="You've killed Captain Jack Sparrow and his pirates.\n By all the right choices you've made it to the FINAL LEVEL of the game. "
                typewriter_writer(d)
                position_meter()
                c2()
            elif choice=="ak47":
                d="You've killed Captain Jack Sparrow and his pirates.\n By all the right choices you've made it to the FINAL LEVEL of the game. "
                typewriter_writer(d)
                position_meter()
                c2()

            elif choice=="knife":
                d="You chose the wrong weapon to fight, a knife is not enough to kill captain jack sparrow and his fleet .\nYou lost the game....Better Luck Next Time....GAME OVER !!!"
                typewriter_writer(d)
                time.sleep(15)
                sys.exit()
            elif choice=="sword":
                d="You've killed Captain Jack Sparrow and his pirates.\n By all the right choices you've made it to the FINAL LEVEL of the game. "
                typewriter_writer(d)
                position_meter()
                c2()

            elif choice=="armour":
                d="You chose the wrong weapon to fight, an armour is not a weapon LMAO .\nYou lost the game....Better Luck Next Time....GAME OVER !!!"
                typewriter_writer(d)
                time.sleep(15)
                sys.exit()
    else:
        d="you chose to run away and you were never able to face  "
        typewriter_writer(d)
        time.sleep(15)
        sys.exit()




def revival():
    global health
    d="You're at very low health. Do you want to take an adrenaline shot to recover??? "
    typewriter_writer(d)
    choose=input("(yes or no) >").strip()
    if choose.lower()=="no":
        dd_die="""Your health is depleting due to the blood loss"""
        typewriter_writer1(dd_die)
        print()
        while health>0:
            health-=5
            print("Current Health-",health)
            time.sleep(0.6)
        ending_text1=("You were too lazy to heal yourself.\nSo you lost the game......Better Luck Next Time....GAME OVER !")
        typewriter_writer(d1)
        time.sleep(15)
        sys.exit()
    elif choose=="yes":
        dd="Reviving..."
        typewriter_writer(dd)
        time.sleep(1)
        print("Health recovered")
        health=100
        print("Current Health =",health)
        inventory.pop(0)
        inventory.append("knife")
        position_meter()
        if currentplace=="a1":
            d="Since you choose to go up you've reached the Corona Castles. In order to cross that you have to get through PRINCESS ZENDA, she isn't welcoming any guests into her kingdom.She's a good close range fighter."
            typewriter_writer(d)

            choose=input("Would you like to fight or run away ? >").strip()
            if choose=="fight":
                print("Inventory=",inventory)
                x="You chose to fight with Princess Zenda, she has invited you to the battlefield. LOOK OUT FOR YOURSELF!!!"
                if "smg" in inventory:
                    manhealth=100
                    while manhealth>0:
                        check=True
                        print()
                        print("""You have two attack types-
                        1)Auto(Quick hit)
                        2)Burst(Precise Hit)""")
                        print()
                        time.sleep(1)
                        print("Princess's health= ",manhealth)
                        attack=input("How do you want to attack >").strip().lower()
                        if attack=="auto":
                            manhealth-=40
                            print("# You hit the Princess for 40 damage with smg")
                            print("# Princess Health-",manhealth)
                            print('')
                            time.sleep(3)
                            health-=30
                            print("# The Princess damaged you for 30 hp")
                            print('# Health-',health)
                            print('')
                            time.sleep(3)
                        elif attack=="burst":
                            manhealth-=30
                            print("# You hit the Princess for 30 damage with smg")
                            print("# Princess Health-",manhealth)
                            print('')
                            time.sleep(3)
                            health-=20
                            print("# The Princess damaged you for 20 hp")
                            print('# Health-',health)
                            print('')
                            time.sleep(3)
                        if manhealth<60:
                            if check==True:
                                print("# You just missed a headshot from princess. Be Carefull")
                                print('')
                                check=False
                                time.sleep(3)
                    else:

                        at2="""Congratulations! You killed the princess\nYou can now move forward to the next enemies."""
                        typewriter_writer(at2)
                        time.sleep(3)
                        position_meter()
                        c1()
                elif "sniper" in inventory:
                    d="Since the princess invited you to the battlefield your sniper gun is of no use now. You've no choice but to surrender yourself.\nYou lost the game......Better Luck Next Time....GAME OVER !!!"
                    typewriter_writer(d)
                    time.sleep(15)
                    sys.exit()
                else:
                    d1="You dont have any weapon other than knife, you didnt pick it after killing the enemy.\nYou lost the game......Better Luck Next Time....GAME OVER !!!"
                    typewriter_writer(d1)
                    time.sleep(15)
                    sys.exit()


            elif choose=='run':
                d="#Since you decided to run, the man with the gun shot you.\nSo you lost the game....Better Luck Next Time....GAME OVER !"
                typewriter_writer(d)
                time.sleep(15)
                sys.exit()


        elif currentplace=="b1":
            d="Since you choose to go down you've reached the Dothraki. In order to cross this region you have to get through KHAL, he isn't welcoming people in his region of rule. He has a really good arsenal and army, you can't fight him in the battlefield. LOOK OUT FOR YOURSELF!!!"
            typewriter_writer(d)
            choose=input("Would you like to fight or run away ? >").strip()
            if choose=="fight":
                print("Inventory=",inventory)
                x="You chose to fight with Khaal Drogo, who is on his horse in the battlefield!!!"
                typewriter_writer(x)
                if "smg" in inventory:
                    d="You decided to enter kill khal drogo in a closed ranged fight but you were killed. If you had choosen the sniper, you could have killed him while hiding in the trees.....Better Luck Next Time....GAME OVER ! "
                    typewriter_writer(d)
                    time.sleep(15)
                    sys.exit()

                elif "sniper" in inventory:
                    choose=int(input("At what angle would you like to take the shot. The khal is located at an angle of 28 degrees to 34 degrees >"))
                    if(34>=choose>=28):
                        d="Well done you killed khal Drogo while hiding in the forest"
                        typewriter_writer(d)
                        time.sleep(5)
                        position_meter()
                        c1()
                    else:
                        d="You missed the shot and khal drogo spotted and killed you in a closed ranged fight. If you had choosen the correct angle, you could have killed him while hiding in the trees.....Better Luck Next Time....GAME OVER ! "
                        typewriter_writer(d)
                        time.sleep(5)

                else:
                    d1="You dont have any weapon other than knife, you didnt pick it after killing your last enemy.\nYou lost the game......Better Luck Next Time....GAME OVER !!!"
                    typewriter_writer(d1)
                    time.sleep(15)
                    sys.exit()


            elif choose=='run':
                d="#Since you decided to run, khal drogo spotted and killed you.\nSo you lost the game....Better Luck Next Time....GAME OVER !"
                typewriter_writer(d)
                time.sleep(15)
                sys.exit()
"""


                  a1
            /           \
s1-------s2                   c1---c2
            \           /
                  b1
                """
zonemap={
    "s1":{
        "ZONENAME": "Woodland of the island. Examine this place to find and know more.",
        "examine": "You are in the deserted forest part of the island with a dead body lying around you. He has an ADRENALINE SHOT and a KNIFE.",
        "iteam1": 'adrenaline_shot_and_knife',
        "right": "s2"
        },
    "s2":{"ZONENAME": "Forest glade in the island. Examine this place to find and know more.",
        "examine": "You find a letter that says, \"You're in a game where you have to fight every clan you come across to win the game.Every choice you make will either help you survive or kill you.\"\n He had a SNIPER and a SMG. Pick your weapon wisely as these choices will decide your fate.",
        "iteam1": 'sniper',
        "iteam2": 'smg',
        "up": "a1",
        "down":"b1"},
    "a1":{
        "ZONENAME": "Corona castles. Examine this place to find and know more.",
        "examine": "You are in the Corona castles in the island, You can have successfully killed the princess. She has an AK47",
        "iteam1": 'ak47',
        "down": "c1",},
    "b1":{
        "ZONENAME": "The Dothraki Ground. Examine this place to find and know more.",
        "examine": "You have successfully killed khal.He has a sword. They are of great use.",
        "iteam1": 'sword',
        "up": "c1",},
    "c1":{
        "ZONENAME": "The Bravoos sea. Examine this place to find and know more.",
        "examine": "You have successfully killed captain jack sparrow. He has a rpg which will help you a lot.",
        "iteam1": "rpg",
        "right": "c2"},
    "c2":{
        "ZONENAME": "The Iron Throne. Examine this place to find and know more.",
        "examine": "You are in the Iron Throne of the island to fight with The Mad Man and capture the Throne to WIN THE GAME. He has dragons who protect him."
    }
}
title_screen()
