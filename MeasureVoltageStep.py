from OpenTap import AvailableValues, Display, Output, Unit, Verdict
from System import Double, String
from System.Collections.Generic import List
from System.ComponentModel import Browsable
from opentap import *

from .Multimeter import *


@attribute(
    Display("Measure Voltage", "Measures voltage between pin an GND (in V)", Groups=["PSLab", "Multimeter"]))
class MeasureVoltageStep(TestStep):
    # Properties
    Channel = property(String, "VOL") \
        .add_attribute(AvailableValues("Available")) \
        .add_attribute(Display("Channel", "Channel to measure voltage from", "Measurements", -50))

    Multimeter = property(Multimeter, None) \
        .add_attribute(Display("Multimeter", "", "Resources", 0))

    OutputValue = property(Double, 0.0) \
        .add_attribute(Display("Current ", "Measured voltage", "Output", 99)) \
        .add_attribute(Unit("V")) \
        .add_attribute(Output())

    @property(List[String])
    @attribute(Browsable(False))  # property not visible for the user.
    def Available(self):
        available = List[String]()
        available.Add("CH1")
        available.Add("CH2")
        available.Add("CH3")
        available.Add("MIC")
        available.Add("CAP")
        available.Add("RES")
        available.Add("VOL")
        return available

    def __init__(self):
        super(MeasureVoltageStep, self).__init__()

    def Run(self):
        super().Run()  # 3.0: Required for debugging to work.

        voltage = float(self.Multimeter.measure_voltage(self.Channel))

        self.OutputValue = voltage
        self.log.Debug(f"Voltage: {voltage} V")
        self.PublishResult("Multimeter", ["Voltage (V)"], [voltage])
        self.UpgradeVerdict(Verdict.Pass)
