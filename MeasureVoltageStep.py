from PythonTap import *
from OpenTap import DisplayAttribute
from System import String
from System.Collections.Generic import List
from System.ComponentModel import BrowsableAttribute

from .PSLabPublisherTestStep import PSLabPublisherTestStep
from .Multimeter import *

@Attribute(DisplayAttribute, "Measure Voltage", "Measures voltage on pin", Groups= ["PSLab", "Multimeter"])
class MeasureVoltageStep(PSLabPublisherTestStep):
    def __init__(self):
        super(MeasureVoltageStep, self).__init__()
        print("Measure resistance test step initialized")

        prop = self.AddProperty("Multimeter", None, Multimeter)
        prop.AddAttribute(DisplayAttribute, "Multimeter", "", "Resources", -100)

        selectable = self.AddProperty("Channel", "VOL", String)
        selectable.AddAttribute(AvailableValuesAttribute, "Available")
        selectable.AddAttribute(DisplayAttribute, "Channel", "Channel to measure voltage from", "Measurements", -50)
        available = self.AddProperty("Available", ["CH1", "CH2", "CH3", "MIC", "CAP", "RES", "VOL"], List[String])
        available.AddAttribute(BrowsableAttribute, False)

    # Inherited method from PythonTap TestStep abstract class
    def Run(self):
        voltage = float(self.Multimeter.measure_voltage(self.Channel))
        print(voltage)
        super(MeasureVoltageStep, self).PublishStepResult("Multimeter", ["Voltage"], [voltage])