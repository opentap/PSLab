"""
Test step to generate a sine waveform
"""
import clr
clr.AddReference("System.Collections")
from System.Collections.Generic import List
from System import Double, Int32
from System.ComponentModel import BrowsableAttribute

from PythonTap import *
from OpenTap import DisplayAttribute, UnitAttribute, AvailableValuesAttribute

from .PSLabSetterTestStep import PSLabSetterTestStep
from .WaveformGenerator import *

class SineWavePin(Enum):
    SI1 = 0
    SI2 = 1

def getStrFromSineWavePin(pin: SineWavePin):
    if pin is SineWavePin.SI1:
        return "SI1"
    else: 
        return "SI2"

@Attribute(DisplayAttribute, "Generate Sine Wave", "Generates a Sine Wave of given frequency and phase on given pin", Groups= ["PSLab", "Waveform Generator"])
class GenerateSineWave(TestStep):
    def __init__(self):
        """Set up the properties, methods, and default values of the step."""
        super(GenerateSineWave, self).__init__()
        print("Generate Sine Wave test step initialized")

        frequency = self.AddProperty("Frequency", 500, float)
        frequency.AddAttribute(DisplayAttribute, "Frequency", "The frequency of the sine wave")
        frequency.AddAttribute(UnitAttribute, "Hz")

        phase = self.AddProperty("Phase", 0, float)
        phase.AddAttribute(DisplayAttribute, "Phase", "The phase of the sine wave")
        phase.AddAttribute(UnitAttribute, "°") # this is used for the unit of measurement

        pin = self.AddProperty("Pin", SineWavePin.SI1, SineWavePin)
        pin.AddAttribute(DisplayAttribute, "Pin", "Pin on which the sine wave is generated: SI1 or SI2")
        
        waveformGenerator = self.AddProperty("WaveformGenerator", None, WaveformGenerator)
        waveformGenerator.AddAttribute(DisplayAttribute, "Waveform Generator", "", "Resources", -100)

    # Inherited method from PythonTap TestStep abstract class
    def Run(self):
        """Called when the test step is executed."""
        pinStr = getStrFromSineWavePin(self.Pin)
        self.WaveformGenerator.generate_sine(pinStr, self.Frequency, self.Phase)
