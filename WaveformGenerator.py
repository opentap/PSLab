"""
Instrument wrapper for PSLab python API
"""    

from System import Double, String

from PythonTap import *
from OpenTap import DisplayAttribute

from pslab import WaveformGenerator as PSLabWaveformGenerator

from .PSLabInstrument import PSLabInstrument
    
from typing import Callable, List, Tuple, Union

# import numpy as np

# import pslab.protocol as CP
# from pslab.instrument.analog import AnalogOutput

# from pslab.instrument.digital import DigitalOutput, DIGITAL_OUTPUTS
# from pslab.serial_handler import SerialHandler

from enum import Enum

class Pin(Enum):
    SI1 = "SI1"
    SI2 = "SI2"

@Attribute(DisplayAttribute, "Waveform Generator", "Waveform generator instrument", "PSLab")
class WaveformGenerator(PSLabInstrument):    
    def __init__(self):
        """Set up the properties, methods, and default values of the instrument."""
        super(WaveformGenerator, self).__init__()

        self.Name = "WaveformGenerator"
        self.RegisterMethod("generate", None).AddArgument("channels", String)
        self.RegisterMethod("generate", None).AddArgument("frequency", String)
        self.RegisterMethod("generate", None).AddArgument("phase", Double)
        
    def Open(self):
        """Called by TAP when the test plans starts."""
        super(WaveformGenerator, self).Open()
        self.instrument = PSLabWaveformGenerator()
        self.Info("PSLab Waveform Generator opened")

    def Close(self):
        """Called by TAP when the test plans ends."""
        self.Info("PSLab Waveform Generator closed")
        super(WaveformGenerator, self).Close()

    def generate(
        self,
        channels: Union[str, List[str]],
        frequency: Union[float, List[float]],
        phase: float = 0,
    ) -> List[float]:
        """Generates a waveform with the given parameters via pslab python api call"""
        wave = self.instrument.generate(channels, frequency, phase)
        self.Info(f"Wave generated: {wave}")
