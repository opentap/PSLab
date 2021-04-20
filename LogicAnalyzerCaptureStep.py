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

@Attribute(DisplayAttribute, "Capture", "Captures logic events using Logic Analyzer", Groups= ["PSLab", "Logic Analyzer"])
class LogicAnalyzerCaptureStep(PSLabPublisherTestStep):
    def __init__(self):
        super(LogicAnalyzerCaptureStep, self).__init__()
        print("Capture test step initialized")

        prop = self.AddProperty("LogicAnalyzer", None, LogicAnalyzer)
        prop.AddAttribute(DisplayAttribute, "Logic Analyzer", "", "Resources", -100)

        selectable = self.AddProperty("channels", 1, Int32)
        selectable.AddAttribute(AvailableValuesAttribute, "Available")
        selectable.AddAttribute(DisplayAttribute, "Channels", "Number of channels to sample from simultaneously.", "Measurements", -50)
        available = self.AddProperty("Available", [1,2,3,4], List[Int32])
        available.AddAttribute(BrowsableAttribute, False)

        prop = self.AddProperty("events", 2500, Int32)
        prop.AddAttribute(DisplayAttribute, "Events", "Number of logic events to capture on each channel.", "Measurements", -40)

        prop = self.AddProperty("timeout", 1.0, Double)
        prop.AddAttribute(DisplayAttribute, "Timeout", "Timeout in seconds before cancelling measurement in blocking mode.", "Measurements", -40)

        prop = self.AddProperty("block", False, Boolean)
        prop.AddAttribute(DisplayAttribute, "Block", "Whether to block while waiting for events to be captured.", "Measurements", -30)

    # Inherited method from PythonTap TestStep abstract class
    def Run(self):
        data = self.LogicAnalyzer.capture(self.channels, events=self.events, timeout=self.timeout, block=self.block)
        """
        if self.block:
            self.PublishStepResult("Measured Interval", ["Interval"], [interval])
        """
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PrePlanRun(self):
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PostPlanRun(self):
        pass