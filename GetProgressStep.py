from OpenTap import Display
from opentap import *

from .LogicAnalyzer import *


@attribute(Display("Get Progress", "Publishes the amount of logic events per channel in the buffer",
                   Groups=["PSLab", "Logic Analyzer"]))
class GetProgressStep(TestStep):
    # Properties
    LogicAnalyzer = property(LogicAnalyzer, None) \
        .add_attribute(Display("Logic Analyzer", "", "Resources", 0))

    def __init__(self):
        super(GetProgressStep, self).__init__()

    def Run(self):
        super().Run()  # 3.0: Required for debugging to work.

        progress = self.LogicAnalyzer.get_progress()
        self.PublishResult("Number of events per channel in buffer", ["Event count"], [progress])
