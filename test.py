import keyboard
import os

def startTest():
    #Game loop:
    while True:
        rows,cols = os.popen('stty size', 'r').read().split()
        testchar = "e"
        world = ""
        world = testchar*rows
        print(world)