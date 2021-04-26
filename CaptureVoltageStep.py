import clr
clr.AddReference("System.Collections")
from System.Collections.Generic import List
from System import Int32, Double
from System.ComponentModel import BrowsableAttribute # BrowsableAttribute can be used to hide things from the user.

from PythonTap import *
from OpenTap import DisplayAttribute, UnitAttribute, AvailableValuesAttribute

from .PSLabSetterTestStep import PSLabSetterTestStep
from .PSLabPublisherTestStep import PSLabPublisherTestStep
from .Oscilloscope import *

@Attribute(DisplayAttribute, "Capture Voltage", "Captures varying voltages using Oscilloscope", Groups= ["PSLab", "Oscilloscope"])
class CaptureVoltageStep(PSLabPublisherTestStep):
    def __init__(self):
        super(CaptureVoltageStep, self).__init__()
        print("Capture test step initialized")

        prop = self.AddProperty("Oscilloscope", None, Oscilloscope)
        prop.AddAttribute(DisplayAttribute, "Oscilloscope", "", "Resources", -100)

        selectable = self.AddProperty("Channels", 1, Int32)
        selectable.AddAttribute(AvailableValuesAttribute, "Available")
        selectable.AddAttribute(DisplayAttribute, "Channels", "Number of channels to sample from simultaneously.", "Measurements", -50)
        available = self.AddProperty("Available", [1,2,4], List[Int32])
        available.AddAttribute(BrowsableAttribute, False)

        prop = self.AddProperty("Samples", 200, Int32)
        prop.AddAttribute(DisplayAttribute, "Samples", "Number of samples to fetch. Maximum is 10000 divided by number of channels.", "Measurements", -40)

        prop = self.AddProperty("Timegap", 10.0, Double)
        prop.AddAttribute(DisplayAttribute, "Time Gap", "Time gap between samples in microseconds.", "Measurements", -30)

    # Inherited method from PythonTap TestStep abstract class
    def Run(self):
        results = self.Oscilloscope.capture(self.Channels, self.Samples, self.Timegap)

        time = results[0].tolist()
        channel1 = results[1].tolist()
        if len(results) == 2:
            for i in range(0, len(time)):
                self.PublishStepResult("Oscilloscope Results", ["Time", "Voltage"], [time[i], channel1[i]])
        elif len(results) == 3:
            channel2 = results[1].tolist()
            for i in range(0, len(time)):
                self.PublishStepResult("Oscilloscope Results", ["Time", "Voltage 1", "Voltage 2"], [time[i], channel1[i], channel2[i]])
        elif len(results) == 5:
            channel2 = results[1].tolist()
            channel3 = results[1].tolist()
            channel4 = results[1].tolist()
            for i in range(0, len(time)):
                self.PublishStepResult("Oscilloscope Results", ["Time", "Voltage 1", "Voltage 2", "Voltage 3", "Voltage 4"], [time[i], channel1[i], channel2[i], channel3[i], channel4[i]])
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PrePlanRun(self):
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PostPlanRun(self):
        pass