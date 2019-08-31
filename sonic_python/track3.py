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

note = 1
def note_up():
    global note
    if note == 127:
        pass
    elif note == 0:
        note = 1
    else:
        note += 1

def note_down():
    global note
    if note == 1:
        pass
    else:
        note -= 1

def reset_note():
    global note
    note = 1

# Set up note encoder to choose notes
note_encoder = rotary.Rotary(CLK_ONE, DT_ONE, SW_ONE, 2)
note_encoder.register(increment=note_up, decrement=note_down, pressed=reset_note)
note_encoder.start()

synth = 0
def next_synth():
    global synth
    if synth >= 8:
        pass
    else:
        synth += 1

def last_synth():
    global synth
    if synth <= 0:
        synth = 0
    else:
        synth -= 1

def reset_synth():
    global synth
    synth = 0

# Set up synth select encoder
synth_encoder = rotary.Rotary(CLK_TWO, DT_TWO, SW_TWO, 2)
synth_encoder.register(increment=next_synth, decrement=last_synth, pressed=reset_synth)
synth_encoder.start()

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
    # Potentiometer driven controls
    attack        = pot_1.value
    decay         = pot_2.value
    sustain       = pot_3.value
    release       = pot_4.value
    sustain_level = pot_5.value
    interval_1    = pot_6.value
    interval_2    = pot_7.value

    note1 = note
    note2 = note + int(proper_round(interval_1 * 10))
    note3 = note2 + int(proper_round(interval_2 * 10))

    if synth == 0:
        use_synth(SAW)
        play(note1, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
        sleep(0.5)
        play(note2, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
        sleep(1)
        play(note3, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
        sleep(0.5)
    elif synth == 1:
        use_synth(MOD_FM)
        play(note1, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
        sleep(0.5)
        play(note2, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
        sleep(1)
        play(note3, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
        sleep(0.5)
    elif synth == 2:
        use_synth(MOD_TRI)
        play(note1, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
        sleep(0.5)
        play(note2, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
        sleep(1)
        play(note3, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
        sleep(0.5)
    elif synth == 3:
        use_synth(GROWL)
        play(note1, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
        sleep(0.5)
        play(note2, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
        sleep(1)
        play(note3, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
        sleep(0.5)
    elif synth == 4:
        use_synth(HOLLOW)
        play(note1, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
        sleep(0.5)
        play(note2, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
        sleep(1)
        play(note3, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
        sleep(0.5)
    elif synth == 5:
        use_synth(BLADE)
        play(note1, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
        sleep(0.5)
        play(note2, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
        sleep(1)
        play(note3, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
        sleep(0.5)
    elif synth == 6:
        use_synth(BLADE)
        play(note1, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
        sleep(0.5)
        play(note2, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
        sleep(1)
        play(note3, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
        sleep(0.5)
    elif synth == 7:
        use_synth(CHIPNOISE)
        play(note1, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
        sleep(0.5)
        play(note2, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
        sleep(1)
        play(note3, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
        sleep(0.5)
    elif synth == 8:
        use_synth(DSAW)
        play(note1, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
        sleep(0.5)
        play(note2, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
        sleep(1)
        play(note3, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
        sleep(0.5)
    else:
        print(attack, decay, sustain, release, sustain_level, interval_1, interval_2, note1, note2, note3)
