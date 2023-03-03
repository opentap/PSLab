"""
Test step to get the voltage on a PV1-3 pin
"""
from OpenTap import Display
from opentap import *

from .PowerSupply import *


@attribute(Display("Get Voltage", "Gets voltage of pin (in V)", Groups=["PSLab", "Power Supply"]))
class GetVoltageStep(TestStep):
    # Properties
    Pin = property(PowerPin, PowerPin.ONE) \
        .add_attribute(Display("Pin", "The chosen PV pin", "", -50))

    PowerSupply = property(PowerSupply, None) \
        .add_attribute(Display("Power Supply", "", "Resources", 0))

    def __init__(self):
        super(GetVoltageStep, self).__init__()

    def Run(self):
        super().Run()  # 3.0: Required for debugging to work.

        voltage = float(self.PowerSupply.getVoltage(self.Pin))
        self.PublishResult("PowerSupply", ["Voltage (V)"], [voltage])
