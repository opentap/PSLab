from OpenTap import Display
from opentap import *

from .Multimeter import *


@attribute(Display("Measure Capacitance", "Measures capacitance connected between CAP and GND (in F)",
                   Groups=["PSLab", "Multimeter"]))
class MeasureCapacitanceStep(TestStep):
    # Properties
    Multimeter = property(Multimeter, None) \
        .add_attribute(Display("Multimeter", "", "Resources", 0))

    def __init__(self):
        super(MeasureCapacitanceStep, self).__init__()

    def Run(self):
        super().Run()  # 3.0: Required for debugging to work.

        capacitance = float(self.Multimeter.measure_capacitance())
        print(capacitance)
        self.PublishResult("Multimeter", ["Capacitance (F)"], [capacitance])
