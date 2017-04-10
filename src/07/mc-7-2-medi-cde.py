#!/usr/bin/python
# Written by Stjepan Horvat
# ( zvanstefan@gmail.com )
# by the exercises from David Lucal Burge - Perfect Pitch Ear Traning Supercourse
# Thanks to Wojciech M. Zabolotny ( wzab@ise.pw.edu.pl ) for snd-virmidi example
# ( wzab@ise.pw.edu.pl )

import random
import time
import sys

fname="/dev/snd/midiC2D0"
#fname=sys.argv[1]
fin=open(fname,"rb")
fout=open(fname,"wb")
#keymin=int(sys.argv[2])
#keymax=int(sys.argv[3])
#keymin=int(60)
#keymax=int(72)

#c major scale
print ("Exercise 7-2:")
print ("Meditation: C, D and E. When ever we seat to practice we think of a tone and sing it. We need to correct our error.")
#from c to c'' white tones

#c major scale
#notes = [ 36, 38, 40, 41, 43, 45, 47, 48, 50, 52, 53, 55, 57, 59, 60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83, 84, 86, 88, 89, 91, 93, 95, 96 ]
#notes = [ 36, 38, 40, 48, 50, 52, 60, 62, 64, 72, 74, 76, 84, 86, 88, 96 ]
notes = [60, 62, 64 ]
noteC = [ 36, 48, 60, 72, 84, 96 ]

i = 0

def playNote(note):
  fout.write((chr(0x90)+chr(note)+chr(127)).encode('utf-8'))
  fout.flush()
  time.sleep(0.7)
  fout.write((chr(0x80)+chr(note)+chr(127)).encode('utf-8'))
  fout.flush()

def nameNote(note):
  if note in noteC:
    return("C")
  elif note-2 in noteC:
    return("D")
  elif note-4 in noteC:
    return("E")
  elif note-5 in noteC:
    return("F")
  elif note-7 in noteC:
    return("G")
  elif note-9 in noteC:
    return("A")
  elif note-11 in noteC:
    return("H")

usage = "Usage: 1-play, 2-next."
round = 1

try:
  print(usage)
  while True:
    note = random.choice(notes)
    match = False
    while not match:
      print (nameNote(note))
      done = False
      while not done:
        n = input("? ")
        if n == "?":
          print(usage)
        elif n == "1":
          playNote(note)
        elif n == "2":
          round += 1
          print("Next round. " + str(round) + ".:")
          done = True
          match = True
except KeyboardInterrupt:
  pass
