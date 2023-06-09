"""
Class to handle multiple connections for multiple instruments
"""
import threading

from pslab import ScienceLab
from pslab.instrument.logic_analyzer import LogicAnalyzer
from pslab.instrument.multimeter import Multimeter
from pslab.instrument.oscilloscope import Oscilloscope
from pslab.instrument.power_supply import PowerSupply
from pslab.instrument.waveform_generator import PWMGenerator
from pslab.instrument.waveform_generator import WaveformGenerator

_lock = threading.Lock()


class ConnectionHandler(object):
    _instance = None
    _device = None

    def __init__(self):
        raise RuntimeError("ConnectionHandler is a singleton class. Call instance() instead")

    def __getScienceLab(self) -> ScienceLab:
        with _lock:
            self._device = ScienceLab() if self._device is None else self._device
            return self._device

    @classmethod
    def instance(cls):
        with _lock:
            if cls._instance is None:
                cls._instance = cls.__new__(cls)
                cls._instance._lock = threading.Lock()
            return cls._instance

    def getOscilloscope(self) -> Oscilloscope:
        return self.__getScienceLab().oscilloscope

    def getWaveformGenerator(self) -> WaveformGenerator:
        return self.__getScienceLab().waveform_generator

    def getPWMGenerator(self) -> PWMGenerator:
        return self.__getScienceLab().pwm_generator

    def getPowerSupply(self) -> PowerSupply:
        return self.__getScienceLab().power_supply

    def getLogicAnalyzer(self) -> LogicAnalyzer:
        return self.__getScienceLab().logic_analyzer

    def getMultimeter(self) -> Multimeter:
        return self.__getScienceLab().multimeter
