"""
Test step to generate a sine waveform
"""
from OpenTap import Display, Unit, Verdict
from System import Double
from opentap import *

from .WaveformGenerator import *


@attribute(
    Display("Generate Sine Wave", "Generates a Sine Wave of given frequency and phase on given pin",
            Groups=["PSLab", "Waveform Generator"]))
class GenerateSineWave(TestStep):
    # Properties
    Pin = property(SineWavePin, SineWavePin.SI1) \
        .add_attribute(Display("Pin", "Pin on which the sine wave is generated", "", -50))

    Phase = property(Double, 0) \
        .add_attribute(Display("Phase", "The phase of the sine wave", "", -40)) \
        .add_attribute(Unit("°"))  # this is used for the unit of measurement

    Frequency = property(Double, 500) \
        .add_attribute(Display("Frequency", "The frequency of the sine wave", "", -30)) \
        .add_attribute(Unit("Hz"))

    WaveformGenerator = property(WaveformGenerator, None) \
        .add_attribute(Display("Waveform Generator", "", "Resources", 0))

    def __init__(self):
        super(GenerateSineWave, self).__init__()

        self.Rules.Add(
            Rule("Frequency", lambda: self.Frequency >= 0.1, lambda: 'Frequency must be at least 0.1 Hz.'))
        self.Rules.Add(
            Rule("Frequency", lambda: self.Frequency < 4000000, lambda: 'Frequency must be lower than 4000000 Hz.'))

    def Run(self):
        super().Run()  # 3.0: Required for debugging to work.

        self.WaveformGenerator.generate_sine(self.Pin, self.Frequency, self.Phase)
        self.UpgradeVerdict(Verdict.Pass)
