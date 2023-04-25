from OpenTap import AvailableValues, Display, Output, Unit, Verdict
from System import Double, String
from System.Collections.Generic import List
from opentap import *

from .LogicAnalyzer import *


@attribute(
    Display("Measure Interval", "Measures time between two events on digital channels (in µs)",
            Groups=["PSLab", "Logic Analyzer"]))
class MeasureIntervalStep(TestStep):
    # Properties
    channel1 = property(DigitalPin, DigitalPin.LA1) \
        .add_attribute(Display("Channel #1", "Name of digital channel to listen for first event on",
                               "Measurements", -50))

    channel2 = property(DigitalPin, DigitalPin.LA1) \
        .add_attribute(Display("Channel #2", "Name of digital channel to listen for second event on",
                               "Measurements", -40))

    mode1 = property(String, "any") \
        .add_attribute(Display("Mode #1", "Type of logic event to listen for on channel #1",
                               "Measurements", -30)) \
        .add_attribute(AvailableValues("Modes"))

    mode2 = property(String, "any") \
        .add_attribute(Display("Mode #2", "Type of logic event to listen for on channel #2",
                               "Measurements", -20)) \
        .add_attribute(AvailableValues("Modes"))

    LogicAnalyzer = property(LogicAnalyzer, None) \
        .add_attribute(Display("Logic Analyzer", "", "Resources", 0))

    @property(List[String])
    @attribute(Browsable(False))  # property not visible for the user.
    def Modes(self):
        modes = List[String]()
        modes.Add("sixteen rising")
        modes.Add("four rising")
        modes.Add("rising")
        modes.Add("falling")
        modes.Add("any")
        modes.Add("disabled")
        return modes

    timeout = property(Double, 1) \
        .add_attribute(Display("Timeout", "Timeout before cancelling measurement", "Measurements", -10)) \
        .add_attribute(Unit("s"))

    OutputValue = property(Double, 0.0) \
        .add_attribute(Display("Interval ", "Measured interval", "Output", 99)) \
        .add_attribute(Unit("µs")) \
        .add_attribute(Output())

    def __init__(self):
        super(MeasureIntervalStep, self).__init__()

    def Run(self):
        super().Run()  # 3.0: Required for debugging to work.

        interval = self.LogicAnalyzer.measure_interval(
            [self.channel1, self.channel2],
            [self.mode1, self.mode2], self.timeout)

        self.OutputValue = interval
        self.log.Debug(f"Interval: {interval} µs")
        self.PublishResult("Measured Interval", ["Interval (µs)"], [interval])
        self.UpgradeVerdict(Verdict.Pass)
