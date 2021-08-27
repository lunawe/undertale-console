import os
import keyboard
from time import sleep

def clear():
    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

mainOptions = [
    "Fight",
    "Act",
    "Item",
    "Mercy"
]

#made them emoji, if u dont like it tell me on dc
#some of them got rendered as two characters and i had to fix that, thats why the heart and fight icon aren't emojis, but i think they look fine
icons = [
    "⚔",
    "🔊",
    "💰",
    "❎",
    "❤"
]

keys = {
    "right":1,
    "left":-1,
    "enter":0,
    "z":0
}

def fightMenu(options, icons, selectionStart = 0):

    #Displaying the options to the player
    selectedOption = selectionStart
    output = ""
    #trying to center it HELP MEEEEEE
    height,width = os.popen('stty size', 'r').read().split()
    width = int(width)
    height = int(height)
    for y in range(height):
        for x in range(width):
            output += " "
        output += "\n"
    for i in range(int((width - len("# Fight  # Act  # Item  # Mercy")) / 2)):
        output += " "

    for i in range(len(options)):
        #cycle through the options
        try:
            #using try cuz len(optins) can go over, but len(options) - 1 messes things up
            if(i == selectedOption):
                #if its selected, we print the heart: icons[-1]
                #yes, weird approach but it was gliitttchy before 4 some reason
                output += str(icons[-1]) + " " + str(options[i]) + "  "
            else:
                output += str(icons[i]) + " " + str(options[i]) + "  "
        except:
            pass
    print(output)
    while True:
        #Making the player decide
        userinput = keyboard.read_key()
        if not keyboard.is_pressed(userinput):
            action = keys.get(userinput, "")
            if action in keys.values():
                if action == 0:
                    print("INTERACTED!!!")
                    return
                selectedOption += action
                if selectedOption < 0:
                    selectedOption = 3
                elif selectedOption > 3:
                    selectedOption = 0
                fightMenu(options, icons, selectedOption)

fightMenu(mainOptions,icons)