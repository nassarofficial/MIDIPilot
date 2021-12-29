#!/usr/bin/env python

from __future__ import print_function

import sys
import time
import argparse
import json

import rtmidi
from rtmidi.midiutil import open_midiinput, open_midioutput
from rtmidi.midiconstants import CONTROL_CHANGE, PROGRAM_CHANGE

class MidiInputHandler(object):
    def __init__(self, port=0):
        super(MidiInputHandler, self).__init__()
        self.port = port
        self._wallclock = time.time()
        with open("config.json") as json_data_file:
            data = json.load(json_data_file)
        self.QC_TO_MIDI = data["QC_TO_MIDI"]
        self.MIDI_TO_QC = data["MIDI_TO_QC"]

    def change_mode(message):
        midiout_GCP.send_message([CONTROL_CHANGE, message[0], message[2]])

    def __call__(self, event, data=None):
        message, deltatime = event
        self._wallclock += deltatime
        print("[%s] @%0.6f %r %s" % (self.port, self._wallclock, \
            message, self.MIDI_TO_QC[str(message[1])]))

        if self.MIDI_TO_QC[str(message[1])] == "reset":
            # CC#0 value 1, CC#32 value 5, Program #1
            midiout_GCP.send_message([CONTROL_CHANGE, 0, 0]) 
            midiout_GCP.send_message([CONTROL_CHANGE, 32, 6]) 
            midiout_GCP.send_message([PROGRAM_CHANGE, 0, 1])
            midiout_GCP.send_message([CONTROL_CHANGE, 46, 127]) 

        elif self.MIDI_TO_QC[str(message[1])] == "scene":
            MidiInputHandler.change_mode(self.QC_TO_MIDI["scene"])

        elif self.MIDI_TO_QC[str(message[1])] == "stomp":
        	MidiInputHandler.change_mode(self.QC_TO_MIDI["stomp"])

        elif self.MIDI_TO_QC[str(message[1])] == "preset":
        	MidiInputHandler.change_mode(self.QC_TO_MIDI["preset"])

        elif self.MIDI_TO_QC[str(message[1])] == "smpA":
            cc = self.QC_TO_MIDI["smpA"][0]
            MidiInputHandler.change_mode(self.QC_TO_MIDI["stomp"])
            midiout_GCP.send_message([CONTROL_CHANGE, cc, 0])
            MidiInputHandler.change_mode(self.QC_TO_MIDI["scene"])

        elif self.MIDI_TO_QC[str(message[1])] == "smpB":
            cc = self.QC_TO_MIDI["smpB"][0]
            MidiInputHandler.change_mode(self.QC_TO_MIDI["stomp"])
            midiout_GCP.send_message([CONTROL_CHANGE, cc, self.QC_TO_MIDI["smpB"][2]])
            MidiInputHandler.change_mode(self.QC_TO_MIDI["scene"])

        elif self.MIDI_TO_QC[str(message[1])] == "smpC":
            cc = self.QC_TO_MIDI["smpC"][0]
            MidiInputHandler.change_mode(self.QC_TO_MIDI["stomp"])
            midiout_GCP.send_message([CONTROL_CHANGE, cc, self.QC_TO_MIDI["smpC"][2]])
            MidiInputHandler.change_mode(self.QC_TO_MIDI["scene"])

        elif self.MIDI_TO_QC[str(message[1])] == "smpD":
            cc = self.QC_TO_MIDI["smpD"][0]
            MidiInputHandler.change_mode(self.QC_TO_MIDI["stomp"])
            midiout_GCP.send_message([CONTROL_CHANGE, cc, self.QC_TO_MIDI["smpD"][2]])
            MidiInputHandler.change_mode(self.QC_TO_MIDI["scene"])

        elif self.MIDI_TO_QC[str(message[1])] == "smpE":
            cc = self.QC_TO_MIDI["smpE"][0]
            MidiInputHandler.change_mode(self.QC_TO_MIDI["stomp"])
            midiout_GCP.send_message([CONTROL_CHANGE, cc, self.QC_TO_MIDI["smpE"][2]])
            MidiInputHandler.change_mode(self.QC_TO_MIDI["scene"])

        elif self.MIDI_TO_QC[str(message[1])] == "smpF":
            cc = self.QC_TO_MIDI["smpF"][0]
            MidiInputHandler.change_mode(self.QC_TO_MIDI["stomp"])
            midiout_GCP.send_message([CONTROL_CHANGE, cc, self.QC_TO_MIDI["smpF"][2]])
            MidiInputHandler.change_mode(self.QC_TO_MIDI["scene"])

        elif self.MIDI_TO_QC[str(message[1])] == "smpG":
            cc = self.QC_TO_MIDI["smpG"][0]
            MidiInputHandler.change_mode(self.QC_TO_MIDI["stomp"])
            midiout_GCP.send_message([CONTROL_CHANGE, cc, self.QC_TO_MIDI["smpG"][2]])
            MidiInputHandler.change_mode(self.QC_TO_MIDI["scene"])

        elif self.MIDI_TO_QC[str(message[1])] == "smpH":
            cc = self.QC_TO_MIDI["smpH"][0]
            MidiInputHandler.change_mode(self.QC_TO_MIDI["stomp"])
            midiout_GCP.send_message([CONTROL_CHANGE, cc, self.QC_TO_MIDI["smpH"][2]])
            MidiInputHandler.change_mode(self.QC_TO_MIDI["scene"])


with open("config.json") as json_data_file:
    data = json.load(json_data_file)

try:
    midiin_GCP, port_name_GCP = open_midiinput(0)
    midiout_GCP, port_name_GCP = open_midioutput(0)

except (EOFError, KeyboardInterrupt): 
    sys.exit()

print("MIDIPilot | Starting")
midiin_GCP.set_callback(MidiInputHandler(port_name_GCP))

print("Waiting for MIDI Input Loopp. Control-C to exit.")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print('')
finally:
    print("Exit.")
    midiin.close_port()
    del midiin
