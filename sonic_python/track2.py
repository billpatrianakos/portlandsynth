from gpiozero import MCP3008
from time import sleep
from psonic import *
from threading import Thread
from pyky040 import pyky040

# Define some constants to determine which GPIO pins the encoders connect to
CLK_ONE = 17
DT_ONE  = 18
SW_ONE  = 27

CLK_TWO = 5
DT_TWO  = 6
SW_TWO  = 13

# Define some global variables to hold encoder state
enc1 = 1
enc2 = 0

def proper_round(num, dec=0):
    num = str(num)[:str(num).index('.')+dec+2]
    if num[-1]>='5':
        return float(num[:-2-(not dec)]+str(int(num[-2-(not dec)])+1))
    return float(num[:-1])

# Callbacks to reset encoders
def encoder_1_sw_callback():
    global enc1
    enc1 = 1

def encoder_2_sw_callback():
    global enc2
    enc2 = 0

# Incrementer callbacks for encoders
def encoder_1_inc(scale_position):
    global enc1
    enc1 += 1

def encoder_2_inc(scale_position):
    global enc2
    enc2 += 1

# Decrement callbacks for encoders
def encoder_1_dec(scale_position):
    global enc1
    enc1 -= 1

def encoder_2_dec(scale_position):
    global enc2
    enc2 -= 1

# Set up encoder 1
encoder_1 = pyky040.Encoder(CLK=CLK_ONE, DT=DT_ONE, SW=SW_ONE)
encoder_1.setup(scale_min=0, scale_max=128, step=1, inc_callback=encoder_1_inc, dec_callback=encoder_1_dec, sw_callback=encoder_1_sw_callback)

encoder_1_thread = Thread(target=encoder_1.watch)
encoder_1_thread.start()

# Set up encoder 2
# encoder_2 = pyky040.Encoder(CLK=CLK_TWO, DT=DT_TWO, SW=SW_TWO)
# encoder_2.setup(scale_min=0, scale_max=100, step=1, inc_callback=encoder_2_inc, dec_callback=encoder_2_dec, sw_callback=encoder_2_sw_callback)

# encoder_2_thread = Thread(target=encoder_2.watch)
# encoder_2_thread.start()

# Get readings from MCP3008 channels
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
    sleep1        = pot_6.value

    # Rotary encoder driven controls
    note1 = enc1
    note2 = note1 + 3
    note3 = note2 + 4

    if note1 < 1:
        note1 = 1

    use_synth(SAW)
    play(note1, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
    sleep(0.5)
    play(note2, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
    sleep(1)
    play(note3, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=proper_round(sustain_level, 1), sustain=int(proper_round(sustain)), release=proper_round(release, 1))
