#!/usr/bin/env python

from subprocess import Popen, DEVNULL, STDOUT
import signal

CMD_ORGAN = 'PIPEWIRE_LATENCY="64/48000" pw-jack jalv -i -s http://gareus.org/oss/lv2/b_synth'

class Organ:
    def __init__(self):
        self.process = None
        self.start()

    def __del__(self):
        self.stop()

    def start(self):
        if self.process is None:
            self.process = Popen(CMD_ORGAN, shell=True, stdout=DEVNULL, stderr=STDOUT)

    def stop(self):
        if self.process is not None:
            self.process.send_signal(signal.SIGINT)
            self.process = None

if __name__ == "__main__":
    organ = Organ()
    organ.start()
