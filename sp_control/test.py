from gpiozero import MCP3008
from pythonosc import osc_message_builder
from pythonosc import udp_client

sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

def proper_round(num, dec=0):
    num = str(num)[:str(num).index('.')+dec+2]
    if num[-1]>='5':
        return float(num[:-2-(not dec)]+str(int(num[-2-(not dec)])+1))
    return float(num[:-1])


pot_1 = MCP3008(channel=0)
pot_2 = MCP3008(channel=1)
pot_3 = MCP3008(channel=2)
pot_4 = MCP3008(channel=3)
pot_5 = MCP3008(channel=4)

pot_1_prev = None
pot_2_prev = None
pot_3_prev = None
pot_4_prev = None
pot_5_prev = None

while True:
    if pot_1.value != pot_1_prev or pot_2.value != pot_2_prev or pot_3.value != pot_3_prev or pot_4.value != pot_4_prev or pot_5.value != pot_5_prev:
        volume = proper_round(pot_1.value)
        cutoff = proper_round(pot_2.value * 10)
        sustain = proper_round(pot_3.value + 0.2, 1)
        print(volume, cutoff, sustain)
    else:
        print("Values have not changed")
