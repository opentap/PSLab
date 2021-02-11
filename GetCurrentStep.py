"""
Test step to get the current on the PCS pin on the PSLab board
"""

from System import Double

from PythonTap import *
from OpenTap import DisplayAttribute, UnitAttribute

from .PSLabTestStep import PSLabTestStep
from .PowerSupply import PowerSupply

class GetCurrentStep(PSLabTestStep):
    def __init__(self):
        super(GetCurrentStep, self).__init__()
        print("Get current test step initialized")

        prop = self.AddProperty("PowerSupply", None, PowerSupply)
        prop.AddAttribute(DisplayAttribute, "Power Supply", "", "Resources", -100)

    # Inherited method from PythonTap TestStep abstract class
    def Run(self):
        self.PowerSupply.getPcs()
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PrePlanRun(self):
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PostPlanRun(self):
        pass
