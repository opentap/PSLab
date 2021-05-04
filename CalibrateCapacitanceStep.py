from PythonTap import *
from OpenTap import DisplayAttribute

from .PSLabSetterTestStep import PSLabSetterTestStep
from .Multimeter import *

@Attribute(DisplayAttribute, "Calibrate Capacitance", "Calibrates stray capacitance", Groups= ["PSLab", "Multimeter"])
class CalibrateCapacitanceStep(PSLabSetterTestStep):
    def __init__(self):
        super(CalibrateCapacitanceStep, self).__init__()
        print("Calibrate Capacitance test step initialized")

        prop = self.AddProperty("Multimeter", None, Multimeter)
        prop.AddAttribute(DisplayAttribute, "Multimeter", "", "Resources", -100)

    # Inherited method from PythonTap TestStep abstract class
    def Run(self):
        self.Multimeter.calibrate_capacitance()