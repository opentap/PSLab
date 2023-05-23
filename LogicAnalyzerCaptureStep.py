from OpenTap import AvailableValues, Display, EnabledIf, Unit
from System import Boolean, Double, Int32
from System.Collections.Generic import List
from System.ComponentModel import Browsable
from opentap import *

from .LogicAnalyzer import *


@attribute(
    Display("Capture", "Captures logic events using Logic Analyzer", Groups=["PSLab", "Logic Analyzer"]))
class LogicAnalyzerCaptureStep(TestStep):
    # Properties
    channels = property(Int32, 1) \
        .add_attribute(AvailableValues("Available")) \
        .add_attribute(Display("Channels", "Number of channels to sample from simultaneously",
                               "Measurements", -50))

    @property(List[Int32])
    @attribute(Browsable(False))  # property not visible for the user.
    def Available(self):
        available = List[Int32]()
        available.Add(1)
        available.Add(2)
        available.Add(3)
        available.Add(4)
        return available

    events = property(Int32, 2500) \
        .add_attribute(
        Display("Events", "Number of logic events to capture on each channel", "Measurements", -40))

    block = property(Boolean, True) \
        .add_attribute(Display("Block", "Whether to block while waiting for events to be captured",
                               "Measurements", -30))

    timeout = property(Double, 1) \
        .add_attribute(Display("Timeout", "Timeout before cancelling measurement in blocking mode",
                               "Measurements", -20)) \
        .add_attribute(Unit("s")) \
        .add_attribute(EnabledIf("block"))

    LogicAnalyzer = property(LogicAnalyzer, None) \
        .add_attribute(Display("Logic Analyzer", "", "Resources", 0))

    def __init__(self):
        super(LogicAnalyzerCaptureStep, self).__init__()

    def Run(self):
        super().Run()  # 3.0: Required for debugging to work.

        data = self.LogicAnalyzer.capture(self.channels, events=self.events, timeout=self.timeout, block=self.block)
        print(data)
