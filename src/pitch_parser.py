import re
from enum import Enum

OCTAVE = 12

class Pitch():
    def __init__(self, index: int, pitch_name: str, octave: int = 4):
        self.index = index
        self.pitch_name = pitch_name
        self.octave = octave

    def get_pitch(self) -> int:
        return self.octave * OCTAVE + self.index

class Pitches(Pitch, Enum):
    C = 0, 1
    CIS = 1, "cis"
    D = 2, "d"
    DIS = 3, "dis"
    E = 4, "e"
    F = 5, "f"
    FIS = 6, "fis"
    G = 7, "g"
    GIS = 8, "gis"
    A = 9, "a"
    AIS = 10, "ais"
    H = 11, "h"
    DES = 1, "des"
    ES = 3, "es"
    GES = 6, "ges"
    AS = 8, "as"
    B = 10, "b"
    

class PitchParser:
    MIDI_BASE = 48

    def is_midi_pitch(self, midi, pitch):
        pitch = re.sub('[\',]', '', pitch)
        return midi % 12 == self.pitchMidiBase[pitch]

    def get_pitch_base(self, pitch):
        pitch = re.sub('[\',]', '', pitch)
        return pitch

    def get_octave_from_pitch(self, pitch):
        octave = 0
        for i in pitch:
            if i == "'":
                octave += 1
            elif i == ",":
                octave -= 1
        return self.MIDI_BASE + octave * 12

    def get_midi_from_pitch(self, pitch):
        octave = self.get_octave_from_pitch(pitch)
        pitch = re.sub('[\',]', '', pitch)
        return self.pitchMidiBase[pitch] + octave

    def get_octave_from_midi(self, midi):
        rest = midi % 12
        center = int(self.MIDI_BASE / 12)
        octave = int((midi - rest) / 12)
        centerOctave = (octave - center)
        if centerOctave > 0:
            return "'" * centerOctave
        elif centerOctave < 0:
            return "," * abs(centerOctave)
        else:
            return ""

    def get_pitch_from_midi(self, midi):
        octave = self.get_octave_from_midi(midi)
        for name, midiBase in self.pitchMidiBase.items():
            if midiBase == midi % 12:
                return name + octave
        return ''

    def get_midi_list_from_pitch_list(self, pitchList):
        midiList = []
        for pitch in pitchList:
            midiList.append(self.get_midi_from_pitch(pitch))
        return midiList

    def get_midi_base_from_midi(self, midi):
        return midi % 12

    def get_midi_base_from_pitch(self, pitch):
        midi = self.get_midi_from_pitch(pitch)
        return self.get_midi_base_from_midi(midi)
