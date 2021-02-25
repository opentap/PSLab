"""
Test step to get the voltage on a PV1-3 pin
"""

from System import Double
from enum import Enum

from PythonTap import *
from OpenTap import DisplayAttribute, UnitAttribute

from .PSLabPublisherTestStep import PSLabPublisherTestStep
from .PowerSupply import *

class GetVoltageStep(PSLabPublisherTestStep):
    def __init__(self):
        super(GetVoltageStep, self).__init__()
        print("Get voltage test step initialized")

        prop = self.AddProperty("Pin", Pin.ONE, Pin)
        prop.AddAttribute(DisplayAttribute, "Pin", "The chosen PV pin", "", -50)

        prop = self.AddProperty("PowerSupply", None, PowerSupply)
        prop.AddAttribute(DisplayAttribute, "Power Supply", "", "Resources", -100)

    # Inherited method from PythonTap TestStep abstract class
    def Run(self):
        # super(GetVoltageStep, self).PublishStepResult("PowerSupply", ["Voltage"], [self.PowerSupply.getVoltage(self.Pin)])
        voltage = float(self.PowerSupply.getVoltage(self.Pin))
        super(GetVoltageStep, self).PublishStepResult("PowerSupply", ["Voltage"], [voltage])
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PrePlanRun(self):
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PostPlanRun(self):
        pass
