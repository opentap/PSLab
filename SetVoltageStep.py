"""
Test step to set the voltage on a PV1-3 pin
"""

from OpenTap import Display, Unit
from System import Double
from opentap import *

from .PowerSupply import *


@attribute(Display("Set Voltage", "Sets pin to a specific voltage", Groups=["PSLab", "Power Supply"]))
class SetVoltageStep(TestStep):
    # Properties
    Pin = property(PowerPin, PowerPin.ONE) \
        .add_attribute(Display("Pin", "The chosen PV pin", "", -50))

    Voltage = property(Double, 0) \
        .add_attribute(Display("Voltage", "The voltage to be output on the chosen PV pin", "", -40)) \
        .add_attribute(Unit("V"))

    PowerSupply = property(PowerSupply, None) \
        .add_attribute(Display("Power Supply", "", "Resources", 0))

    def __init__(self):
        super(SetVoltageStep, self).__init__()

    def Run(self):
        self.PowerSupply.setVoltage(self.Pin, self.Voltage)
