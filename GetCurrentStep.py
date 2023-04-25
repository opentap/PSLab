"""
Test step to get the current on the PCS pin on the PSLab board
"""
from OpenTap import Display, Output, Unit, Verdict
from System import Double
from opentap import *

from .PowerSupply import *


@attribute(Display("Get Current", "Gets current of PCS pin (in A)", Groups=["PSLab", "Power Supply"]))
class GetCurrentStep(TestStep):
    # Properties
    PowerSupply = property(PowerSupply, None) \
        .add_attribute(Display("Power Supply", "", "Resources", 0))

    OutputValue = property(Double, 0.0) \
        .add_attribute(Display("Current ", "Read current", "Output", 99)) \
        .add_attribute(Unit("A")) \
        .add_attribute(Output())

    def __init__(self):
        super(GetCurrentStep, self).__init__()

    def Run(self):
        super().Run()  # 3.0: Required for debugging to work.

        current = float(self.PowerSupply.getPcs())

        self.OutputValue = current
        self.log.Debug(f"Current: {current} A")
        self.PublishResult("PowerSupply", ["Current (A)"], [current])
        self.UpgradeVerdict(Verdict.Pass)
