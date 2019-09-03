#!/usr/bin/env python3

from gpiozero import MCP3008
from time import sleep
from psonic import *
from RPi_GPIO_Rotary import rotary

def proper_round(num, dec=0):
    num = str(num)[:str(num).index('.')+dec+2]
    if num[-1]>='5':
        return float(num[:-2-(not dec)]+str(int(num[-2-(not dec)])+1))
    return float(num[:-1])

# Define some constants to determine which GPIO pins the encoders connect to
CLK_ONE = 17
DT_ONE  = 18
SW_ONE  = 27

CLK_TWO = 5
DT_TWO  = 6
SW_TWO  = 13

# Set up chord and style switching on encoder 1
all_chords   = ['Cs', 'Db', 'D', 'Ds', 'Eb', 'E', 'F', 'Fs', 'Gb', 'G', 'Gs', 'Ab', 'A', 'As', 'Bb', 'B']
chord_styles = ['major', 'minor', 'major7', 'dom7', 'minor7', 'aug', 'dim', 'dim7', '1', "5", "+5", "m+5", "sus2", "sus4", "6", "m6", "7sus2", "7sus4", "7-5", "m7-5", "7+5", "m7+5", "9", "m9", "m7+9", "maj9", "9sus4", "6*9", "m6*9", "7-9", "m7-9", "7-10", "9+5", "m9+5", "7+5-9", "m7+5-9", "11", "m11", "maj11", "11+", "m11+", "13", "m13", "M", "m", "7", "M7", "m7", "augmented", "a", "diminished", "i", "diminished7", "i7"]
max_chords   = len(all_chords) - 1
max_styles   = len(chord_styles) - 1

selected_chord = 0
selected_style = 0

def chord_change_callback():
    global selected_chord
    selected_chord += 1
    print('Selected chord: ', selected_chord)

def next_style():
    global selected_style
    global max_styles
    if (selected_style + 1) > max_styles:
        print('Max chord styles reached')
    else:
        selected_style += 1
        print('Current chord style: ', selected_style)

def previous_style():
    global selected_style
    if (selected_style - 1) < 1:
        print('Minimum style reached')
    else:
        selected_style -= 1
        print('Selected style: ', selected_style)

# Set up chord encoder to choose chords
chord_encoder = rotary.Rotary(CLK_ONE, DT_ONE, SW_ONE, 2)
chord_encoder.register(increment=next_style, decrement=previous_style, pressed=chord_change_callback)
chord_encoder.start()


# Set up synth switching on encoder 2
synth = 0
synths = [DULL_BELL, PRETTY_BELL, SINE, SQUARE, PULSE, SUBPULSE, DTRI, DPULSE, FM, MOD_FM, MOD_SAW, MOD_DSAW, MOD_SINE, MOD_TRI, MOD_PULSE, SUPERSAW, HOOVER, SYNTH_VIOLIN, PLUCK, PIANO, GROWL, DARK_AMBIENCE, DARK_SEA_HORN, HOLLOW, ZAWA, NOISE, GNOISE, BNOISE, CNOISE, DSAW, TB303, BLADE, PROPHET, SAW, BEEP, TRI, CHIPLEAD, CHIPBASS, CHIPNOISE, TECHSAWS, SOUND_IN, SOUND_IN_STEREO]
max_synths = len(synths) - 1
inversion = 1

def synth_change_callback():
    global synth
    synth += 1
    print('Selected synth: ', synths[synth])

def next_inversion():
    global inversion
    inversion += 1
    print('Inversion: ', inversion)

def previous_inversion():
    global inversion
    if (inversion - 1) < 1:
        print('Lower inversion limit reached')
    else:
        inversion -= 1
        print('Inversion: ', inversion)

# Set up synth encoder to choose synth
synth_encoder = rotary.Rotary(CLK_TWO, DT_TWO, SW_TWO, 2)
synth_encoder.register(increment=next_inversion, decrement=previous_inversion, pressed=synth_change_callback)
synth_encoder.start()

# Read from the pots
# pot_1 = MCP3008(channel=0)
# pot_2 = MCP3008(channel=1)
# pot_3 = MCP3008(channel=2)
# pot_4 = MCP3008(channel=3)
# pot_5 = MCP3008(channel=4)
# pot_6 = MCP3008(channel=5)
pot_7 = MCP3008(channel=6)
pot_8 = MCP3008(channel=7)

while True:
    sleep_time = pot_7.value
    octave     = pot_8.value
    octave     = int(proper_round(octave * 10))
    use_synth(synths[synth])
    print(proper_round(sleep_time, 1))
    print(all_chords[selected_chord] + str(octave), chord_styles[selected_style], inversion)
    play(all_chords[selected_chord] + str(octave), chord_styles[selected_style])
    sleep(proper_round(sleep_time, 1))
    play(all_chords[selected_chord], chord_styles[selected_style], inversion=inversion)
    sleep(proper_round(sleep_time, 1))
    play(all_chords[selected_chord], chord_styles[selected_style], inversion=inversion)
    sleep(proper_round(sleep_time, 1))
    play(all_chords[selected_chord], chord_styles[selected_style])
    sleep(proper_round(sleep_time, 1))
