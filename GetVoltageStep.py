"""
Test step to get the voltage on a PV1-3 pin
"""
from OpenTap import Display, Output, Unit, Verdict
from System import Double
from opentap import *

from .PowerSupply import *


@attribute(Display("Get Voltage", "Gets voltage of pin (in V)", Groups=["PSLab", "Power Supply"]))
class GetVoltageStep(TestStep):
    # Properties
    Pin = property(PowerPin, PowerPin.ONE) \
        .add_attribute(Display("Pin", "The chosen PV pin", "", -50))

    PowerSupply = property(PowerSupply, None) \
        .add_attribute(Display("Power Supply", "", "Resources", 0))

    OutputValue = property(Double, 0.0) \
        .add_attribute(Display("Current ", "Read voltage", "Output", 99)) \
        .add_attribute(Unit("V")) \
        .add_attribute(Output())

    def __init__(self):
        super(GetVoltageStep, self).__init__()

    def Run(self):
        super().Run()  # 3.0: Required for debugging to work.

        voltage = float(self.PowerSupply.getVoltage(self.Pin))

        self.OutputValue = voltage
        self.log.Debug(f"Voltage: {voltage} V")
        self.PublishResult("PowerSupply", ["Voltage (V)"], [voltage])
        self.UpgradeVerdict(Verdict.Pass)
