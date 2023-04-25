from OpenTap import Display, Output, Unit, Verdict
from System import Double
from opentap import *

from .Multimeter import *


@attribute(Display("Measure Resistance", "Measures resistance between RES and GND (in Ω)",
                   Groups=["PSLab", "Multimeter"]))
class MeasureResistanceStep(TestStep):
    # Properties
    Multimeter = property(Multimeter, None) \
        .add_attribute(Display("Multimeter", "Device used for measurement", "Resources", 0))

    OutputValue = property(Double, 0.0) \
        .add_attribute(Display("Resistance ", "Measured resistance", "Output", 99)) \
        .add_attribute(Unit("Ω")) \
        .add_attribute(Output())

    def __init__(self):
        super(MeasureResistanceStep, self).__init__()

    def Run(self):
        super().Run()  # 3.0: Required for debugging to work.

        resistance = self.Multimeter.measure_resistance()

        self.OutputValue = resistance
        self.log.Debug(f"Resistance: {resistance} Ω")
        self.PublishResult("Multimeter", ["Resistance (Ω)"], [resistance])
        self.UpgradeVerdict(Verdict.Pass)
