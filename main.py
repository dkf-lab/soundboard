from playsound import playsound
import glob
import os
# find sounds in directory and put them in list
avaliableSounds = []
def scanDir():
    global avaliableSounds
    avaliableSounds = [f for f in glob.glob("*.mp3")] #add MP3 sounds to list
scanDir()
clear = lambda: os.system('cls')

while True:
    clear()
    print("Type 'exit' to exit or 'rescan' to scan for new files.")
    print('Avaliable Sounds:')
    count = 0
    for x in avaliableSounds:
        print(count, x)
        count += 1
    uinput = input('Which sound would you like to play? ')
    if uinput == ('rescan'):
        scanDir()
    if uinput == ('exit'):
        quit()
    else:
        try:
            playsound(avaliableSounds[int(uinput)])
        except ValueError:
            print('Enter an integer you twat!!')
