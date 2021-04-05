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

@Attribute(DisplayAttribute, "Measure Interval", "Measures time between two events on digital channels", Groups= ["PSLab", "Logic Analyzer"])
class MeasureIntervalStep(PSLabPublisherTestStep):
    def __init__(self):
        super(MeasureIntervalStep, self).__init__()
        print("Measure interval test step initialized")

        prop = self.AddProperty("LogicAnalyzer", None, LogicAnalyzer)
        prop.AddAttribute(DisplayAttribute, "Logic Analyzer", "", "Resources", -100)

        selectable = self.AddProperty("channel1", DigitalPin.LA1, DigitalPin)
        selectable.AddAttribute(DisplayAttribute, "Channel #1", "Name of digital channel to listen for first event on", "Measurements", -50)

        selectable = self.AddProperty("channel2", DigitalPin.LA1, DigitalPin)
        selectable.AddAttribute(DisplayAttribute, "Channel #2", "Name of digital channel to listen for second event on", "Measurements", -50)

        prop = self.AddProperty("mode1", "any", String)
        prop.AddAttribute(AvailableValuesAttribute, "Modes")
        prop.AddAttribute(DisplayAttribute, "Mode #1", "Type of logic event to listen for on channel #1", "Measurements", -40)

        prop = self.AddProperty("mode2", "any", String)
        prop.AddAttribute(AvailableValuesAttribute, "Modes")
        prop.AddAttribute(DisplayAttribute, "Mode #2", "Type of logic event to listen for on channel #2", "Measurements", -40)

        modes = self.AddProperty("Modes", list(MODES.keys()), List[String])
        modes.AddAttribute(BrowsableAttribute, False)

        prop = self.AddProperty("timeout", 0.0, Double)
        prop.AddAttribute(DisplayAttribute, "Timeout", "Timeout in seconds before cancelling measurement", "Measurements", -30)

    # Inherited method from PythonTap TestStep abstract class
    def Run(self):
        interval = self.LogicAnalyzer.measure_interval([self.LogicAnalyzer.getPinName(self.channel1), self.LogicAnalyzer.getPinName(self.channel2)], [self.mode1, self.mode2], self.timeout)
        self.PublishStepResult("Measured Interval", ["Interval"], [interval])
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PrePlanRun(self):
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PostPlanRun(self):
        pass