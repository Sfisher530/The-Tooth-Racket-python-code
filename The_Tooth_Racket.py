#--Developer: Scott Fisher
#--Date: 09/25/2019
#--Subject: Group project 1 CISGAME-403: Text Based Choose Your Own Adventure Game
#--Program Name: The Tooth Racket

##########--Global imports--##########
import random
import time

##########-Functions--##########
def cls():
    print("\n" * 100)
    
def displayIntro():##########Background Info/Introduction def block Title slide used to begin and when asked to restart
    print(''' Many people know about Crime Rackets and The Mafia, they've seen them glorified in movies and on T.V. shows; or maybe even played cops and robbers when they were kids.''')
    time.sleep(8)
    print()
    print('''What they may not know or choose not to believe is that one of the most notorious and secretive of all these syndicates is The Tooth Fairy Mafia.''')
    time.sleep(7)
    print()
    print('''The T.F.M. is a group of renegade Tooth Fairies who have gone against their sworn oath to bring kids joy and happiness; and instead have chosen to use their powers to create a lucrative
Tooth Racket selling the teeth on the magical black market.''')
    time.sleep(11)
    print()
    print('''Parents may think it's a harmless myth, but they don't know the truth, they don't know about...''')
    time.sleep(5)
    print()
    print('''...The Tooth Racket...''')
    time.sleep(3)
    cls()

def displayFinalTask():###########Extra flavor text setting up the character background and chooseHouse() def block
    print('''You are playing as Pixie Glitter a member in training of an Elite Tooth Fairy Taskforce code Named: The Awesome Blossoms.''')
    time.sleep(6)
    print()
    print('''You are in your final days of training and head to the mess hall to get some dinner...''')
    time.sleep(5)
    print()
    print('''...just as you begin to eat you get called to the head Don Juan's Office. Not wanting to take your chances and miss out on a Task, you decide not to eat and go straight to his office as quickly as possibly.''')
    time.sleep(9)
    print()
    print(''' When you arrive you are told to perform one final task in order to secure your spot on the E.T.F.T.''')
    time.sleep(5)
    print()
    print('''The Task: To gather the teeth of children from the street that's most notorious for having more lost teeth in a row than any other...''')
    time.sleep(8)
    print()
    print('''...Candy Cane Lane...''')
    time.sleep(4)
    print()
    print('''Its widely known that this street has the highest tooth loss to child ratio this side of the Mississippi; which you would think this would be a good thing...''')
    time.sleep(7)
    print()
    print('''...Unfortunately after rumors began to spread on the local news involving a string of unsolved tooth robberies, paranoid parents started increasing their security just as a precaution.''')
    time.sleep(10)
    print()
    print('''With your final task given you fly off with your sights set on Candy Cane Lane, making sure to take your Wand, and Magical Tooth locator with you.''')
    time.sleep(8)
    cls()

def chooseHouse():##########First user input choice and def block to be called whenever there is a fail and the player needs to restart from the begining.
    chooseHouse_Options = ["1","2","3"]
    user_choice = ""
    while user_choice not in chooseHouse_Options:
        cls()
        print(''' As you fly in to Candy Cane Lane you begin to search around the neighborhood using your standard issue Magical Tooth Locator...''')
        time.sleep(6)
        print()
        print('''...Your in Luck!!!''')
        time.sleep(3)
        print()
        print('''The M.T.L. discovers three houses nearby that all just so happen to have children who lost their front teeth and all have them hidden awaiting their gift they will receive in the morning...''')
        time.sleep(7)
        print()
        print('''...Or will they...''')
        time.sleep(3)
        print()
        print('''Dun Dun Dunnnnnn!!''')
        time.sleep(3)
        print()
        print('''You quickly fly closer to see which house to go to first; but unfortunately there is a problem. The MTL was able to find and point out varying degrees of security at each house.''')
        time.sleep(7)
        print()
        print('''This will be an issue and you will have to tread cautiously at each house.''')
        time.sleep(5)
        print()
        print('''Flying around using your M.T.L. you can see that the Blue house has the least amount of security.''')
        time.sleep(6)
        print()
        print('''The Green house has a moderate amount of security''')
        time.sleep(4)
        print()
        print('''and the Red house has maximum security.''')
        time.sleep(4)
        print()
        print('''Which House will you Choose? 
                1) Fly to the Blue House
                2) Fly to the Green House
                3) Fly to the Red house''')

        user_choice = str(input("Enter option number:"))
        #print("You have selected " + user_choice)
        if user_choice == chooseHouse_Options[0]:
            House01()
        elif user_choice == chooseHouse_Options[1]:
            House02()
        elif user_choice == chooseHouse_Options[2]:
            House03()

def House01():##########Def Block for the Blue House
    cls()
    print("\n \n --> You Fly over to the Blue House")


    

def House02():###############Def Block for the Green House
    choose_house_options = ["1","2","3"]
    user_choice = ""
    while user_choice not in choose_house_options:
        cls()
        print('''\n \n --> You fly over to the green house and deploy your M.T.L. and as soon as you do the device detects motion near the backyard and you presume there is a dog roaming around nearby.''')
        time.sleep(6)
        print()
        print('''A quick fly over and you discover that there is a Doggy Door in the backyard which would explain the motion you detected; as well as a window on the side of the house which leads directly to the kids bedroom; but it could be full of traps.''')
        time.sleep(10)
        print()
        print('''One last look around the perimeter and you find that the front door has an alarm which may be connected directly to the police.''')
        time.sleep(5)
        print()
        print('''Which option will you choose?
             1) Through the Doggy Door?
             2) Through the window?
             3) Through the Front Door?''')

        user_choice = str(input('Enter option number:'))############this is asking for the users input and converting it into a string to be used in the if/elif operators
        if user_choice == choose_house_options[0]:
            doggyDoor()
        elif user_choice == chooseHouse_Options[1]:
            Window()
        elif user_choice == chooseHouse_Options[2]:
            frontDoor()

