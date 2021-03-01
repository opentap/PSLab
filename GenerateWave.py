"""
Test step to Create_AWG
"""

from System import Double

from PythonTap import *
from OpenTap import DisplayAttribute, UnitAttribute

from .PSLabSetterTestStep import PSLabSetterTestStep
from .Create_AWG import Create_AWG
from .Create_AWG import Pin


class GenerateWave(PSLabSetterTestStep):
    def __init__(self):
        super(GenerateWave, self).__init__()
        print("GenerateWave test step initialized")

        prop = self.AddProperty("channels", Pin.SI1, Pin)
        prop.AddAttribute(DisplayAttribute, "Channels", "The current to be output on the PCS pin", "Measurements", -50)
        prop.AddAttribute(UnitAttribute, "A")

        prop = self.AddProperty("frequency", 0, float)
        prop.AddAttribute(DisplayAttribute, "frequency", "The frequency to be output", "Measurements", -50)
        prop.AddAttribute(UnitAttribute, "A")

        prop = self.AddProperty("phase", 0, float)
        prop.AddAttribute(DisplayAttribute, "phase", "The phase to be output", "Measurements", -50)
        prop.AddAttribute(UnitAttribute, "A") # this is used for the unit of measurement

        prop = self.AddProperty("Create_AWG", None, Create_AWG)
        prop.AddAttribute(DisplayAttribute, "Create AWG", "", "Resources", -100)

    # Inherited method from PythonTap TestStep abstract class
    def Run(self):
        self.Create_AWG.generate(self.channels.value, self.frequency, self.phase)
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PrePlanRun(self):
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PostPlanRun(self):
        pass
