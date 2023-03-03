from OpenTap import Display
from opentap import *

from .ConnectionHandler import ConnectionHandler


@attribute(Display("Multimeter", "Multimeter Instrument", "PSLab"))
class Multimeter(Instrument):
    def __init__(self):
        """Set up the properties, methods and default values of the instrument."""
        super(Multimeter, self).__init__()  # The base class initializer must be invoked.
        self.instrument = None
        self.Name = "Multimeter"

    def Open(self):
        super(Multimeter, self).Open()
        # Open COM connection to instrument using ConnectionHandler
        self.instrument = ConnectionHandler.instance().getMultimeter()
        """Called by TAP when the test plan starts"""

    def Close(self):
        """Called by TAP when the test plan ends."""
        super(Multimeter, self).Close()

    def measure_resistance(self):
        """Measure the resistance of a resistor connected between RES and GND."""
        return self.instrument.measure_resistance()

    def measure_voltage(self, channel="VOL"):
        """Measure the voltage on the selected channel."""
        return self.instrument.measure_voltage(channel)

    def calibrate_capacitance(self):
        """Calibrate stray capacitance."""
        return self.instrument.calibrate_capacitance()

    def measure_capacitance(self):
        """Measure the capacitance of a capacitor connected between CAP and GND."""
        return self.instrument.measure_capacitance()
