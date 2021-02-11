from PythonTap import *

"""
Wrapper for PSLab Test step
"""
@Abstract
class PSLabTestStep(TestStep):
    def __init__(self):
        super(PSLabTestStep, self).__init__()
        print("Test step initialized")

    def setInstrument(instrument):
        self.instrument = instrument

    # Inherited method from PythonTap TestStep abstract class
    def Run(self):
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PrePlanRun(self):
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PostPlanRun(self):
        pass
