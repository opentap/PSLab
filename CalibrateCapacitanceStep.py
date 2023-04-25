from OpenTap import Display, Verdict
from opentap import *

from .Multimeter import *


@attribute(
    Display("Calibrate Capacitance", "Calibrates stray capacitance", Groups=["PSLab", "Multimeter"]))
class CalibrateCapacitanceStep(TestStep):
    # Properties
    Multimeter = property(Multimeter, None) \
        .add_attribute(Display("Multimeter", "", "Resources", 0))

    def __init__(self):
        super(CalibrateCapacitanceStep, self).__init__()

    def Run(self):
        super().Run()  # 3.0: Required for debugging to work.

        self.Multimeter.calibrate_capacitance()
        self.UpgradeVerdict(Verdict.Pass)
