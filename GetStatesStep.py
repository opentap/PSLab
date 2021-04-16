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

@Attribute(DisplayAttribute, "Get States", "Gets current states of each digital input", Groups= ["PSLab", "Logic Analyzer"])
class GetStatesStep(PSLabPublisherTestStep):
    def __init__(self):
        super(GetStatesStep, self).__init__()
        print("Measure states step initialized")

        prop = self.AddProperty("LogicAnalyzer", None, LogicAnalyzer)
        prop.AddAttribute(DisplayAttribute, "Logic Analyzer", "", "Resources", -100)

    # Inherited method from PythonTap TestStep abstract class
    def Run(self):
        states = self.LogicAnalyzer.get_states()
        states_names = list(states.keys())
        states_values = list(states.values())
        self.Info("pin names: " + ', '.join(states_names))
        self.Info("pin states: " + ', '.join([str(val) for val in states_values]))
        self.PublishStepResult("States", states_names, states_values)
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PrePlanRun(self):
        pass

    # Inherited method from PythonTap TestStep abstract class
    def PostPlanRun(self):
        pass