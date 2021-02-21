from PythonTap import *

"""
Wrapper for PSLab Test step that publishes its results
"""
@Abstract
class PSLabPublisherTestStep(TestStep):
    def __init__(self):
        super(PSLabPublisherTestStep, self).__init__()
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

    # Publish results (Triggers publish result listeners)
    def PublishStepResult(self, table_name, column_names, row_values):
        self.PublishResult(table_name, column_names, row_values)
