# import myPyLib   # get control-C handler

import time
import math
import pyaudio
from numpy import linspace,sin,pi,int16
from gpiozero import MCP3008

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

pa = None;
s  = None;

def init_audio(rate=8000):
  global pa,s
  print "init_audio: Create PyAudio object"
  pa = pyaudio.PyAudio()
  print "init_audio: Open stream"
  s = pa.open(output=True,
            channels=1,
            rate=rate,
            format=pyaudio.paInt16,
            output_device_index=0)
  print "init_audio: audio stream initialized"

def close_audio():
  global pa,s
  print "close_audio: Closing stream"
  s.close()
  print "close_audio: Terminating PyAudio Object"
  pa.terminate()


def note(freq, len, amp=5000, rate=8000):
 t = linspace(0,len,len*rate)
 data = sin(2*pi*freq*t)*amp
 return data.astype(int16) # two byte integers

def tone(freq=440.0, tonelen=0.5, amplitude=5000, rate=8000):
  global s
  # generate sound
  tone = note(freq, tonelen, amplitude, rate)

  # play it    
  #print "tone.main(): start playing tone"
  s.write(tone)


# ##### MAIN ######
def main():
  # myPyLib.set_cntl_c_handler(close_audio)  # Set CNTL-C handler 

  # open audio channel
  init_audio()

  # play tones forever    
  print "tone.main(): start playing tones"
  while True:
    print "tone.main: tone() 440"
    tone()
    time.sleep(3)
    print "tone.main: tone(261)"
    tone(261,1)
    time.sleep(3)
    print "tone.main: tone(880)"
    tone(880)
    time.sleep(3)


if __name__ == "__main__":
    main()
