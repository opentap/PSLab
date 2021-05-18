"""
Instrument wrapper for PSLab Logic Analyzer Instrument
"""

from System import Double, Boolean

from PythonTap import *
from OpenTap import DisplayAttribute

from pslab import PowerSupply as PSLabPowerSupply
from pslab import protocol as CP
from pslab.instrument.digital import MODES

from .PSLabInstrument import PSLabInstrument
from .ConnectionHandler import ConnectionHandler

class DigitalPin(Enum):
    LA1 = 0
    LA2 = 1
    LA3 = 2
    LA4 = 3

@Attribute(DisplayAttribute, "LogicAnalyzer", "Logic Analyzer Instrument", "PSLab")
class LogicAnalyzer(PSLabInstrument):
    def __init__(self):
        "Set up the properties, methods and default values of the instrument."
        super(LogicAnalyzer, self).__init__() # The base class initializer must be invoked.

        self.Name = "Logic Analyzer"
        self.RegisterMethod("measure_frequency", None).AddArgument("channel", DigitalPin)
        self.RegisterMethod("measure_frequency", None).AddArgument("simultaneous_oscilloscope", Boolean)
        self.RegisterMethod("measure_frequency", None).AddArgument("timeout", Double)

    def Open(self):
        super(LogicAnalyzer, self).Open()
        # Open COM connection to instrument through ConnectionHandler
        self.instrument = ConnectionHandler.instance().getLogicAnalyzer()
        """Called by TAP when the test plan starts."""
        self.Info("PSLab Power Supply Opened")

    def Close(self):
        """Called by TAP when the test plan ends."""
        self.Info("PSLab Power Supply Closed")
        super(LogicAnalyzer, self).Close()

    def getPinName(self, pin):
        if pin == DigitalPin.LA1:
            return "LA1"
        elif pin == DigitalPin.LA2:
            return "LA2"
        elif pin == DigitalPin.LA3:
            return "LA3"
        elif pin == DigitalPin.LA4:
            return "LA4"
        else:
            raise ValueError("Invalid pin")

    # Not tested
    def measure_frequency(self, channel, simultaneous_oscilloscope=False, timeout=1):
        """Method to measure the frequency on one or multiple channels"""
        self.instrument.measure_frequency(channel, simultaneous_oscilloscope, timeout)

    # Not tested
    def measure_interval(self, channels, modes, timeout=1):
        """Method to measure the interval between two events"""
        self.instrument.measure_interval(channels, modes, timeout)

    # Not tested
    def measure_duty_cycle(self, channel, timeout=1):
        """Method to measure the duty cycle and wavelength, cannot be used at the same time as oscilloscope"""
        self.instrument.measure_duty_cycle(channel, timeout)

    # Tested with no events and block=False
    def capture(self, channels, events=CP.MAX_SAMPLES//4, timeout=1, modes=4*("any",), e2e_time=None, block=True):
        """Method to capture logic events, cannot be used at the same time as oscilloscope."""
        self.instrument.capture(channels, events, timeout, modes, e2e_time, block)

    # Not tested
    def fetch_data(self):
        """Method to collect captured events"""
        return self.instrument.fetch_data()

    # Not tested
    def get_progress(self):
        """Method to return number of collected events per channel in buffer"""
        return self.instrument.get_progress()

    # Tested without signal
    def get_initial_states(self):
        """Method to return initial state of each digital input at start of capture"""
        return self.instrument.get_initial_states()

    # Not tested
    def stop(self):
        """Method to stop running the capture function"""
        self.instrument.stop()

    # Tested without signal
    def get_states(self):
        """Method to get the current states of the digital inputs"""
        return self.instrument.get_states()

    # Not tested
    def count_pulses(self, channel="FRQ", interval=1, block=True):
        """Method to count pulses on a digital input"""
        return self.instrument.count_pulses(channel, interval, block)

    # Not tested
    def fetch_pulse_count(self):
        """Method to get the number of pulses counted since calling count_pulses"""
        return self.instrument.fetch_pulse_count()
