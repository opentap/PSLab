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
from .PWMGenerator import *

class SquareWavePin(Enum):
    SQ1 = 0
    SQ2 = 1
    SQ3 = 2
    SQ4 = 3

def getStrFromSquareWavePin(pin: SquareWavePin):
    if pin is SquareWavePin.SQ1:
        return "SQ1"
    elif pin is SquareWavePin.SQ2:
        return "SQ2"
    elif pin is SquareWavePin.SQ3:
        return "SQ3"
    else: 
        return "SQ4"

@Attribute(DisplayAttribute, "Generate Square Wave", "Generates a Square Wave of given frequency, duty cycle, and phase on given pin", Groups= ["PSLab", "PWM Generator"])
class GenerateSquareWave(TestStep):
    def __init__(self):
        """Set up the properties, methods, and default values of the step."""
        super(GenerateSquareWave, self).__init__()
        print("Generate Square Wave test step initialized")

        frequency = self.AddProperty("Frequency", 500, float)
        frequency.AddAttribute(DisplayAttribute, "Frequency", "The frequency of the square wave")
        frequency.AddAttribute(UnitAttribute, "Hz")

        duty_cycles = self.AddProperty("Duty_Cycles", 0.1, float)
        duty_cycles.AddAttribute(DisplayAttribute, "Duty Cycles", "The duty cycle of the square wave")

        phase = self.AddProperty("Phases", 0, float)
        phase.AddAttribute(DisplayAttribute, "Phase", "The phase of the square wave")
        phase.AddAttribute(UnitAttribute, "°") # this is used for the unit of measurement

        pin = self.AddProperty("Pin", SquareWavePin.SQ1, SquareWavePin)
        pin.AddAttribute(DisplayAttribute, "Pin", "Pin on which the sine wave is generated: SQ1, SQ2, SQ3, or SQ4")
        
        pwmGenerator = self.AddProperty("PWMGenerator", None, PWMGenerator)
        pwmGenerator.AddAttribute(DisplayAttribute, "PWM Generator", "", "Resources", -100)

    # Inherited method from PythonTap TestStep abstract class
    def Run(self):
        """Called when the test step is executed."""
        pinStr = getStrFromSquareWavePin(self.Pin)
        self.PWMGenerator.generate(pinStr, self.Frequency, self.Duty_Cycles, self.Phases)
