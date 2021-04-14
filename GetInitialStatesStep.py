import clr
clr.AddReference("System.Collections")
from System.Collections.Generic import List
from System import Int32, Double, Boolean, String
from System.ComponentModel import BrowsableAttribute # BrowsableAttribute can be used to hide things from the user.

from PythonTap import *
from OpenTap import DisplayAttribute, UnitAttribute, AvailableValuesAttribute

from .PSLabSetterTestStep import PSLabSetterTestStep
from .PSLabPublisherTestStep import PSLabPublisherTestStep
from .LogicAnalyzer import *

@Attribute(DisplayAttribute, "Get Initial States", "Gets initial states for each digital input at start of capture", Groups= ["PSLab", "Logic Analyzer"])
class GetInitialStatesStep(PSLabPublisherTestStep):
    def __init__(self):
        super(GetInitialStatesStep, self).__init__()
        print("Measure interval test step initialized")

        prop = self.AddProperty("LogicAnalyzer", None, LogicAnalyzer)
        prop.AddAttribute(DisplayAttribute, "Logic Analyzer", "", "Resources", -100)

    # Inherited method from PythonTap TestStep abstract class
    def Run(self):
        initial_states = self.LogicAnalyzer.get_initial_states()
        initial_states_names = list(initial_states.keys())
        initial_states_values = list(initial_states.values())
        self.Info("initial states: " + ', '.join(initial_states_names))
        self.Info("initial values: " + ', '.join([str(val) for val in initial_states_values]))
        self.PublishStepResult("Initial States", initial_states_names, initial_states_values)
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PrePlanRun(self):
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PostPlanRun(self):
        pass