"""
Test step to set the voltage on a PV1-3 pin
"""

from OpenTap import Display, Unit, Verdict
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

        self.Rules.Add(
            Rule("Voltage", lambda: self.Voltage >= self.get_min_voltage(),
                 lambda: f'Voltage must be at least {self.get_min_voltage()} V for {self.Pin}.'))
        self.Rules.Add(
            Rule("Voltage", lambda: self.Voltage <= self.get_max_voltage(),
                 lambda: f'Voltage must not exceed {self.get_max_voltage()} V for {self.Pin}.'))

    def Run(self):
        self.PowerSupply.setVoltage(self.Pin, self.Voltage)
        self.UpgradeVerdict(Verdict.Pass)

    def get_min_voltage(self):
        """Gets minimal voltage for current pin."""
        match self.Pin:
            case PowerPin.ONE:
                return -5
            case PowerPin.TWO:
                return -3.3
            case PowerPin.THREE:
                return 0
            case _:
                raise Exception(f"Unsupported pin: {self.Pin}")

    def get_max_voltage(self):
        """Gets maximum voltage for current pin."""
        match self.Pin:
            case PowerPin.ONE:
                return 5
            case PowerPin.TWO | PowerPin.THREE:
                return 3.3
            case _:
                raise Exception(f"Unsupported pin: {self.Pin}")
