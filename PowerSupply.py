"""
Instrument wrapper for PSLab python API
"""
from enum import Enum

from OpenTap import Display
from opentap import *

from .ConnectionHandler import ConnectionHandler


class PowerPin(Enum):
    ONE = 0
    TWO = 1
    THREE = 2


@attribute(Display("Power Supply", "Power supply instrument", "PSLab"))
class PowerSupply(Instrument):
    def __init__(self):
        """Set up the properties, methods and default values of the instrument."""
        super(PowerSupply, self).__init__()  # The base class initializer must be invoked.

        self.instrument = None
        self.Name = "Power Supply"

    def Open(self):
        super(PowerSupply, self).Open()
        # Open COM connection to instrument through ConnectionHandler
        self.instrument = ConnectionHandler.instance().getPowerSupply()
        """Called by TAP when the test plan starts."""

    def Close(self):
        """Called by TAP when the test plan ends."""
        super(PowerSupply, self).Close()

    def setPcs(self, current):
        self.instrument.pcs = current
        self.log.Info(f"PSLab Power Supply PCS Current set to {current}")

    def getPcs(self):
        current = self.instrument.pcs
        self.log.Info(f"PSLab Power Supply PCS Current is {current}")
        return current

    def setVoltage(self, pin, voltage):
        match pin:
            case PowerPin.ONE:
                self.instrument.pv1 = voltage
            case PowerPin.TWO:
                self.instrument.pv2 = voltage
            case PowerPin.THREE:
                self.instrument.pv3 = voltage
            case _:
                raise Exception(f"Bad pin number: {pin}")

        self.log.Info(f"PSLab Power Supply {pin} pin voltage set to {voltage}")

    def getVoltage(self, pin):
        match pin:
            case PowerPin.ONE:
                self.log.Info(f"PSLab Power Supply {pin} pin voltage is {self.instrument.pv1}")
                return self.instrument.pv1
            case PowerPin.TWO:
                self.log.Info(f"PSLab Power Supply {pin} pin voltage set to {self.instrument.pv2}")
                return self.instrument.pv2
            case PowerPin.THREE:
                self.log.Info(f"PSLab Power Supply {pin} pin voltage set to {self.instrument.pv3}")
                return self.instrument.pv3
            case _:
                raise Exception(f"Bad pin number: {pin}")
