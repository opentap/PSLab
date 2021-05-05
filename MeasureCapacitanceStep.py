from PythonTap import *
from OpenTap import DisplayAttribute

from .PSLabPublisherTestStep import PSLabPublisherTestStep
from .Multimeter import *

@Attribute(DisplayAttribute, "Measure Capacitance", "Measures capacitor connected between CAP and GND", Groups= ["PSLab", "Multimeter"])
class MeasureCapacitanceStep(PSLabPublisherTestStep):
    def __init__(self):
        super(MeasureCapacitanceStep, self).__init__()
        print("Measure resistance test step initialized")

        prop = self.AddProperty("Multimeter", None, Multimeter)
        prop.AddAttribute(DisplayAttribute, "Multimeter", "", "Resources", -100)

    # Inherited method from PythonTap TestStep abstract class
    def Run(self):
        capacitance = float(self.Multimeter.measure_capacitance())
        print(capacitance)
        super(MeasureCapacitanceStep, self).PublishStepResult("Multimeter", ["Capacitance"], [capacitance])