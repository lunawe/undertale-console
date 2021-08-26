import os

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
logo_len = len("Press Enter...")
y = int((int(cols) - logo_len) / 2)
input(f"{space*y}Press Enter...")