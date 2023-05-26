"""
Test step to set the current on the PCS pin on the PSLab board
"""

from OpenTap import Display, Unit, Verdict
from System import Double
from opentap import *

from .PowerSupply import *


@attribute(
    Display("Set Current", "Sets pin to a specific current amount", Groups=["PSLab", "Power Supply"]))
class SetCurrentStep(TestStep):
    # Properties
    Current = property(Double, 0) \
        .add_attribute(Display("Current", "The current to be output on the PCS pin", "", -50)) \
        .add_attribute(Unit("A"))

    PowerSupply = property(PowerSupply, None) \
        .add_attribute(Display("Power Supply", "", "Resources", 0))

    def __init__(self):
        super(SetCurrentStep, self).__init__()

        self.Rules.Add(Rule("Current", lambda: self.Current >= 0, lambda: 'Current must not be negative.'))
        self.Rules.Add(Rule("Current", lambda: self.Current <= 3.3e-3, lambda: f'Current must not exceed {3.3e-3} A.'))

    def Run(self):
        self.PowerSupply.setPcs(self.Current)
        self.UpgradeVerdict(Verdict.Pass)
