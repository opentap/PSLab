from OpenTap import Display
from opentap import *

from .LogicAnalyzer import *


@attribute(
    Display("Stop Capture", "Stops the capture method if it's running", Groups=["PSLab", "Logic Analyzer"]))
class StopCaptureStep(TestStep):
    # Properties
    LogicAnalyzer = property(LogicAnalyzer, None) \
        .add_attribute(Display("Logic Analyzer", "", "Resources", 0))

    def __init__(self):
        super(StopCaptureStep, self).__init__()

    def Run(self):
        self.LogicAnalyzer.stop()
