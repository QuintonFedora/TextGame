import random
import time
print('Introduction'.center(51,'-'))
print('An adventure game that changes with the choices you make and has multiple outcomes!')
print("Welcome to What's Next".center(52,'-'))
time.sleep(2)
ASCII_ART = r'''
                      .::--::.      
                   .-==========-.   
                  -=======+======-  
                 -====++==+=++====- 
                .=======+**+=======.
                .=======+**+=======.
                 -====++==+=++====- 
                  -=======+======-  
                   .-==========-.   
                      .::--::.      
'''

print(ASCII_ART)
time.sleep(1)
print('The Beginning...')
print("You slowly wake up to a warm orange glow that covers everything.")
print('Introduction'.center(30,'-'))
print("You hear a voice in the distance ask...")

hp = 100
hp1 = random.randint(1, 7)
hp2 = random.randint(10, 20)
hp3 = random.randint(97, 100)
Name = input("What is your name?: ").title()
print()
print(f"You tell the voice your name is {Name}. \nThere is no response...")
time.sleep(1)
print("You are confused of where the voice went, and where you are...\nYou notice a shadow in the distance, maybe a building.")
print()
Choice_1 = int(input("Do you get up and travel to the structure [press 1] or take off hazmat suit? [press 2]: "))
print()

if Choice_1 == 1:
    print("You get up from the ground and notice a pain in your shoulder.")
    hp = hp - hp1
    time.sleep(1)
    print(f"You lose {hp1} health due to an unknown reason... Your health is now {hp}/100")
    print()
else:
    print("You take off your hazmat suit and suddenly die of asphyxia and radiation poisoning.")
    time.sleep(1)
    hp = hp - 100
    print()
    print(f"Your health points are {hp}/100")
    print('Game Over!'.center(82,'-'))
    exit()

Choice_2 = int(input("Do you keep going to structure [press 1] or inspect injury [press 2]?: "))
print()
if Choice_2 == 1:
    print(f"{Name} keeps going to structure and starts to feel light headed...")
    time.sleep(1)
    hp = hp - hp2
    print(f"You lost -{hp2} health. Your current health is {hp}/100")
    time.sleep(1)
    print()
    Choice_2p = int(input("Do you stop and inspect injury [press 1] or ignore the light headedness and continue towards the structure? [press 2]?: "))
    if Choice_2p == 1:
        print(f"{Name} stops to inspect the injury and finds that he is bleeding out. In a few minutes {Name} will bleed out.")
        time.sleep(.75)
        hp = hp - hp2
        print(f"Your current health is {hp}/100 after losing -{hp2}")
        print()
    elif Choice_2p == 2:
        print("You start to lose consciousness. \nThe world fades to black...")
        time.sleep(1)
        print(f"You lose -{hp} out of {hp}/100 health")
        time.sleep(.5)
        print('You are dead, Game Over!'.center(32,'-'))
        exit()
    Choice_2l = int(input("Do you sit down on the ground and accept your fate [press 1] or do you look for a quick fix? [press 2]: " ))
    if Choice_2l == 1:
        print(f"{Name} has accepted their fate and they are at peace as they watch the world fade away slowly...")
        time.sleep(1)
        print()
        print(f"You lose -{hp} out of {hp}/100 health")
        time.sleep(.5)
        print('You bled out, Game Over!'.center(92,'-'))
        exit()
    elif Choice_2l == 2:
        print(f"You quickly look around for something to wrap the injury in to stop the bleeding. \nYou find nothing... \n{Name} Passes away in a panic while looking for a bandage...")
        time.sleep(1)
        print()
        print(f"You lose -{hp} out of {hp}/100 health")
        time.sleep(.5)
        print('Game Over!'.center(81,'-'))
        exit()

elif Choice_2 == 2:
    print(f"{Name} takes a moment to look at their injury, It is a cut that is bleeding. \n{Name} see's a bandage a few feet from him and uses it. \nThis helps but does not completely fix the problem...")
    time.sleep(1)
    print()
    hp = hp - hp2
    print(f"You lose -{hp2} out of {hp}/100 health")
Choice_3 = int(input("Do you keep going to structure in hopes of finding help [press 1] or go back to the place you woke up at? [press 2]: "))
if Choice_3 == 1:
    print("You continue towards the structure and just before you get there you start to pass out. \nJust before you fully pass out you see someone walking towards you, \nbut you are unable to do anything.")
    time.sleep(1)
    print(f"You lose -{hp2} out of {hp}/100 health")
    Choice_3p = int(input("You wake up in a small hut in an unknown location, \nDo you look for someone [press 1] or look for information in the hut? [press 2]: "))
    if Choice_3p == 1:
        print()
        print("You exit the small hut and start looking for someone nearby. You see a truck moving in the distance, \nAs you come closer to the truck you realize that they are armed and may not be friendly.")
        print("Your suspicions were proven to be valid as the people in the truck start shooting at you.")
        time.sleep(1)
        print()
        print(f"{Name} does not make it...")
        print(f"You lose -{hp} out of {hp}/100 health")
        print('You were killed by unknown survivors in a truck...Game Over!'.center(81,'-'))
        exit()
    elif Choice_3p == 2:
        print()
        print("You get up off the ground and look around for any information of where you are. You find a news paper dated 9/17/2031, \nThe front headline says 'The End of Civilization?' under is a story about nuclear war between the U.S. and Russia...")
        time.sleep(1)
        print()
        print(f"Your final health is {hp}/100 points")
        print(f"You Won the game {Name}! Hopefully you can survive the fallout...".center(80,'-'))
        exit()
elif Choice_3 == 2:
    print(f"{Name} starts to run back to the place they woke up at. \nWhen they get there they find a bandage and use it to stop the bleeding.")
    time.sleep(1.5)
    print("after the stress of finding something to stop the bleeding settles you look around and realize that the structures you have been seeing...\nare ruins of what once were...the world looks as though it were a postapocolyptic warzone...\nA half burned news paper blows by in the wind, you catch it and read the headline.\nWEDNESDAY, SEP 17th, 2031 - 'The End of Civilization?' under is a story about nuclear war between the U.S. and Russia...")
    print()
    time.sleep(1.5)
    hp = hp + hp1
    print(f"You gain {hp1} out of {hp}/100 health")
    print(f"You Won the game {Name}! You found out the truth about the war...".center(80,'-'))
    exit()