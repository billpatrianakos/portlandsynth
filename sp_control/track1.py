from gpiozero import MCP3008
from pythonosc import osc_message_builder
from pythonosc import udp_client
from time import sleep

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

volume_prev  = None
cutoff_prev  = None
sustain_prev = None
pause_prev   = None

while True:
    volume  = proper_round(pot_1.value)
    cutoff  = proper_round(pot_2.value * 10)
    sustain = proper_round(pot_3.value + 0.2, 1)
    pause   = pot_4.value
    if volume != volume_prev or cutoff != cutoff_prev or sustain != sustain_prev:
        sender.send_message('/trigger/prophet', [volume, cutoff, sustain])
        volume_prev  = volume
        cutoff_prev  = cutoff
        sustain_prev = sustain
        pause_prev   = pause
        sleep(pause)
    else:
        print("No changes. Turn some knobs.")
