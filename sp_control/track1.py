from gpiozero import MCP3008
from pythonosc import osc_message_builder
from pythonosc import udp_client

sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)

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
    if pot_1 != pot_1_prev or pot_2 != pot_2_prev or pot_3 != pot_3_prev or pot_4 != pot_4_prev or pot_5 != pot_5_prev:
        sender.send_message('/trigger/prophet', [pot_1, pot_2, pot_3])
        pot_1_prev = pot_1
        pot_2_prev = pot_2
        pot_3_prev = pot_3
        pot_4_prev = pot_4
        pot_5_prev = pot_5
