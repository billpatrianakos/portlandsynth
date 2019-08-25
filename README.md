# Portland Synth

> Control Sonic Pi using Python, OSC, and some potentiometers connected to a Raspberry Pi

These are a collection of Sonic Pi loops and Python scripts that work together to generate music either with Python alone or Sonic Pi on a headless Raspberry Pi. You'll need a set of 10k potentiometers, a MCP3008 ADC chip, a mini solderless breadboard, some jumper wires, and any Raspberry Pi with populated GPIO pins (I'm using a Pi Zero W but Sonic Pi is not officially supported on it so beware).

The idea is that you can generate music one of two ways:

1. Run Sonic Pi and send OSC commands to it using a Python script that reads the values of your potentiometers.
2. Run a Python script that generates a waveform and play it through `aplay`

Details on how to wire up the Pi and fit it into an enclosure coming soon.

## Usage

Note: So far only the pysounds folder has anything that actually consistently produces sound in it.

TODO:

- how to run sonic pi headless
- what to do if you run on a pi zero with no audio out
- python OSC to sonic pi explanation
- pure python instructions

## Why is it called "Portland Synth"?

Because I've been naming my Raspberry Pi's after places and landmarks in the Pacific Northwest recently and I built this project on my Pi Zero W with the hostname `portland`.
