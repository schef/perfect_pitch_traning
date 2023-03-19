import rtmidi
from pitch_parser import Pitch
import time

class MidiPlayer():
    NOTE_DURATION = 1
    CHANNEL = 0x90

    def __init__(self):
        self.midi = rtmidi.MidiOut()
        self.midi.open_virtual_port("ppt")

    def play(self, pitch: Pitch, state: bool):
        self.midi.send_message([MidiPlayer.CHANNEL, pitch.get_pitch(), (0, 100)[state]])

    def plays(self, pitches: list[Pitch], harmonically: bool = False):
        if not harmonically:
            for pitch in pitches:
                self.play(pitch, True)
                time.sleep(MidiPlayer.NOTE_DURATION)
                self.play(pitch, False)
        else:
            for pitch in pitches:
                self.play(pitch, True)
            time.sleep(MidiPlayer.NOTE_DURATION)
            for pitch in pitches:
                self.play(pitch, False)

    def panic(self):
        self.midi.send_message(rtmidi.MidiMessage.allNotesOff())

if __name__ == "__main__":
    from pitch_parser import Pitches
    midi_player = MidiPlayer()
    pitches = [Pitches.C, Pitches.E, Pitches.G]
    midi_player.plays(pitches)
