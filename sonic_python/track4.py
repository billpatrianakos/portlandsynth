#!/usr/bin/env python3

from gpiozero import MCP3008
from time import sleep
from psonic import *
from pigpio_encoder import pigpio_encoder
# sudo apt-get install pigpio python-pigpio python3-pigpio
# pip install pigpio_encoder
# sudo systemctl enable pigpiod # to enable pigpiod at startup
# sudo pigpiod # to start manually

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
chords       = ['Cs', 'Db', 'D', 'Ds', 'Eb', 'E', 'F', 'Fs', 'Gb', 'G', 'Gs', 'Ab', 'A', 'As', 'Bb', 'B']
chord_styles = ['major', 'minor', 'major7', 'dom7', 'minor7', 'aug', 'dim', 'dim7', '1', "5", "+5", "m+5", "sus2", "sus4", "6", "m6", "7sus2", "7sus4", "7-5", "m7-5", "7+5", "m7+5", "9", "m9", "m7+9", "maj9", "9sus4", "6*9", "m6*9", "7-9", "m7-9", "7-10", "9+5", "m9+5", "7+5-9", "m7+5-9", "11", "m11", "maj11", "11+", "m11+", "13", "m13", "M", "m", "7", "M7", "m7", "augmented", "a", "diminished", "i", "diminished7", "i7"]
max_chords   = len(chords) - 1
max_styles   = len(chord_styles) - 1

selected_chord = 0
selected_style = 0

def chord_change_callback(counter):
    global selected_chord
    selected_chord = counter
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

chord_encoder = pigpio_encoder.Rotary(clk=CLK_ONE, dt=DT_ONE, sw=SW_ONE)
chord_encoder.setup_rotary(min=0, max=max_chords, scale=1, debounce=300, rotary_callback=chord_change_callback)
chord_encoder.setup_switch(debounce=300, long_press=True, sw_short_callback=next_style, sw_long_callback=previous_style)

chord_encoder.watch()

# Set up synth switching on encoder 2
synth = 0
synths = [DULL_BELL, PRETTY_BELL, SINE, SQUARE, PULSE, SUBPULSE, DTRI, DPULSE, FM, MOD_FM, MOD_SAW, MOD_DSAW, MOD_SINE, MOD_TRI, MOD_PULSE, SUPERSAW, HOOVER, SYNTH_VIOLIN, PLUCK, PIANO, GROWL, DARK_AMBIENCE, DARK_SEA_HORN, HOLLOW, ZAWA, NOISE, GNOISE, BNOISE, CNOISE, DSAW, TB303, BLADE, PROPHET, SAW, BEEP, TRI, CHIPLEAD, CHIPBASS, CHIPNOISE, TECHSAWS, SOUND_IN, SOUND_IN_STEREO]
max_synths = len(synths) - 1
inversion = 1

def synth_change_callback(counter):
    global synth
    synth = counter
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

synth_encoder = pigpio_encoder.Rotary(clk=CLK_TWO, dt=DT_TWO, sw=SW_TWO)
synth_encoder.setup_rotary(min=0, max=max_synths, scale=1, debounce=300, rotary_callback=synth_change_callback)
synth_encoder.setup_switch(debounce=300, long_press=True, sw_short_callback=next_inversion, sw_long_callback=previous_inversion)

synth_encoder.watch()

# Read from the pots
pot_1 = MCP3008(channel=0)
pot_2 = MCP3008(channel=1)
pot_3 = MCP3008(channel=2)
pot_4 = MCP3008(channel=3)
pot_5 = MCP3008(channel=4)
pot_6 = MCP3008(channel=5)
pot_7 = MCP3008(channel=6)
pot_8 = MCP3008(channel=7)

while True:
    sleep_time = pot_7.value
    use_synth(synths[synth])
    print(proper_round(sleep_time, 1))
    play(chord(chords[selected_chord], chord_styles[selected_style]))
    sleep(proper_round(sleep_time, 1))
    play(chord(chords[selected_chord], chord_styles[selected_style], inversion=inversion))
    sleep(proper_round(sleep_time, 1))
    play(chord(chords[selected_chord], chord_styles[selected_style], inversion=inversion))
    sleep(proper_round(sleep_time, 1))
    play(chord(chords[selected_chord], chord_styles[selected_style]))
    sleep(proper_round(sleep_time, 1))
