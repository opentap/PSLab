from PythonTap import *
from OpenTap import DisplayAttribute
from pslab import Oscilloscope as PSLabOscilloscope
from .PSLabInstrument import PSLabInstrument

@Attribute(DisplayAttribute, "Oscilloscope", "Oscilloscope Instrument", "PSLab")
class Oscilloscope(PSLabInstrument):
    def __init__(self):
        """Set up the properties, methods and default values of the instrument."""
        super(Oscilloscope, self).__init__() # The base class initializer must be invoked.
        self.Name = "Oscilloscope"

    def Open(self):
        super(Oscilloscope, self).Open()
        # Open COM connection to instrument, blocks other instrument connections while connected
        self.instrument = PSLabOscilloscope()# ConnectionHandler.openConnection())
        """Called by TAP when the test plan starts"""
        self.Info("PSLab Oscilloscope Opened")

    def Close(self):
        """Called by TAP when the test plan ends."""
        self.Info("PSLab Oscilloscope Closed")
        super(Oscilloscope, self).Close()
        # Call ConnectionHandler.closeConnection() to close
        #ConnectionHandler.closeConnection()

    def capture(self, channels, samples, timegap):
        """Capture an oscilloscope trace from the specified input channels."""
        if channels == 1:
            x,y = self.instrument.capture(channels, samples, timegap)
            self.Info(f"Samples captured on one channel: {x} {y}")
            return x,y
        elif channels == 2:
            x,y1,y2 = self.instrument.capture(channels, samples, timegap)
            self.Info(f"Samples captured on two channels: {x} {y1} {y2}")
            return x,y1,y2
        elif channels == 4:
            x,y1,y2,y3,y4 = self.instrument.capture(channels, samples, timegap)
            self.Info(f"Samples captured on four channels: {x} {y1} {y2} {y3} {y4}")
            return x,y1,y2,y3,y4
        else:
            error("Invalid number of channels")
        pass