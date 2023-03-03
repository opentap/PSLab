from OpenTap import Display
from opentap import *

from .LogicAnalyzer import *


@attribute(
    Display("Get Pulse Count", "Publishes the amount of pulses counted since calling count_pulses",
            Groups=["PSLab", "Logic Analyzer"]))
class GetPulseCountStep(TestStep):
    # Properties
    LogicAnalyzer = property(LogicAnalyzer, None) \
        .add_attribute(Display("Logic Analyzer", "", "Resources", 0))

    def __init__(self):
        super(GetPulseCountStep, self).__init__()

    def Run(self):
        super().Run()  # 3.0: Required for debugging to work.

        pulsecount = self.LogicAnalyzer.fetch_pulse_count()
        self.PublishResult("Pulse Count", ["Pulse count"], [pulsecount])
