import clr
clr.AddReference("System.Collections")
from System.Collections.Generic import List
from System import Int32, Double
from System.ComponentModel import BrowsableAttribute # BrowsableAttribute can be used to hide things from the user.

from PythonTap import *
from OpenTap import DisplayAttribute, UnitAttribute, AvailableValuesAttribute
import math
from .PSLabSetterTestStep import PSLabSetterTestStep
from .PSLabPublisherTestStep import PSLabPublisherTestStep
from .Oscilloscope import *

def calc_rms_sample(frequency, samples_per_period = 32):
    while True:
        periods = 8
        sample_count = periods * samples_per_period
        timegap = int(1/frequency/samples_per_period*1000000.0)
        if timegap > 10000:
            samples_per_period *= 2
        else:
            return sample_count, timegap



@Attribute(DisplayAttribute, "Measure RMS Voltage", "Measures RMS Voltage at a specific Frequency", "PSLab")
class MeasureRMSVoltage(PSLabPublisherTestStep):
    def __init__(self):
        super(MeasureRMSVoltage, self).__init__()

        prop = self.AddProperty("Oscilloscope", None, Oscilloscope)
        prop.AddAttribute(DisplayAttribute, "Oscilloscope", "", "Resources", -100)

        self.AddProperty("Frequency", 500, Double).AddAttribute(UnitAttribute, "Hz")
        self.AddProperty("PreDelay", 0.02, Double).AddAttribute(UnitAttribute, "s")

        channels = self.AddProperty("Channels", 1, Int32)
        channels.AddAttribute(AvailableValuesAttribute, "Available")
        channels.AddAttribute(DisplayAttribute, "Channels", "Number of channels to sample from simultaneously.", "Measurements", -50)
        available = self.AddProperty("Available", [1,2,4], List[Int32])
        available.AddAttribute(BrowsableAttribute, False)


    # Inherited method from PythonTap TestStep abstract class
    def Run(self):

        if self.PreDelay > 0.001:
            OpenTap.TapThread.Sleep(int(self.PreDelay * 1000))

        sampleCount, timegap = calc_rms_sample(self.Frequency)
        x, y = self.Oscilloscope.capture(self.Channels, sampleCount, timegap)
        samples = Array[Double](y)

        sum_samples_i_2 = 0
        for i in samples:
            sum_samples_i_2 += i*i
        rms_amplitude = math.sqrt(sum_samples_i_2/len(samples))        

        self.PublishStepResult("RMS", ["Frequency", "RMS Voltage"], [self.Frequency, rms_amplitude])