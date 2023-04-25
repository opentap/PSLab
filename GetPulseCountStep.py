from OpenTap import Display, Output, Verdict
from System import Int32
from opentap import *

from .LogicAnalyzer import *


@attribute(
    Display("Get Pulse Count", "Publishes the amount of pulses counted since calling count_pulses",
            Groups=["PSLab", "Logic Analyzer"]))
class GetPulseCountStep(TestStep):
    # Properties
    LogicAnalyzer = property(LogicAnalyzer, None) \
        .add_attribute(Display("Logic Analyzer", "", "Resources", 0))

    OutputValue = property(Int32, 0) \
        .add_attribute(Display("Pulse Count ", "Counted pulses", "Output", 99)) \
        .add_attribute(Output())

    def __init__(self):
        super(GetPulseCountStep, self).__init__()

    def Run(self):
        super().Run()  # 3.0: Required for debugging to work.

        pulsecount = self.LogicAnalyzer.fetch_pulse_count()

        self.OutputValue = pulsecount
        self.log.Debug(f"Pulses: {pulsecount}")
        self.PublishResult("Pulse Count", ["Pulse count"], [pulsecount])
        self.UpgradeVerdict(Verdict.Pass)
