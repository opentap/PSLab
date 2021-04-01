"""
Instrument wrapper for PSLab Logic Analyzer Instrument
"""

from System import Double

from PythonTap import *
from OpenTap import DisplayAttribute

from pslab import PowerSupply as PSLabPowerSupply
from pslab import protocol as CP

from .PSLabInstrument import PSLabInstrument
from .ConnectionHandler import ConnectionHandler

class DigitalPin(Enum):
    LA1 = "LA1"
    LA2 = "LA2"
    LA3 = "LA3"
    LA4 = "LA4"

@Attribute(DisplayAttribute, "Logic Analyzer", "Logic Analyzer Instrument", "PSLab")
class LogicAnalyzer(PSLabInstrument):
    def __init__(self):
        "Set up the properties, methods and default values of the instrument."
        super(LogicAnalyzer, self).__init__() # The base class initializer must be invoked.

        self.Name = "Logic Analyzer"
        self.RegisterMethod("pcs", None).AddArgument("current", Double)

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

    def measure_frequency(self, channel, simultaneous_oscilloscope=False, timeout=1):
        """Method to measure the frequency on one or multiple channels"""
        self.instrument.measure_frequency(channel, simultaneous_oscilloscope, timeout)

    def measure_interval(self, channels, modes, timeout=1):
        """Method to measure the interval between two events"""
        self.instrument.measure_interval(channels, modes, timeout)

    def measure_duty_cycle(self, channel, timeout=1):
        """Method to measure the duty cycle and wavelength, cannot be used at the same time as oscilloscope"""
        self.instrument.measure_duty_cycle(channel, timeout)

    def capture(self, channels, events=CP.MAX_SAMPLES//4, timeout=1, modes=4*("any",), e2e_time=None, block=True):
        """Method to capture logic events, cannot be used at the same time as oscilloscope."""
        self.instrument.capture(channels, events, timeout, modes, e2e_time, block)

    def fetch_data(self):
        """Method to collect captured events"""
        return self.instrument.fetch_data()

    def get_progress(self):
        """Method to return number of collected events per channel in buffer"""
        return self.instrument.get_progress()

    def get_initial_states(self):
        """Method to return initial state of each digital input at start of capture"""
        return self.instrument.get_initial_states()

    def get_xy(self, timestamps, inital_states=None):
        """Method to turn timestamps into plottable data"""
        return self.instrument.get_xy(timestamps, initial_states)

    def configure_trigger(self, trigger_channel, trigger_mode):
        """Method to set up a trigger channel and trigger conditions"""
        self.instrument.configure_trigger(trigger_channel, trigger_mode)

    def stop(self):
        """Method to stop running the capture function"""
        self.instrument.stop()

    def get_states(self):
        """Method to get the current states of the digital inputs"""
        return self.instrument.get_states()

    def count_pulses(self, channel="FRQ", interval=1, block=True):
        """Method to count pulses on a digital input"""
        return self.instrument.count_pulses(channel, interval, block)

    def fetch_pulse_conf(self):
        """Method to get the number of pulses counted since calling count_pulses"""
        return self.instrument.fetch_pulse_conf()
