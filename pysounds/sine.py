import pyaudio
import numpy as np
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

volume_prev     = None
duration_prev   = None
f_prev          = None

# p = pyaudio.PyAudio()

fs = 48000 # sampling rate, Hz, must be integer

while True:
    sine_freq_multiplier    = pot_4.value
    volume   = proper_round(pot_1.value)          # range [0.0, 1.0]
    duration = proper_round(pot_2.value * 10)     # in seconds, may be float
    f        = proper_round(pot_3.value * (sine_freq_multiplier * 10), 1) # sine frequency, Hz, may be float
    print(volume, duration, f, sine_freq_multiplier)
    if volume != volume_prev or duration != duration_prev or f != f_prev:
        p = pyaudio.PyAudio()
        # generate samples, note conversion to float32 array
        # samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
        samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32).tobytes()

        # for paFloat32 sample values must be in range [-1.0, 1.0]
        stream = p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=fs,
                        output=True)

        # play. May repeat with different volume values (if done interactively) 
        # stream.write(volume*samples)
        stream.write(samples)

        stream.stop_stream()
        stream.close()

        p.terminate()

        volume_prev     = volume
        duration_prev   = duration
        f_prev          = f
        sine_freq_multiplier_prev      = sine_freq_multiplier
        # sleep(sine_freq_multiplier)
