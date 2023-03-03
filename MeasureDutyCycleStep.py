from OpenTap import Display, Unit
from System import Double
from opentap import *

from .LogicAnalyzer import *


@attribute(
    Display("Measure Duty Cycle", "Measures the duty cycle and period (in ms)",
            Groups=["PSLab", "Logic Analyzer"]))
class MeasureDutyCycleStep(TestStep):
    # Properties
    channel = property(DigitalPin, DigitalPin.LA1) \
        .add_attribute(Display("Channel", "Name of digital channel to listen on", "Measurements", -50))

    timeout = property(Double, 1) \
        .add_attribute(Display("Timeout", "Timeout before cancelling measurement", "Measurements", -40)) \
        .add_attribute(Unit("s"))

    LogicAnalyzer = property(LogicAnalyzer, None) \
        .add_attribute(Display("Logic Analyzer", "", "Resources", 0))

    def __init__(self):
        super(MeasureDutyCycleStep, self).__init__()

    def Run(self):
        super().Run()  # 3.0: Required for debugging to work.

        period, duty_cycle = self.LogicAnalyzer.measure_duty_cycle(self.channel, self.timeout)
        self.PublishResult("Measured Duty Cycle", ["Period (ms)", "Duty Cycle"], [period, duty_cycle])
