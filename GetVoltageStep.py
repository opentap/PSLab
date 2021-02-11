"""
Test step to get the voltage on a PV1-3 pin
"""

from System import Double
from enum import Enum

from PythonTap import *
from OpenTap import DisplayAttribute, UnitAttribute

from .PSLabTestStep import PSLabTestStep
from .PowerSupply import *

class GetVoltageStep(PSLabTestStep):
    def __init__(self):
        super(GetVoltageStep, self).__init__()
        print("Get voltage test step initialized")

        prop = self.AddProperty("Pin", Pin.ONE, Pin)
        prop.AddAttribute(DisplayAttribute, "Pin", "The chosen PV pin", "", -50)

        prop = self.AddProperty("PowerSupply", None, PowerSupply)
        prop.AddAttribute(DisplayAttribute, "Power Supply", "", "Resources", -100)

    # Inherited method from PythonTap TestStep abstract class
    def Run(self):
        self.PowerSupply.getVoltage(self.Pin)
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PrePlanRun(self):
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PostPlanRun(self):
        pass
