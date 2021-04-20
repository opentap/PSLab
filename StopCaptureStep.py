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

@Attribute(DisplayAttribute, "Stop Capture", "Stops the capture method if it's running", Groups= ["PSLab", "Logic Analyzer"])
class StopCaptureStep(PSLabPublisherTestStep):
    def __init__(self):
        super(StopCaptureStep, self).__init__()
        print("Stop capture test step initialized")

        prop = self.AddProperty("LogicAnalyzer", None, LogicAnalyzer)
        prop.AddAttribute(DisplayAttribute, "Logic Analyzer", "", "Resources", -100)

    # Inherited method from PythonTap TestStep abstract class
    def Run(self):
        self.LogicAnalyzer.stop()
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PrePlanRun(self):
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PostPlanRun(self):
        pass