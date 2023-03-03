from OpenTap import Display
from opentap import *

from .ConnectionHandler import ConnectionHandler


@attribute(Display("Oscilloscope", "Oscilloscope Instrument", "PSLab"))
class Oscilloscope(Instrument):
    def __init__(self):
        """Set up the properties, methods and default values of the instrument."""
        super(Oscilloscope, self).__init__()  # The base class initializer must be invoked.
        self.instrument = None
        self.Name = "Oscilloscope"

    def Open(self):
        super(Oscilloscope, self).Open()
        # Open COM connection to instrument using ConnectionHandler
        self.instrument = ConnectionHandler.instance().getOscilloscope()
        """Called by TAP when the test plan starts"""

    def Close(self):
        """Called by TAP when the test plan ends."""
        super(Oscilloscope, self).Close()

    def capture(self, channels, samples, timegap):
        """Capture an oscilloscope trace from the specified input channels."""
        if isinstance(channels, str):
            x, y = self.instrument.capture(channels, samples, timegap)
            self.log.Info(f"Samples captured on channel '{channels}': {x} {y}")
            return x, y

        match channels:
            case 1:
                x, y = self.instrument.capture(channels, samples, timegap)
                self.log.Info(f"Samples captured on one channel: {x} {y}")
                return x, y
            case 2:
                x, y1, y2 = self.instrument.capture(channels, samples, timegap)
                self.log.Info(f"Samples captured on two channels: {x} {y1} {y2}")
                return x, y1, y2
            case 3:
                x, y1, y2, y3 = self.instrument.capture(channels, samples, timegap)
                self.log.Info(f"Samples captured on three channels: {x} {y1} {y2} {y3}")
                return x, y1, y2, y3
            case 4:
                x, y1, y2, y3, y4 = self.instrument.capture(channels, samples, timegap)
                self.log.Info(f"Samples captured on four channels: {x} {y1} {y2} {y3} {y4}")
                return x, y1, y2, y3, y4
            case _:
                raise Exception(f"Invalid number of channels: {channels}")
