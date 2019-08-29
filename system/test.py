from gpiozero import MCP3008
from time import sleep


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
pot_6 = MCP3008(channel=5)
pot_7 = MCP3008(channel=6)
pot_8 = MCP3008(channel=7)


while True:
    print(proper_round(pot_1.value, 2), proper_round(pot_2.value, 2), proper_round(pot_3.value, 2), proper_round(pot_4.value, 2), proper_round(pot_5.value, 2), proper_round(pot_6.value, 2), proper_round(pot_7.value, 2), proper_round(pot_8.value, 2))
    sleep(0.5)
