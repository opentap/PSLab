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

@Attribute(DisplayAttribute, "Count pulses", "Count pulses on a digital channel", Groups= ["PSLab", "Logic Analyzer"])
class CountPulsesStep(PSLabPublisherTestStep):
    def __init__(self):
        super(CountPulsesStep, self).__init__()
        print("Count pulses step initialized")

        prop = self.AddProperty("LogicAnalyzer", None, LogicAnalyzer)
        prop.AddAttribute(DisplayAttribute, "Logic Analyzer", "", "Resources", -100)

        selectable = self.AddProperty("channel", "FRQ", String)
        selectable.AddAttribute(AvailableValuesAttribute, "Available")
        selectable.AddAttribute(DisplayAttribute, "Channel", "Channel to count pulses on.", "Measurements", -50)
        available = self.AddProperty("Available", ["LA1", "LA2", "LA3", "LA4", "FRQ"], List[String])
        available.AddAttribute(BrowsableAttribute, False)

        prop = self.AddProperty("interval", 1.0, Double)
        prop.AddAttribute(DisplayAttribute, "Interval", "Time in seconds during which to count pulses.", "Measurements", -40)

        prop = self.AddProperty("block", False, Boolean)
        prop.AddAttribute(DisplayAttribute, "Block", "Whether to block while waiting for pulses to be captured.", "Measurements", -30)

    # Inherited method from PythonTap TestStep abstract class
    def Run(self):
        data = self.LogicAnalyzer.count_pulses(self.channel, interval=self.interval, block=self.block)
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PrePlanRun(self):
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PostPlanRun(self):
        pass