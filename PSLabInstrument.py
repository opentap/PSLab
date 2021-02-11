from PythonTap import *

"""
Wrapper for PSLab Instruments; exposes internal methods for test steps
"""
@Abstract
class PSLabInstrument(Instrument):
    def __init__(self):
        super(PSLabInstrument, self).__init__()

    # Inherited method from PythonTap Instrument abstract class
    def Open(self):
        pass

    # Inherited method from PythonTap Instrument abstract class
    def Close(self):
        pass
