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
    
def displayIntro():
    print(''' Many people know about Crime Rackets and The Mafia, they've seen them glorified
in movies and on T.V. shows; or maybe even played cops and robbers when they were kids.''')
    time.sleep(7)
    print()
    print('''What they may not know or choose not to believe is that one of the most notorious
and secretive of all these syndicates is The Tooth Fairy Mafia.''')
    time.sleep(8)
    print()
    print('''The T.F.M. is a group of renegade Tooth Fairies who have gone against their sworn oath
to bring kids joy and happiness; and instead have chosen to use their powers to create a lucrative
Tooth Racket selling the teeth on the magical black market.''')
    time.sleep(10)
    print()
    print('''Parents may think it's a harmless myth, but they don't know the truth.
They don't know about...''')
    time.sleep(4)
    print()
    print('''...The Tooth Racket...''')
    time.sleep(4)
    cls()

def displayFinalMission():
    print('''You are playing as Pixie Glitter a member in training of an Elite Tooth Fairy Taskforcce,
code Named: The Awesome Blossoms.''')
    time.sleep(6)
    print()
    print('''You are in your final month of training and head to the mess hall to get some dinner...''')
    time.sleep(5)
    print()
    print('''...just as you begin to eat you get called to the head "Don Juans" Office.
You decide not to finish eating and go straight to his office.''')
    time.sleep(7)
    print()
    print(''' When you arrive you see that he has a mission scroll in his hands. You are told to perform
one final job in order to secure your spot on the E.T.F.T. The Mission: to gather the teeth of children
from the most notorious street for lost teeth...''')
    time.sleep(10)
    print()
    print('''...Candy Cane Lane...''')
    time.sleep(4)
    print()
    print('''Its safe to say that this street has the highest tooth loss to child ratio this side of the Mississippi!
You would think this would be a good thing, but unfortunately after rumors began to spread involving a
string of unsolved tooth robberies, paranoid parents started increasing their security just as a precaution.''')
    time.sleep(12)
    print()
    print('''With your final mission in hand you fly off with your sights
set on Candy Cane Lane, making sure to take your Wand, and Magical Tooth locator''')
    time.sleep(3)
    cls()

def chooseHouse():
    chooseHouse_Options = ["1","2","3"]
    user_choice = ""
    while user_choice not in chooseHouse_Options:
        cls()
        print(''' As you fly in to Candy Cane Lane you begin to search around the neighborhood
using your standard issue Magical Tooth Locator.''')
        time.sleep(1)
        print()
        print('''Your in Luck!''')
        time.sleep(1)
        print()
        print('''The MTL discovers three houses nearby that all just so happen to have children
who lost their front teeth and have them stuffed behind their pillows waiting for a gift
they will receive in the morning...''')
        time.sleep(1)
        print()
        print('''...Or will they, Dun Dun Dunnnnnn!!''')
        time.sleep(1)
        print()
        print('''You quickly fly closer to see which house to go to first; but unfortunately
there is a problem, the MTL also pointed out varying degrees of security at each house.''')
        time.sleep(1)
        print()
        print('''This may be an issue and you will have to tread cautiously at each house.''')
        time.sleep(1)
        print()
        print('''Flying around long enough you notice that the Blue house has the least amount of security.''')
        time.sleep(1)
        print()
        print('''The Green house has a moderate amount of security''')
        time.sleep(1)
        print()
        print('''and the Red house has maximum security.''')
        time.sleep(1)
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

def House01():
    cls()
    print("\n \n --> You Fly over to the Blue House")

def House02():
    cls()
    print("\n \n --> You Fly over to the Green House")

def House03():
    cls()
    print("\n \n --> You Fly over to the Red House")
    

        
##########-Main Program--##########
    
displayIntro()

displayFinalMission()
    
chooseHouse()


