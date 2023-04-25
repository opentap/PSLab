from OpenTap import Display, Output, Verdict
from System import Int32
from opentap import *

from .LogicAnalyzer import *


@attribute(Display("Get Progress", "Publishes the amount of logic events per channel in the buffer",
                   Groups=["PSLab", "Logic Analyzer"]))
class GetProgressStep(TestStep):
    # Properties
    LogicAnalyzer = property(LogicAnalyzer, None) \
        .add_attribute(Display("Logic Analyzer", "", "Resources", 0))

    OutputValue = property(Int32, 0) \
        .add_attribute(Display("Progress ", "Number of events", "Output", 99)) \
        .add_attribute(Output())

    def __init__(self):
        super(GetProgressStep, self).__init__()

    def Run(self):
        super().Run()  # 3.0: Required for debugging to work.

        progress = self.LogicAnalyzer.get_progress()

        self.OutputValue = progress
        self.log.Debug(f"Progress: {progress}")
        self.PublishResult("Number of events per channel in buffer", ["Event count"], [progress])
        self.UpgradeVerdict(Verdict.Pass)
