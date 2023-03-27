#!/usr/bin/env python

from dataclasses import dataclass
from common import run_bash_cmd
from time import sleep

CMD_PORT_LIST = "jack_lsp"
CMD_CONNECT = "jack_connect"

@dataclass
class Connection():
    name: str
    channels: list[str]

    @staticmethod
    def get_ports() -> list[str]:
        return run_bash_cmd(CMD_PORT_LIST)

    def get(self) -> list[str]:
        ports = []
        for channel in self.channels:
            for port in Connection.get_ports():
                if self.name in port and channel in port:
                    ports.append(port)
                    break
        return ports

class Connector:
    def __init__(self):
        self.audio_soundcard_ucm204hd = Connection("UMC204HD", ["playback_AUX0", "playback_AUX1"])
        self.audio_soundcard_builtin = Connection("Built-in", ["playback_FL", "playback_FR"])
        self.audio_instrument_organ = Connection("setBfree", ["outL", "outR"])
        self.midi_keyboard_isometric = Connection("Pico", ["capture_0"]) 
        self.midi_instrument_organ = Connection("setBfree", ["control"])
        self.midi_player_ppt = Connection("RtMidiOut", ["ppt"])
    
    @staticmethod
    def wait_for_port(connection: Connection):
        max_timeout = 1.0
        timeout_counter = 0.0
        timeout_step = 0.05
        while(True):
            if len(connection.get()):
                break
            sleep(timeout_step)
            timeout_counter += timeout_step
            if timeout_counter >= max_timeout:
                break


    @staticmethod
    def connect_ports(from_connection: Connection, to_connection: Connection):
        Connector.wait_for_port(from_connection)
        Connector.wait_for_port(to_connection)
        from_ports = from_connection.get()
        to_ports = to_connection.get()
        if len(from_ports) != len(to_ports):
            print(f"ERROR, port mismatch: {from_ports} != {to_ports}")
            return

        for i in range(len(from_ports)):
            cmd = f"{CMD_CONNECT} \"{from_ports[i]}\" \"{to_ports[i]}\""
            run_bash_cmd(cmd)

    def connect_home(self):
        self.connect_ports(self.midi_keyboard_isometric, self.midi_instrument_organ)
        self.connect_ports(self.midi_player_ppt, self.midi_instrument_organ)
        self.connect_ports(self.audio_instrument_organ, self.audio_soundcard_ucm204hd)

    def connect_office(self):
        self.connect_ports(self.midi_player_ppt, self.midi_instrument_organ)
        self.connect_ports(self.audio_instrument_organ, self.audio_soundcard_builtin)

    def connect(self):
        self.connect_home()
        #self.connect_office()

if __name__ == "__main__":
    connector = Connector()
    connector.connect()
