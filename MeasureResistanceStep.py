from PythonTap import *
from OpenTap import DisplayAttribute

from .PSLabPublisherTestStep import PSLabPublisherTestStep
from .Multimeter import *

@Attribute(DisplayAttribute, "Measure Resistance", "Measures resistance between RES and GND", Groups= ["PSLab", "Multimeter"])
class MeasureResistanceStep(PSLabPublisherTestStep):
    def __init__(self):
        super(MeasureResistanceStep, self).__init__()
        print("Measure resistance test step initialized")

        prop = self.AddProperty("Multimeter", None, Multimeter)
        prop.AddAttribute(DisplayAttribute, "Multimeter", "", "Resources", -100)

    # Inherited method from PythonTap TestStep abstract class
    def Run(self):
        resistance = float(self.Multimeter.measure_resistance())
        print(resistance)
        super(MeasureResistanceStep, self).PublishStepResult("Multimeter", ["Resistance"], [resistance])