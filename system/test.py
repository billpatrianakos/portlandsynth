from gpiozero import MCP3008
from time import sleep
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
enc1 = 0
enc2 = 0


def proper_round(num, dec=0):
    num = str(num)[:str(num).index('.')+dec+2]
    if num[-1]>='5':
        return float(num[:-2-(not dec)]+str(int(num[-2-(not dec)])+1))
    return float(num[:-1])


# Callbacks to increment encoder
def encoder_1_callback(scale_position):
    global enc1
    enc1 = scale_position

def encoder_2_callback(scale_position):
    global enc2
    enc2 = scale_position


# Callbacks to reset encoders
def encoder_1_sw_callback():
    global enc1
    enc1 = 0

def encoder_2_sw_callback():
    global enc2
    enc2 = 0

# Set up encoder 1
encoder_1 = pyky040.Encoder(CLK=CLK_ONE, DT=DT_ONE, SW=SW_ONE)
encoder_1.setup(scale_min=0, scale_max=128, step=1, chg_callback=encoder_1_callback, sw_callback=encoder_1_sw_callback)

encoder_1_thread = Thread(target=encoder_1.watch)
encoder_1_thread.start()

# Set up encoder 2
encoder_2 = pyky040.Encoder(CLK=CLK_TWO, DT=DT_TWO, SW=SW_TWO)
encoder_2.setup(scale_min=0, scale_max=100, step=1, chg_callback=encoder_2_callback, sw_callback=encoder_2_sw_callback)

encoder_2_thread = Thread(target=encoder_2.watch)
encoder_2_thread.start()


pot_1 = MCP3008(channel=0)
pot_2 = MCP3008(channel=1)
pot_3 = MCP3008(channel=2)
pot_4 = MCP3008(channel=3)
pot_5 = MCP3008(channel=4)
pot_6 = MCP3008(channel=5)
pot_7 = MCP3008(channel=6)
pot_8 = MCP3008(channel=7)


while True:
    print(proper_round(pot_1.value, 2), proper_round(pot_2.value, 2), proper_round(pot_3.value, 2), proper_round(pot_4.value, 2), proper_round(pot_5.value, 2), proper_round(pot_6.value, 2), proper_round(pot_7.value, 2), proper_round(pot_8.value, 2), enc1, enc2)
    sleep(0.5)
