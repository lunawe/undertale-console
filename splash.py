import os

def clear():
    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

clear()

rows,cols_ = os.popen('stty size', 'r').read().split()
logo_height = 3
space = " "
try:
    rows = int(int(rows) / 2)
except:
    rows = int(rows) / 2

splash1 = "█ █ █▄ █ █▀▄ █▀▀ █▀█ ▀█▀ ▄▀█ █   █▀▀"
splash2 = "█▄█ █ ▀█ █▄▀ ██▄ █▀▄  █  █▀█ █▄▄ ██▄"
splash3 = "          Terminal Edition"

logo_len = len(splash1)
cols = int((int(cols_) - logo_len) / 2)

splash = [
    splash1,
    splash2,
    splash3
]

print("\n"*rows)
for i in splash:
    print(" "*cols,i)
print("\n"*(rows-1))
logo_len = len("Press Enter...")
cols = int((int(cols_) - logo_len) / 2)
input(f"{space*cols}Press Enter...")