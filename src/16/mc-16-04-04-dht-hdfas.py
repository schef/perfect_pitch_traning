#!/usr/bin/python3
#import time
import random
import imp
modl = imp.load_source('ppFunctions', '../00/ppFunctions.py')
logo = imp.load_source('logo', '../00/logo.py')
import os
from ppFunctions import *
from termcolor import colored, cprint
os.system('clear')
from logo import *
#sleep becouse of loading midi modules
print_logo()
time.sleep(1)

print_status = lambda x: cprint(x, 'white', 'on_blue')
print_help = lambda x: cprint(x, 'red')

hit = 0
rounde = 1
done = False


choiceList = [ "h,", "d", "f", "as"]
generatedList = []
for i in choiceList:
    generatedList.append(stringToMidiNum(i))
while True:
  try:
    os.system('clear')
    print_logo()
    print_status("Status: round=" + str(rounde) + ", hit=" + str(hit))
    print_help("Help: rEPEAT sKIP")
    randomNotes = []
    copyGeneratedList = list(generatedList)
    for i in range(2):
        randomNotes.append(random.choice(copyGeneratedList))
        copyGeneratedList.remove(randomNotes[-1])
    randomNotes.sort()
    #print(randomNotes)
    playHarmonicNotes(randomNotes)
    while not done:
        guessedNote = input("Your input: ")
        splitedGuessedNotes = guessedNote.split()
        print(splitedGuessedNotes)
        if guessedNote == "r":
            print("Repeating...")
            playHarmonicNotes(randomNotes)
        elif guessedNote == "s":
            print("Skiping...")
            done = True
        elif any([x for x in splitedGuessedNotes if x not in lilypondTones]):
            print("What? Syntax error!")
        else:
            if (lilypondTones[splitedGuessedNotes[0]] == randomNotes[0]%12 and lilypondTones[splitedGuessedNotes[1]] == randomNotes[1]%12):
                print("Yea!")
                hit += 1
                rounde += 1
                done = True
            else:
                print("Almost!")
                playHarmonicNotes(randomNotes)
                #playHarmonicNotes((lilypondTones[splitedGuessedNotes[0]]+60,lilypondTones[splitedGuessedNotes[1]]+60))
                hit = 0
    done = False
  except (KeyboardInterrupt):
    print('...Program Stopped Manually!')
    raise
