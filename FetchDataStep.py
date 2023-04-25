from OpenTap import Display, Verdict
from opentap import *

from .LogicAnalyzer import *


@attribute(
    Display("Fetch Data", "Publishes the captured logic events", Groups=["PSLab", "Logic Analyzer"]))
class FetchDataStep(TestStep):
    # Properties
    LogicAnalyzer = property(LogicAnalyzer, None) \
        .add_attribute(Display("Logic Analyzer", "", "Resources", 0))

    def __init__(self):
        super(FetchDataStep, self).__init__()

    def Run(self):
        super().Run()  # 3.0: Required for debugging to work.

        data = self.LogicAnalyzer.fetch_data()
        channels = [str(i + 1) for i in range(len(data))]
        for i in range(len(data[0])):
            self.PublishResult("Captured Data", channels, [data[channel][i] for channel in range(len(data))])

        self.UpgradeVerdict(Verdict.Pass)
