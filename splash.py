import os
import keyboard
import test

def clear():
    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

clear()

rows,cols = os.popen('stty size', 'r').read().split()
logo_height = 3
space = " "
try:
    x = int(int(rows) / 2)
except:
    x = int(rows) / 2

splash1 = "█ █ █▄ █ █▀▄ █▀▀ █▀█ ▀█▀ ▄▀█ █   █▀▀"
splash2 = "█▄█ █ ▀█ █▄▀ ██▄ █▀▄  █  █▀█ █▄▄ ██▄"
splash3 = "          Terminal Edition"

logo_len = len(splash1)
y = int((int(cols) - logo_len) / 2)

splash = [
    splash1,
    splash2,
    splash3
]

print("\n"*x)
for i in splash:
    print(" "*y,i)
print("\n"*(x-1))
logo_len = len("Press Z...")
y = int((int(cols) - logo_len) / 2)
print(f"{space*y}Press Z...")
#Waiting for them 2 press Z
while True:
    userinput = keyboard.read_key()
    if userinput in ["z", "enter"]:
        break
test.startTest()