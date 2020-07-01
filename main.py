from playsound import playsound
import glob
# find sounds in directory and put them in list
avaliableSounds = [f for f in glob.glob("*.mp3")] #add MP3 sounds to list

while True:
    print(''*3)
    print('Avaliable Sounds:')
    count = 0
    for x in avaliableSounds:
        print(count, x)
        count += 1
    uinput = input('Which sound would you like to play? ')
    if uinput == ('exit'):
        quit()
    else:
        try:
            playsound(avaliableSounds[int(uinput)])
        except ValueError:
            print('Enter an integer you twat!!')
