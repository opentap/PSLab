import clr
clr.AddReference("System.Collections")
from System.Collections.Generic import List
from System import Int32, Double, Boolean
from System.ComponentModel import BrowsableAttribute # BrowsableAttribute can be used to hide things from the user.

from PythonTap import *
from OpenTap import DisplayAttribute, UnitAttribute, AvailableValuesAttribute

from .PSLabSetterTestStep import PSLabSetterTestStep
from .PSLabPublisherTestStep import PSLabPublisherTestStep
from .LogicAnalyzer import *

@Attribute(DisplayAttribute, "Measure Frequency", "Measures frequency on a digital pin", Groups= ["PSLab", "Logic Analyzer"])
class MeasureFrequencyStep(PSLabPublisherTestStep):
    def __init__(self):
        super(MeasureFrequencyStep, self).__init__()
        print("Measure frequency test step initialized")

        prop = self.AddProperty("LogicAnalyzer", None, LogicAnalyzer)
        prop.AddAttribute(DisplayAttribute, "Logic Analyzer", "", "Resources", -100)

        selectable = self.AddProperty("channel", DigitalPin.LA1, DigitalPin)
        selectable.AddAttribute(DisplayAttribute, "Channel", "Name of digital channel to measure frequency on", "Measurements", -50)

        prop = self.AddProperty("simultaneous_oscilloscope", False, Boolean)
        prop.AddAttribute(DisplayAttribute, "Simultaneously Using Oscilloscope", "Set to true if using oscilloscope at the same time", "Measurements", -40)

        prop = self.AddProperty("timeout", 0.0, Double)
        prop.AddAttribute(DisplayAttribute, "Timeout", "Timeout in seconds before cancelling measurement", "Measurements", -30)

    # Inherited method from PythonTap TestStep abstract class
    def Run(self):
        frequency = self.LogicAnalyzer.measure_frequency(self.LogicAnalyzer.getPinName(self.channel), self.simultaneous_oscilloscope, self.timeout)
        self.PublishStepResult("Measured Frequency", ["Frequency"], [frequency])
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PrePlanRun(self):
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PostPlanRun(self):
        pass