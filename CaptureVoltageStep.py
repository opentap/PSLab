import clr
clr.AddReference("System.Collections")
from System.Collections.Generic import List
from System import Int32, Double

from PythonTap import *
from OpenTap import DisplayAttribute, UnitAttribute, AvailableValuesAttribute

from .PSLabSetterTestStep import PSLabSetterTestStep
from .PSLabPublisherTestStep import PSLabPublisherTestStep
from .Oscilloscope import *

class CaptureVoltageStep(PSLabSetterTestStep):
    def __init__(self):
        super(CaptureVoltageStep, self).__init__()
        print("Capture test step initialized")

        prop = self.AddProperty("Oscilloscope", None, Oscilloscope)
        prop.AddAttribute(DisplayAttribute, "Instrument", "", "Resources", -100)

        selectable = self.AddProperty("Selectable", 1, Int32)
        selectable.AddAttribute(AvailableValuesAttribute, "Available")
        selectable.AddAttribute(DisplayAttribute, "Channels", "Number of channels to sample from simultaneously.", "Measurements", -50)
        available = self.AddProperty("Available", [1,2,4], List[Int32])
        available.AddAttribute(DisplayAttribute, "Available Values", "PSLab Oscilliscope only allows for 1, 2, or 4 simultaneous channels", "Measurements", -60)

        prop = self.AddProperty("Samples", 0, Int32)
        prop.AddAttribute(DisplayAttribute, "Samples", "Number of samples to fetch. Maximum is 10000 divided by number of channels.", "Measurements", -40)

        prop = self.AddProperty("Timegap", 0.0, Double)
        prop.AddAttribute(DisplayAttribute, "Time Gap", "Time gap between samples in microseconds.", "Measurements", -30)

    # Inherited method from PythonTap TestStep abstract class
    def Run(self):
        self.Oscilloscope.capture(self.Selectable, self.Samples, self.Timegap)
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PrePlanRun(self):
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PostPlanRun(self):
        pass