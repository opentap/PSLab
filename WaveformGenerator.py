"""
Instrument wrapper for PSLab python API
"""    

from System import Double, String

from PythonTap import *
from OpenTap import DisplayAttribute

from pslab import WaveformGenerator as PSLabWaveformGenerator
from pslab.instrument.waveform_generator import logger
logger.setLevel('ERROR')

from .PSLabInstrument import PSLabInstrument
from .ConnectionHandler import ConnectionHandler

from typing import Callable, List, Tuple, Union
from enum import Enum

class WaveformPin(Enum):
    SI1 = "SI1"
    SI2 = "SI2"

@Attribute(DisplayAttribute, "Waveform Generator", "Waveform Generator Instrument", "PSLab")
class WaveformGenerator(PSLabInstrument):    
    def __init__(self):
        """Set up the properties, methods, and default values of the instrument."""
        super(WaveformGenerator, self).__init__()

        self.Name = "Waveform Generator"
        self.RegisterMethod("generate", None).AddArgument("Channels", String)
        self.RegisterMethod("generate", None).AddArgument("Frequency", String)
        self.RegisterMethod("generate", None).AddArgument("Phase", Double)
        
    def Open(self):
        """Called by TAP when the test plans starts."""
        super(WaveformGenerator, self).Open()
        self.instrument = ConnectionHandler.instance().getWaveformGenerator()
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
        self.instrument.generate(channels, frequency, phase)
