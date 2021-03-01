"""
Instrument wrapper for PSLab python API
"""    

#    from System import Double
#    from PythonTap import *
#    from OpenTap import DisplayAttribute

#from os import O_NDELAY
from pslab import WaveformGenerator # <-- should this be waveform_generator or 

from .PSLabInstrument import PSLabInstrument
    
#import logging
from typing import Callable, List, Tuple, Union

import numpy as np

import pslab.protocol as CP
from pslab.instrument.analog import AnalogOutput

from pslab.instrument.digital import DigitalOutput, DIGITAL_OUTPUTS
from pslab.serial_handler import SerialHandler
from enum import Enum

class Pin(Enum):
    SI1 = "SI1"
    SI2 = "SI2"


    
class Create_AWG(PSLabInstrument):    
    
    def __init__(self):
        #setting up device 
        super(Create_AWG).__init__()

        self.Name = "Create_AWG"
       #self.RegisterMethod("generate", None).AddArgument("channels", string)
        
    def Open(self):
        super(Create_AWG, self).Open()
        self.instrument = WaveformGenerator()
        self.Info("PSLab Create_AWG opened")

    def Close(self):
        self.Info("PSLab Create_AWG closed")
        super(Create_AWG, self).Close()


    def generate(
        self,
        channels: Union[str, List[str]],
        frequency: Union[float, List[float]],
        phase: float = 0,
    ) -> List[float]:

       wave = self.instrument.generate(channels, frequency, phase)
       self.Info(f"Wave generated: {wave}")
        
        
        
       
       



