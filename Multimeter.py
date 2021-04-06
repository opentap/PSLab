from PythonTap import *
from OpenTap import DisplayAttribute

from .PSLabInstrument import PSLabInstrument
from .ConnectionHandler import ConnectionHandler

@Attribute(DisplayAttribute, "Multimeter", "Multimeter Instrument", "PSLab")
class Multimeter(PSLabInstrument):
    def __init__(self):
        """Set up the properties, methods and default values of the instrument."""
        super(Multimeter, self).__init__() # The base class initializer must be invoked.
        self.Name = "Multimeter"

    def Open(self):
        super(Multimeter, self).Open()
        # Open COM connection to instrument using ConnectionHandler
        self.instrument = ConnectionHandler.instance().getMultimeter()
        """Called by TAP when the test plan starts"""
        self.Info("PSLab Multimeter Opened")

    def Close(self):
        """Called by TAP when the test plan ends."""
        self.Info("PSLab Multimeter Closed")
        super(Multimeter, self).Close()

    def measure_resistance(self):
        """Measure the resistance of a resistor connected between RES and GND."""
        self.instrument.measure_resistance()

    def measure_voltage(self, channel = "VOL"):
        """Measure the voltage on the selected channel."""
        self.instrument.measure_voltage(channel)

    def calibrate_capacitance(self):
        """Calibrate stray capacitance."""
        self.instrument.calibrate_capacitance()

    def measure_capacitance(self):
        """Measure the capacitance of a capacitor connected between CAP and GND."""
        self.instrument.measure_capacitance()
    
