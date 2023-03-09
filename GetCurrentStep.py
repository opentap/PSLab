"""
Test step to get the current on the PCS pin on the PSLab board
"""
from OpenTap import Display
from opentap import *

from .PowerSupply import *


@attribute(Display("Get Current", "Gets current of PCS pin (in A)", Groups=["PSLab", "Power Supply"]))
class GetCurrentStep(TestStep):
    # Properties
    PowerSupply = property(PowerSupply, None) \
        .add_attribute(Display("Power Supply", "", "Resources", 0))

    def __init__(self):
        super(GetCurrentStep, self).__init__()

    def Run(self):
        super().Run()  # 3.0: Required for debugging to work.

        current = float(self.PowerSupply.getPcs())
        self.PublishResult("PowerSupply", ["Current (A)"], [current])
