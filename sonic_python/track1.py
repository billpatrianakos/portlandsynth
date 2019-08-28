from gpiozero import MCP3008
from time import sleep
import random
from psonic import *
from threading import Thread


def proper_round(num, dec=0):
    num = str(num)[:str(num).index('.')+dec+2]
    if num[-1]>='5':
        return float(num[:-2-(not dec)]+str(int(num[-2-(not dec)])+1))
    return float(num[:-1])


pot_1 = MCP3008(channel=0)
pot_2 = MCP3008(channel=1)
pot_3 = MCP3008(channel=2)
pot_4 = MCP3008(channel=4)

def dsaw():
    c = chord(E3, MAJOR7)
    while True:
        attack = proper_round(pot_1.value, 2)
        decay  = proper_round(pot_2.value, 1)
        cutoff = int(proper_round((pot_3.value + 1) * 10))
        sustain = proper_round(pot_4.value, 1)
        use_synth(DSAW)
        play(random.choice(c), release=0.6, attack=attack, decay=decay, cutoff=cutoff, sustain=sustain)
        sleep(0.5)


def snare():
    while True:
        sample(ELEC_SNARE)
        sleep(1)

dsaw_thread = Thread(target=dsaw)
snare_thread = Thread(target=snare)

dsaw_thread.start()
snare_thread.start()

while True:
    pass
