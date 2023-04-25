from OpenTap import Display, Output, Unit, Verdict
from System import Double
from opentap import *

from .Multimeter import *


@attribute(Display("Measure Capacitance", "Measures capacitance connected between CAP and GND (in F)",
                   Groups=["PSLab", "Multimeter"]))
class MeasureCapacitanceStep(TestStep):
    # Properties
    Multimeter = property(Multimeter, None) \
        .add_attribute(Display("Multimeter", "", "Resources", 0))

    OutputValue = property(Double, 0.0) \
        .add_attribute(Display("Capacitance ", "Measured capacitance", "Output", 99)) \
        .add_attribute(Unit("F")) \
        .add_attribute(Output())

    def __init__(self):
        super(MeasureCapacitanceStep, self).__init__()

    def Run(self):
        super().Run()  # 3.0: Required for debugging to work.

        capacitance = float(self.Multimeter.measure_capacitance())

        self.OutputValue = capacitance
        self.log.Debug(f"Capacitance: {capacitance} F")
        self.PublishResult("Multimeter", ["Capacitance (F)"], [capacitance])
        self.UpgradeVerdict(Verdict.Pass)
