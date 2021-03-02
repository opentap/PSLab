from PythonTap import *
from OpenTap import DisplayAttribute
from pslab import Oscilloscope as PSLabOscilloscope
from .PSLabInstrument import PSLabInstrument

#class Channels(Enum):
#    ONE = 1
#    TWO = 2
#    FOUR = 4

@Attribute(DisplayAttribute, "Oscilloscope", "Oscilloscope Instrument", "PSLab")
class Oscilloscope(PSLabInstrument):
    def __init__(self):
        "Set up the properties, methods and default values of the instrument."
        super(Oscilloscope, self).__init__() # The base class initializer must be invoked.
        self.Name = "Oscilloscope"

    def Open(self):
        super(Oscilloscope, self).Open()
        # Open COM connection to instrument, blocks other instrument connections while connected
        self.instrument = PSLabOscilloscope()
        """Called by TAP when the test plan starts"""
        self.Info("PSLab Oscilloscope Opened")

    def Close(self):
        """Called by TAP when the test plan ends."""
        self.Info("PSLab Oscilloscope Closed")
        super(Oscilloscope, self).Close()

    def capture(self, channels, samples, timegap):
        if channels == 1:
            x,y = self.instrument.capture(channels, samples, timegap)
            self.Info(f"One sample captured: {x} {y}")
        elif channels == 2:
            x,y1,y2 = self.instrument.capture(channels, samples, timegap)
            self.Info(f"Two samples captured: {x} {y1} {y2}")
        elif channels == 4:
            x,y1,y2,y3,y4 = self.instrument.capture(channels, samples, timegap)
            self.Info(f"Four samples captured: {x} {y1} {y2} {y3} {y4}")
        pass