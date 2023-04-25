from OpenTap import AvailableValues, Display, EnabledIf, Output, Unit, Verdict
from System import Boolean, Double, String, Int32
from System.Collections.Generic import List
from opentap import *

from .LogicAnalyzer import *


@attribute(
    Display("Count pulses", "Count pulses on a digital channel", Groups=["PSLab", "Logic Analyzer"]))
class CountPulsesStep(TestStep):
    # Properties
    channel = property(String, "FRQ") \
        .add_attribute(Display("Channel", "Channel to count pulses on", "Measurements", -50)) \
        .add_attribute(AvailableValues("Available"))

    @property(List[String])
    @attribute(Browsable(False))  # property not visible for the user.
    def Available(self):
        available = List[String]()
        available.Add("LA1")
        available.Add("LA2")
        available.Add("LA3")
        available.Add("LA4")
        available.Add("FRQ")
        return available

    block = property(Boolean, True) \
        .add_attribute(
        Display("Block", "Whether to block while waiting for pulses to be captured", "Measurements", -30))

    interval = property(Double, 1) \
        .add_attribute(Display("Interval", "Time during which to count pulses", "Measurements", -40)) \
        .add_attribute(Unit("s")) \
        .add_attribute(EnabledIf("block"))

    LogicAnalyzer = property(LogicAnalyzer, None) \
        .add_attribute(Display("Logic Analyzer", "", "Resources", 0))

    OutputValue = property(Int32, 0) \
        .add_attribute(Display("Pulse Count ", "Counted pulses", "Output", 99)) \
        .add_attribute(EnabledIf("block")) \
        .add_attribute(Output())

    def __init__(self):
        super(CountPulsesStep, self).__init__()

    def Run(self):
        super().Run()  # 3.0: Required for debugging to work.

        pulsecount = self.LogicAnalyzer.count_pulses(self.channel, interval=self.interval, block=self.block)

        if self.block:
            self.OutputValue = pulsecount
            self.log.Debug(f"Pulses: {pulsecount}")
        else:
            self.log.Debug("Counting pulses asynchronously, get pulse count via Get Pulse Count Step.")

        self.PublishResult("Pulse Count", ["Pulse count"], [pulsecount])
        self.UpgradeVerdict(Verdict.Pass)
