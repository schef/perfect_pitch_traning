#!/usr/bin/env python3

from connector import Connector
from organ import Organ
from midi_player import MidiPlayer
from time import sleep

organ = Organ()
player = MidiPlayer()
connector = Connector()

if __name__ == "__main__":
    connector.connect()
