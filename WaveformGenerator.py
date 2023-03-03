"""
Instrument wrapper for PSLab python API
"""

from enum import Enum

from OpenTap import Display
from opentap import *

from .ConnectionHandler import ConnectionHandler

SineWavePin = Enum('SineWavePin', ['SI1', 'SI2'])

SquareWavePin = Enum('SquareWavePin', ['SQ1', 'SQ2', 'SQ3', 'SQ4'])

@attribute(Display("Waveform Generator", "Waveform Generator Instrument", "PSLab"))
class WaveformGenerator(Instrument):
    def __init__(self):
        """Set up the properties, methods, and default values of the instrument."""
        super(WaveformGenerator, self).__init__()

        self.square = None
        self.sine = None
        self.Name = "Waveform Generator"

    def Open(self):
        """Called by TAP when the test plans starts."""
        super(WaveformGenerator, self).Open()
        self.sine = ConnectionHandler.instance().getWaveformGenerator()
        self.square = ConnectionHandler.instance().getPWMGenerator()

    def Close(self):
        """Called by TAP when the test plans ends."""
        super(WaveformGenerator, self).Close()

    def generate_sine(self, channel: SineWavePin, frequency, phase=0):
        """Generates a waveform with the given parameters via pslab python api call"""
        self.sine.generate(channel.name, frequency, phase)

    def generate_square(self, channel: SquareWavePin, frequency, duty_cycle, phase=0):
        """Generate PWM signals on SQ1, SQ2, SQ3, or SQ4."""
        self.square.generate(channel.name, frequency, duty_cycle, phase)
