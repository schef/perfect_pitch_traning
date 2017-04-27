import rtmidi
import time

class player:
    def __init__(self):
        self.name = "svirko"
        self.velocity = 112
        self.duration = 1
        self.midiout = rtmidi.MidiOut()
        self.midiout.open_virtual_port(self.name)
    def toneOn(self, midi):
        self.midiout.send_message([0x90, midi, self.velocity])
    def toneOff(self, midi):
        self.midiout.send_message([0x80, midi, 0])
    def playMelodicly(self, tones):
        for tone in tones:
            self.toneOn(tone)
            time.sleep(self.duration)
            self.toneOff(tone)
    def playHarmonicly(self, tones):
        for tone in tones:
            self.toneOn(tone)
        time.sleep(self.duration)
        for tone in tones:
            self.toneOff(tone)

