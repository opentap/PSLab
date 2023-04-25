from OpenTap import Display, Verdict
from opentap import *

from .LogicAnalyzer import *


@attribute(
    Display("Get States", "Gets current states of each digital input", Groups=["PSLab", "Logic Analyzer"]))
class GetStatesStep(TestStep):
    # Properties
    LogicAnalyzer = property(LogicAnalyzer, None) \
        .add_attribute(Display("Logic Analyzer", "", "Resources", 0))

    def __init__(self):
        super(GetStatesStep, self).__init__()

    def Run(self):
        super().Run()  # 3.0: Required for debugging to work.

        states = self.LogicAnalyzer.get_states()
        states_names = list(states.keys())
        states_values = list(states.values())
        self.log.Debug("pin names: " + ', '.join(states_names))
        self.log.Debug("pin states: " + ', '.join([str(val) for val in states_values]))
        self.PublishResult("States", states_names, states_values)
        self.UpgradeVerdict(Verdict.Pass)
