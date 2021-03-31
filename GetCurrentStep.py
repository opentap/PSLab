"""
Test step to get the current on the PCS pin on the PSLab board
"""

from System import Double

from PythonTap import *
from OpenTap import DisplayAttribute, UnitAttribute

from .PSLabPublisherTestStep import PSLabPublisherTestStep
from .PowerSupply import PowerSupply

@Attribute(DisplayAttribute, "Get Current", "Gets current of pin", "PSLab")
class GetCurrentStep(PSLabPublisherTestStep):
    def __init__(self):
        super(GetCurrentStep, self).__init__()
        print("Get current test step initialized")

        prop = self.AddProperty("PowerSupply", None, PowerSupply)
        prop.AddAttribute(DisplayAttribute, "Power Supply", "", "Resources", -100)

    # Inherited method from PythonTap TestStep abstract class
    def Run(self):
        current = float(self.PowerSupply.getPcs())
        super(GetCurrentStep, self).PublishStepResult("PowerSupply", ["Current"], [current])
        self.PowerSupply.getPcs()
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PrePlanRun(self):
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PostPlanRun(self):
        pass
