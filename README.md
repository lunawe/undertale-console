# undertale-console
Undertale, but it's completely text-based and runs in terminal...

# How to install
You must be root to run the script if you're using a \*nix system (ex. MacOS), but you can run it without admin on NT-based systems(Windows)
```
pip install keyboard
```
or
```
pip3 install keyboard
```

Then:
```
sh main.sh 
```
or for NT-based systems:
```
main.bat
```

# Bugs
Your terminal may tell you that you need to be root to use keyboard/module keyboard is not found.
That means that you only installed keyboard in your home directory and not in the superuser directory.
If so, type this in your terminal:
```
sudo pip3 install keyboard
```
The game should then work.
