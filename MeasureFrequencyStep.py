from OpenTap import Display, Unit
from System import Boolean, Double
from opentap import *

from .LogicAnalyzer import *


@attribute(
    Display("Measure Frequency", "Measures frequency on a digital pin (in Hz)",
            Groups=["PSLab", "Logic Analyzer"]))
class MeasureFrequencyStep(TestStep):
    # Properties
    channel = property(DigitalPin, DigitalPin.LA1) \
        .add_attribute(
        Display("Channel", "Name of digital channel to measure frequency on", "Measurements", - 50))

    simultaneous_oscilloscope = property(Boolean, False) \
        .add_attribute(
        Display("Simultaneously Using Oscilloscope", "Set to true if using oscilloscope at the same time",
                "Measurements", -40))

    timeout = property(Double, 1) \
        .add_attribute(Display("Timeout", "Timeout before cancelling measurement", "Measurements", -30)) \
        .add_attribute(Unit("s"))

    LogicAnalyzer = property(LogicAnalyzer, None) \
        .add_attribute(Display("Logic Analyzer", "", "Resources", 0))

    def __init__(self):
        super(MeasureFrequencyStep, self).__init__()

    def Run(self):
        super().Run()  # 3.0: Required for debugging to work.

        frequency = self.LogicAnalyzer.measure_frequency(self.channel, self.simultaneous_oscilloscope, self.timeout)
        self.PublishResult("Measured Frequency", ["Frequency (Hz)"], [frequency])
