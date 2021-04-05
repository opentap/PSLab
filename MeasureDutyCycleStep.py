import clr
clr.AddReference("System.Collections")
from System.Collections.Generic import List
from System import Int32, Double, Boolean, String
from System.ComponentModel import BrowsableAttribute # BrowsableAttribute can be used to hide things from the user.

from PythonTap import *
from OpenTap import DisplayAttribute, UnitAttribute, AvailableValuesAttribute

from .PSLabSetterTestStep import PSLabSetterTestStep
from .PSLabPublisherTestStep import PSLabPublisherTestStep
from .LogicAnalyzer import *

@Attribute(DisplayAttribute, "Measure Duty Cycle", "Measures the duty cycle and wavelength", Groups= ["PSLab", "Logic Analyzer"])
class MeasureDutyCycleStep(PSLabPublisherTestStep):
    def __init__(self):
        super(MeasureDutyCycleStep, self).__init__()
        print("Measure duty cycle test step initialized")

        prop = self.AddProperty("LogicAnalyzer", None, LogicAnalyzer)
        prop.AddAttribute(DisplayAttribute, "Logic Analyzer", "", "Resources", -100)

        selectable = self.AddProperty("channel", DigitalPin.LA1, DigitalPin)
        selectable.AddAttribute(DisplayAttribute, "Channel", "Name of digital channel to listen on", "Measurements", -50)

        prop = self.AddProperty("timeout", 0.0, Double)
        prop.AddAttribute(DisplayAttribute, "Timeout", "Timeout in seconds before cancelling measurement", "Measurements", -30)

    # Inherited method from PythonTap TestStep abstract class
    def Run(self):
        period, duty_cycle = self.LogicAnalyzer.measure_duty_cycle(self.LogicAnalyzer.getPinName(self.channel), self.timeout)
        self.PublishStepResult("Measured Duty Cycle", ["Period", "Duty Cycle"], [period, duty_cycle])
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PrePlanRun(self):
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PostPlanRun(self):
        pass