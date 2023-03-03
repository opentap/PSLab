from OpenTap import Display
from opentap import *

from .Multimeter import *


@attribute(Display("Measure Resistance", "Measures resistance between RES and GND (in Ω)",
                   Groups=["PSLab", "Multimeter"]))
class MeasureResistanceStep(TestStep):
    # Properties
    Multimeter = property(Multimeter, None) \
        .add_attribute(Display("Multimeter", "", "Resources", 0))

    def __init__(self):
        super(MeasureResistanceStep, self).__init__()

    def Run(self):
        super().Run()  # 3.0: Required for debugging to work.

        resistance = self.Multimeter.measure_resistance()
        print(resistance)
        self.PublishResult("Multimeter", ["Resistance (Ω)"], [resistance])
