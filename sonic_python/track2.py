from gpiozero import MCP3008
from time import sleep

def proper_round(num, dec=0):
    num = str(num)[:str(num).index('.')+dec+2]
    if num[-1]>='5':
        return float(num[:-2-(not dec)]+str(int(num[-2-(not dec)])+1))
    return float(num[:-1])

# Get readings from MCP3008 channels
pot_1 = MCP3008(channel=0)
pot_2 = MCP3008(channel=1)
pot_3 = MCP3008(channel=2)
pot_4 = MCP3008(channel=4)

while True:
    attack  = pot_1.value
    decay   = pot_2.value
    sustain = pot_3.value
    release = pot_4.value

    use_synth(SAW)
    play(72, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=0.4, sustain=int(proper_round(sustain)), release=proper_round(release, 1))
    sleep(1)
    play(75, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=0.4, sustain=int(proper_round(sustain)), release=proper_round(release, 1))
    sleep(1)
    play(79, attack=proper_round(attack, 1), decay=int(proper_round(decay)), sustain_level=0.4, sustain=int(proper_round(sustain)), release=proper_round(release, 1))
