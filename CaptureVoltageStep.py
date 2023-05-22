from OpenTap import AvailableValues, Display, Unit, Verdict
from System import Double, Int32
from System.Collections.Generic import List
from System.ComponentModel import Browsable
from opentap import *

from .Oscilloscope import *


@attribute(Display("Capture Voltage", "Captures varying voltages (in V)",
                   Groups=["PSLab", "Oscilloscope"]))
class CaptureVoltageStep(TestStep):
    # Properties
    Channels = property(Int32, 1) \
        .add_attribute(
        Display("Channels", "Number of channels to sample from simultaneously", "Measurements", -50)) \
        .add_attribute(AvailableValues("Available"))

    Oscilloscope = property(Oscilloscope, None) \
        .add_attribute(Display("Oscilloscope", "", "Resources", 0))

    @property(List[Int32])
    @attribute(Browsable(False))  # property not visible for the user.
    def Available(self):
        available = List[Int32]()
        available.Add(1)
        available.Add(2)
        available.Add(3)
        available.Add(4)
        return available

    Samples = property(Int32, 200) \
        .add_attribute(Display("Samples",
                               "Number of samples to fetch, maximum is 10000 divided by number of channels",
                               "Measurements", -40))

    Timegap = property(Double, 10) \
        .add_attribute(Display("Time Gap", "Time gap between samples", "Measurements", -30)) \
        .add_attribute(Unit("ms"))

    def __init__(self):
        super(CaptureVoltageStep, self).__init__()

    def Run(self):
        super().Run()  # 3.0: Required for debugging to work.

        results = self.Oscilloscope.capture(self.Channels, self.Samples, self.Timegap)

        time = results[0].tolist()
        channel1 = results[1].tolist()
        match len(results):
            case 2:
                for i in range(0, len(time)):
                    self.PublishResult("Oscilloscope Results", ["Time", "Voltage (V)"], [time[i], channel1[i]])
            case 3:
                channel2 = results[2].tolist()
                for i in range(0, len(time)):
                    self.PublishResult("Oscilloscope Results", ["Time", "Voltage 1 (V)", "Voltage 2 (V)"],
                                       [time[i], channel1[i], channel2[i]])
            case 4:
                channel2 = results[2].tolist()
                channel3 = results[3].tolist()
                for i in range(0, len(time)):
                    self.PublishResult("Oscilloscope Results",
                                       ["Time", "Voltage 1 (V)", "Voltage 2 (V)", "Voltage 3 (V)"],
                                       [time[i], channel1[i], channel2[i], channel3[i]])
            case 5:
                channel2 = results[2].tolist()
                channel3 = results[3].tolist()
                channel4 = results[4].tolist()
                for i in range(0, len(time)):
                    self.PublishResult("Oscilloscope Results",
                                       ["Time", "Voltage 1 (V)", "Voltage 2 (V)", "Voltage 3 (V)", "Voltage 4 (V)"],
                                       [time[i], channel1[i], channel2[i], channel3[i], channel4[i]])
            case _:
                raise Exception(f"Unexpected number of results: {len(results)}")

        self.UpgradeVerdict(Verdict.Pass)
