#!/usr/bin/python3
#import time
import random
import imp
modl = imp.load_source('ppFunctions', '../00/ppFunctions.py')
import os
from ppFunctions import *
from termcolor import colored, cprint
#sleep becouse of loading midi modules
print("Are you ready?")
time.sleep(1)

print_status = lambda x: cprint(x, 'white', 'on_blue')
print_help = lambda x: cprint(x, 'red')

def updateScreenStatus():
    os.system('clear')
    print_status("Status: round=" + str(rounde) + ", hit=" + str(hit))
    print_help("Help: rEPEAT sKIP")

hit = 0
rounde = 1
done = False

definedTones = stringToMidiNum("c e g")
practiceTonesRange = generatePracticeTonesRange("c", "c'", "black")

while True:
  try:
    updateScreenStatus()
    randomNotes = chooseTonesFromGivenList(2, practiceTonesRange)
    playHarmonicNotes(definedTones)
    playHarmonicNotes(randomNotes)
    while not done:
        guessedNotes = input("Your input:").split()
        if (guessedNotes[0] == "r"):
            print("Repeating...")
            playHarmonicNotes(definedTones)
            playHarmonicNotes(randomNotes)
        elif (guessedNotes[0] == "s"):
            print("Skiping...")
            done = True
        elif (not isSyntaxValid(guessedNotes)): print("What? Syntax error!")
        else:
            if (areTonesCorrect(randomNotes, guessedNotes)):
                print("Yea!")
                hit += 1
                rounde += 1
                done = True
            else:
                print("Almost!")
                hit = 0
    done = False
  except (KeyboardInterrupt):
    print('...Program Stopped Manually!')
    raise
