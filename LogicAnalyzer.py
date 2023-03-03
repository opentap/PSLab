"""
Instrument wrapper for PSLab Logic Analyzer Instrument
"""
from enum import Enum

from OpenTap import Display
from opentap import *
from pslab import protocol as CP

from .ConnectionHandler import ConnectionHandler


class DigitalPin(Enum):
    LA1 = 0
    LA2 = 1
    LA3 = 2
    LA4 = 3


@attribute(Display("Logic Analyzer", "Logic Analyzer Instrument", "PSLab"))
class LogicAnalyzer(Instrument):
    def __init__(self):
        "Set up the properties, methods and default values of the instrument."
        super(LogicAnalyzer, self).__init__()  # The base class initializer must be invoked.

        self.instrument = None
        self.Name = "Logic Analyzer"

    def Open(self):
        super(LogicAnalyzer, self).Open()
        # Open COM connection to instrument through ConnectionHandler
        self.instrument = ConnectionHandler.instance().getLogicAnalyzer()
        """Called by TAP when the test plan starts."""

    def Close(self):
        """Called by TAP when the test plan ends."""
        super(LogicAnalyzer, self).Close()

    def measure_frequency(self, channel, simultaneous_oscilloscope=False, timeout=1):
        """Method to measure the frequency"""
        return self.instrument.measure_frequency(channel.name, simultaneous_oscilloscope, timeout)

    def measure_interval(self, channels, modes, timeout=1):
        """Method to measure the interval between two events"""
        return self.instrument.measure_interval(list(map(lambda c: c.name, channels)), modes, timeout)

    def measure_duty_cycle(self, channel, timeout=1):
        """Method to measure the duty cycle and wavelength, cannot be used at the same time as oscilloscope"""
        return self.instrument.measure_duty_cycle(channel.name, timeout)

    # Tested with no events and block=False
    def capture(self, channels, events=CP.MAX_SAMPLES // 4, timeout=1, modes=4 * ("any",), e2e_time=None, block=True):
        """Method to capture logic events, cannot be used at the same time as oscilloscope."""
        return self.instrument.capture(channels, events, timeout, modes, e2e_time, block)

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
