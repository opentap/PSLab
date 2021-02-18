"""
Instrument wrapper for PSLab python API
"""

from System import Double

from PythonTap import *
from OpenTap import DisplayAttribute

from pslab import PowerSupply as PSLabPowerSupply

from .PSLabInstrument import PSLabInstrument

class Pin(Enum):
    ONE = 0
    TWO = 1
    THREE = 2

@Attribute(DisplayAttribute, "Power Supply", "Power supply instrument", "PSLab")
class PowerSupply(PSLabInstrument):
    def __init__(self):
        "Set up the properties, methods and default values of the instrument."
        super(PowerSupply, self).__init__() # The base class initializer must be invoked.

        self.Name = "PowerSupply"
        self.RegisterMethod("pcs", None).AddArgument("current", Double)

    def Open(self):
        super(PowerSupply, self).Open()
        # Open COM connection to instrument, blocks other instrument connections while connected
        self.instrument = PSLabPowerSupply()
        """Called by TAP when the test plan starts."""
        self.Info("PSLab Power Supply Opened")

    def Close(self):
        """Called by TAP when the test plan ends."""
        self.Info("PSLab Power Supply Closed")
        super(PowerSupply, self).Close()

    def setPcs(self, current):
        self.instrument.pcs = current
        self.Info(f"PSLab Power Supply PCS Current set to {current}")

    def getPcs(self):
        current = self.instrument.pcs
        self.Info(f"PSLab Power Supply PCS Current is {current}")
        return current

    def setVoltage(self, pin, voltage):
        if pin is Pin.ONE:
            self.instrument.pv1 = voltage
        elif pin is Pin.TWO:
            self.instrument.pv2 = voltage
        elif pin is Pin.THREE:
            self.instrument.pv3 = voltage
        else:
            error("Bad pin number")
            return
        self.Info(f"PSLab Power Supply {pin} pin voltage set to {voltage}")

    def getVoltage(self, pin):
        if pin is Pin.ONE:
            self.Info(f"PSLab Power Supply {pin} pin voltage is {self.instrument.pv1}")
            return self.instrument.pv1
        elif pin is Pin.TWO:
            self.Info(f"PSLab Power Supply {pin} pin voltage set to {self.instrument.pv2}")
            return self.instrument.pv2
        elif pin is Pin.THREE:
            self.Info(f"PSLab Power Supply {pin} pin voltage set to {self.instrument.pv3}")
            return self.instrument.pv3
        else:
            error("Bad pin number")
            return
