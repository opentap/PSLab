from OpenTap import Display, Verdict
from opentap import *

from .LogicAnalyzer import *


@attribute(
    Display("Get Initial States", "Gets initial states for each digital input at start of capture",
            Groups=["PSLab", "Logic Analyzer"]))
class GetInitialStatesStep(TestStep):
    # Properties
    LogicAnalyzer = property(LogicAnalyzer, None) \
        .add_attribute(Display("Logic Analyzer", "", "Resources", 0))

    def __init__(self):
        super(GetInitialStatesStep, self).__init__()

    def Run(self):
        super().Run()  # 3.0: Required for debugging to work.

        initial_states = self.LogicAnalyzer.get_initial_states()
        initial_states_names = list(initial_states.keys())
        initial_states_values = list(initial_states.values())
        self.log.Debug("initial states: " + ', '.join(initial_states_names))
        self.log.Debug("initial values: " + ', '.join([str(val) for val in initial_states_values]))
        self.PublishResult("Initial States", initial_states_names, initial_states_values)
        self.UpgradeVerdict(Verdict.Pass)
