"""
Test step to set the current on the PCS pin on the PSLab board
"""

from System import Double

from PythonTap import *
from OpenTap import DisplayAttribute, UnitAttribute

from .PSLabSetterTestStep import PSLabSetterTestStep
from .PowerSupply import PowerSupply

class SetCurrentStep(PSLabSetterTestStep):
    def __init__(self):
        super(SetCurrentStep, self).__init__()
        print("Set current test step initialized")

        prop = self.AddProperty("Current", 0, Double)
        prop.AddAttribute(DisplayAttribute, "Current", "The current to be output on the PCS pin", "Measurements", -50)
        prop.AddAttribute(UnitAttribute, "A")

        prop = self.AddProperty("PowerSupply", None, PowerSupply)
        prop.AddAttribute(DisplayAttribute, "Power Supply", "", "Resources", -100)

    # Inherited method from PythonTap TestStep abstract class
    def Run(self):
        self.PowerSupply.setPcs(self.Current)
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PrePlanRun(self):
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PostPlanRun(self):
        pass
