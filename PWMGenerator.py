from System import Double, String
from PythonTap import *
from OpenTap import DisplayAttribute

from .PSLabInstrument import PSLabInstrument
from .ConnectionHandler import ConnectionHandler

@Attribute(DisplayAttribute, "PWM Generator", "PWM Generator Instrument", "PSLab")
class PWMGenerator(PSLabInstrument):    
    def __init__(self):
        """Set up the properties, methods, and default values of the instrument."""
        super(PWMGenerator, self).__init__()

        self.Name = "PWM Generator"
        
    def Open(self):
        """Called by TAP when the test plans starts."""
        super(PWMGenerator, self).Open()
        self.instrument = ConnectionHandler.instance().getPWMGenerator()
        self.Info("PSLab PWM Generator opened")

    def Close(self):
        """Called by TAP when the test plans ends."""
        self.Info("PSLab PWM Generator closed")
        super(PWMGenerator, self).Close()

    def generate(self, channels, frequency, duty_cycles, phases = 0):
        """Generate PWM signals on SQ1, SQ2, SQ3, and SQ4."""
        self.instrument.generate(channels, frequency, duty_cycles, phases)
