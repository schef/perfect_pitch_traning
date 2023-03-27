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
    MIDI_BASE = 60

