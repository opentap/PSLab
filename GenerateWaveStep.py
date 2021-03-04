"""
Test step to generate a waveform
"""

from System import Double

from PythonTap import *
from OpenTap import DisplayAttribute, UnitAttribute

from .PSLabSetterTestStep import PSLabSetterTestStep
from .WaveformGenerator import *


class GenerateWaveStep(PSLabSetterTestStep):
    def __init__(self):
        """Set up the properties, methods, and default values of the step."""
        super(GenerateWaveStep, self).__init__()
        print("GenerateWave test step initialized")

        prop = self.AddProperty("channels", WaveformPin.SI1, WaveformPin)
        prop.AddAttribute(DisplayAttribute, "Channels", "The current to be output on the PCS pin", "Measurements", -50)
        prop.AddAttribute(UnitAttribute, "A")

        prop = self.AddProperty("frequency", 0, float)
        prop.AddAttribute(DisplayAttribute, "frequency", "The frequency to be output", "Measurements", -50)
        prop.AddAttribute(UnitAttribute, "A")

        prop = self.AddProperty("phase", 0, float)
        prop.AddAttribute(DisplayAttribute, "phase", "The phase to be output", "Measurements", -50)
        prop.AddAttribute(UnitAttribute, "A") # this is used for the unit of measurement

        prop = self.AddProperty("WaveformGenerator", None, WaveformGenerator)
        prop.AddAttribute(DisplayAttribute, "WaveformGenerator", "", "Resources", -100)

    # Inherited method from PythonTap TestStep abstract class
    def Run(self):
        """Called when the test step is executed."""
        self.WaveformGenerator.generate(self.channels.value, self.frequency, self.phase)
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PrePlanRun(self):
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PostPlanRun(self):
        pass
