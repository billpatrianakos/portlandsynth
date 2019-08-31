# Portland Synth

> Control Sonic Pi using Python and some potentiometers connected to a Raspberry Pi

These are a collection of Sonic Pi loops and Python scripts that work together to generate music either with Python alone or Sonic Pi on a headless Raspberry Pi. You'll need a set of 10k potentiometers (8 is great, 4 is enough), a MCP3008 ADC chip, a mini solderless breadboard, some jumper wires, and any Raspberry Pi with populated GPIO pins (I'm using a Pi Zero W but Sonic Pi is not officially supported on it so beware).

The idea is that you can generate music one of two ways:

1. Play Sonic Pi music through Python scripts and manipulate the sound in real time with the values read from some potentiometers.
2. Run a Python script that generates a waveform and play it through `aplay`

## Wiring it up

I had limited materials to work with. You can wire it up however you like but this is how it is currently working with 8 potentiometers and 2 rotary encoders.

![Breadboard Image](https://github.com/billpatrianakos/portlandsynth/raw/master/docs/portland_synth_bb.png)

TODO: In depth explanation of wiring and which GPIO controls what part.

## Installation

1. Install Sonic Pi however you want. Use the package manager or build from source. Doesn't matter. *If you are running a headless Pi* then be sure to install `xvfb` otherwise Sonic Pi won't start.
2. Copy this entire project to your Pi
3. Install the dependencies with `pip install -r requirements.txt` (Only Python 3 is supported. Python 2.7 may or may not work with these scripts)

## Usage

### To start Sonic Pi on a headless Raspberry Pi

Run the script in the system folder: `./sonic-pi-headless.sh`

### To play some music

Just run any of the Python music files like `python3 pysounds/sine.py` or `python3 sonic_python/track2.py`

*Remember:* If you don't have at least 4 potentiometers connected to your Pi then there will be no signals to read and the scripts will probably crash.


TODO:

- how to run sonic pi headless
- what to do if you run on a pi zero with no audio out
- python OSC to sonic pi explanation
- pure python instructions

## Why is it called "Portland Synth"?

Because I've been naming my Raspberry Pi's after places and landmarks in the Pacific Northwest recently and I built this project on my Pi Zero W with the hostname `portland`.
