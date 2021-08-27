import os
import keyboard
from time import sleep

def clear():
    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

mainOptions = [
    "", #Added a space so it'd be easier to make the thing
    "Fight",
    "Act",
    "Item",
    "Mercy"
]

icons = [
    "<3",
    "<=",
    "))",
    "&?"
    "><"
]

keys = {
    "Right":1,
    "Left":-1,
    "Enter":0
}

def fightMenu(options, icons):
    #Displaying the options to the player
    selectedOption = 0
    while True:
        for i in range(len(options) - 1):
            if(i == selectedOption):print(f"{icons[0]}{options[i]} ", end = "")
            else:print(f"{icons[i]}{options[i]} ", end = "")
        #Making the player decide
        select = keyboard.read_key()
        keys.get(select, "")
        if(select == ""):
            if(options[selectedOption] in options):print("Indev!");sleep(1);clear();break
        else:clear()
        clear()

fightMenu(mainOptions,icons)