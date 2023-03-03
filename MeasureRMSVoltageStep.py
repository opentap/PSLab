import math

from OpenTap import AvailableValues, Display, TapThread, Unit
from System import Double, String
from System.Collections.Generic import List
from opentap import *

from .Oscilloscope import *


def calc_rms_sample(frequency, samples_per_period=32):
    while True:
        periods = 8
        sample_count = periods * samples_per_period
        timegap = int(1 / frequency / samples_per_period * 1000000.0)
        if timegap > 10000:
            samples_per_period *= 2
        else:
            return sample_count, timegap


@attribute(Display("Measure RMS Voltage", "Measures RMS Voltage at a specific Frequency (in V)",
                   Groups=["PSLab", "Oscilloscope"]))
class MeasureRMSVoltage(TestStep):
    # Properties
    Channel = property(String, "CH1") \
        .add_attribute(AvailableValues("Available")) \
        .add_attribute(Display("Channel", "Channel to measure voltage from", "Measurements", -50))

    Frequency = property(Double, 500) \
        .add_attribute(Display("Frequency", "Frequency of the sampling",
                               "Measurements", -40)) \
        .add_attribute(Unit("Hz"))

    PreDelay = property(Double, 0.02) \
        .add_attribute(Display("PreDelay", "Time to wait before measurement",
                               "Measurements", -30)) \
        .add_attribute(Unit("s"))

    Oscilloscope = property(Oscilloscope, None) \
        .add_attribute(Display("Oscilloscope", "", "Resources", 0))

    @property(List[String])
    @attribute(Browsable(False))  # property not visible for the user.
    def Available(self):
        available = List[String]()
        available.Add("CH1")
        available.Add("CH2")
        available.Add("CH3")
        available.Add("MIC")
        available.Add("CAP")
        available.Add("RES")
        available.Add("VOL")
        return available

    def __init__(self):
        super(MeasureRMSVoltage, self).__init__()

    def Run(self):
        super().Run()  # 3.0: Required for debugging to work.

        if self.PreDelay > 0.001:
            TapThread.Sleep(int(self.PreDelay * 1000))

        sample_count, timegap = calc_rms_sample(self.Frequency)
        timestamps, voltages = self.Oscilloscope.capture(self.Channel, sample_count, timegap)

        sum_samples_i_2 = 0
        for i in voltages:
            sum_samples_i_2 += i * i
        rms_amplitude = math.sqrt(sum_samples_i_2 / len(voltages))
        self.PublishResult("RMS", ["Frequency", "RMS Voltage (V)"], [self.Frequency, rms_amplitude])
