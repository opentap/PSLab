"""
Test step to generate a square waveform
"""
from OpenTap import Display, Unit, Verdict
from System import Double
from opentap import *

from .WaveformGenerator import *


@attribute(Display("Generate Square Wave",
                   "Generates a Square Wave of given frequency, duty cycle, and phase on given pin",
                   Groups=["PSLab", "Waveform Generator"]))
class GenerateSquareWave(TestStep):
    # Properties
    Pin = property(SquareWavePin, SquareWavePin.SQ1) \
        .add_attribute(Display("Pin", "Pin on which the square wave is generated", "", -50))

    Frequency = property(Double, 1000) \
        .add_attribute(Display("Frequency", "The frequency of the square wave", "", -40)) \
        .add_attribute(Unit("Hz"))

    Phases = property(Double, 0) \
        .add_attribute(Display("Phase", "The phase of the square wave", "", -30)) \
        .add_attribute(Unit("°"))  # this is used for the unit of measurement

    Duty_Cycles = property(Double, 0.7) \
        .add_attribute(Display("Duty Cycles", "The duty cycle of the square wave", "", -20))

    WaveformGenerator = property(WaveformGenerator, None) \
        .add_attribute(Display("Waveform Generator", "", "Resources", 0))

    def __init__(self):
        super(GenerateSquareWave, self).__init__()

    def Run(self):
        super().Run()  # 3.0: Required for debugging to work.

        self.WaveformGenerator.generate_square(self.Pin, self.Frequency, self.Duty_Cycles, self.Phases)
        self.UpgradeVerdict(Verdict.Pass)
