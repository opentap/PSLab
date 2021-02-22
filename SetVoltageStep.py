"""
Test step to set the voltage on a PV1-3 pin
"""

from System import Double
from enum import Enum

from PythonTap import *
from OpenTap import DisplayAttribute, UnitAttribute

from .PSLabSetterTestStep import PSLabSetterTestStep
from .PowerSupply import *

class SetVoltageStep(PSLabSetterTestStep):
    def __init__(self):
        super(SetVoltageStep, self).__init__()
        print("Set voltage test step initialized")

        prop = self.AddProperty("Voltage", 0, Double)
        prop.AddAttribute(DisplayAttribute, "Voltage", "The voltage to be output on the chosen PV pin", "Measurements", -50)
        prop.AddAttribute(UnitAttribute, "V")

        prop = self.AddProperty("Pin", Pin.ONE, Pin)
        prop.AddAttribute(DisplayAttribute, "Pin", "The chosen PV pin", "", -50)

        prop = self.AddProperty("PowerSupply", None, PowerSupply)
        prop.AddAttribute(DisplayAttribute, "Power Supply", "", "Resources", -100)

    # Inherited method from PythonTap TestStep abstract class
    def Run(self):
        self.PowerSupply.setVoltage(self.Pin, self.Voltage)
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PrePlanRun(self):
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PostPlanRun(self):
        pass