def doggyDoor():#############Def block for the doggy door deciscion from the Green House
    green_house_options = ["1","2"]
    user_choice = ""
    while user_choice not in green_house_options:
        cls()
        print('''\n\n --> You fly to the Doggy Door and hide in nearby shurbbery carefully checking to see if the path is clear. Since you need to conserve your magic use you are unable to use your MTL.''')
        time.sleep(7)
        print()
        print('''What will you do?
             1) Press your luck with the door?
             2) Return and try another option?''')

        user_choice = str(input('Enter option number:'))########this is asking for the users input and converting it into a string to be used in the if/elif operators
        if user_choice == green_house_options[0]:
            pressLuck()
        elif user_choice == green_house_options[1]:
            house02()

def pressLuck():#########Def block for the press luck options from the doggyDoor deciscion tree
    press_luck_options = ["1","2"]
    user_choice = ""
    while user_choice not in press_luck_options:
        cls()
        print('''Once you decided that there are no dogs around, you dart out from your hiding spot and straight for the doggy door.''')
        time.sleep(6)
        print()
        print('''YOU MAKE IT!!!''')
        time.sleep(2)
        print()
        print('''Now comes the hard part of avoiding detection inside the house. Thankfully you have your magic wand which makes yourself invisible except to dogs and those with child like imaginations.''')
        time.sleep(6)
        print()
        print('''Flying down a hallway you carelessly dart around a corner and fly right into the family dogs!!!.''')
        time.sleep(6)
        print()
        print('''You need to make a deciscion quickly!
             1) Play Dead?
             2) Try to retreat back outside?''')

        user_choice = str(input('Enter option number:'))########this is asking for the users input and converting it into a string to be used in the if/elif operators
        if user_choice == press_luck_options[0]:
            playDead()
        elif user_choice == chooseHouse_Options[1]:
            chewToy()

def playDead():##########Def block for Luck Win 1/Play Dead Success option from the press luck deciscion tree
    cls()
    print(''' Your quick thinking and skills of resembling a corpse pay off!''')
    time.sleep(4)
    print()
    print('''You push on to the kids bedroom and use the last charge from your magic wand to successfully extract the tooth from its hiding spot.''')
    time.sleep(8)
    print()
    print('''Next time try to set a reminder to leave the wand on the charger before you leave for a Task. ''')



def missionComplete():#########def Block for the Mission Complete Flavor Text before the Credits
    print('''You fly back confidently knowing that when you return to the T.F.M.H.Q. with your Task complete that you will join the ranks of the Elite Tooth Fairy Taskforce; and all your hard work and training will be complete.''')
    time.sleep(8)
    print()
    print('''Impressed with the results the Head Don Juan makes you an offer you cannot refuse, a Task to save your partner Dixie Glitter who was captured while you were off gathering teeth at Candy Cane Lane.''')
    time.sleep(8)
    print()
    print('''Dixie was captured by scientists who are trying to analyze her magical powers and find out if there are others like her and If completed you will be responsible for stopping the eventual takedown of the entire Racket,
 and would possibly be offered a position as the right hand fairy of the Don. One step closer to your ultimate goal of Head Don Juan of the Tooth Fairy Mafia!''')


def endCredits():
    end_credits_options = ["Y","N"]
    user_choice = ''
    while user_choice not in end_credits_options:
        print('''\n\n\n\n                                                       Thanks for Playing!

                                                                 Hope you had fun and enjoyed our first game collaboration:
                                                              
                                                                          The Tooth Racket, by Phantom Gamers.

                                                          "Remember To Never Give Up, and Never Stop Gaming!" - Raynday Gamer
                                                              

                                                            Lead Design/Storyboard editor/Programer.....................Scott F.

                                                            Lead Programer/storyboard/level design......................Luis P.

                                                            Lead Programer/Storyboard/level design......................Ryan R.

                                                            Lead Storybord/Level Design/programming.....................Robert W.


                                                            Crowd Funding on GoFundMe/Patreon begins Nov. 6th 2019 for the

                                                        The Tooth Racket 2 : Return 2 candy Cane Lane(This time its personal)''')
    
        print(''' would you like to play again? (Y or N)''')
        user_choice = str(input('Enter option Y or N:'))
        if user_choice == end_credits_options[0]:
            displayIntro()
            displayFinalTask()
            chooseHouse()
            missionComplete()
            endCredits()
            
        elif user_choice == end_credits_options[1]:
            break
        

        
 

    

def Window():##########Def block for the Window deciscion from the Green House
    print('''\n\n --> You fly towards the window and notice that it is already cracked open, and effortlessly use your magic to shrink yourself and fly through the mesh screening to get into the house.''')
    time.sleep(7)
    print()
    print('''Easy enough, however your next task is to find your way to the kids bedroom and successfully get the tooth without waking him/her.''')







































def House03():#Def Block for the Red House 
    cls()
    print("\n \n --> You Fly over to the Red House")
    

        
##########-Main Program--##########
    
displayIntro()

displayFinalTask()
    
chooseHouse()

missionComplete()

endCredits()

