"""
Class to handle multiple connections for multiple instruments
"""

from pslab.serial_handler import SerialHandler

device: SerialHandler = None
connections = 0

class ConnectionHandler: 

    @staticmethod
    def openConnection():
        global connections
        global device
        connections = connections + 1
        if device is None:
            device = SerialHandler()
        return device

    @staticmethod
    def closeConnection():
        global connections
        global device
        if connections > 0: 
            connections -= 1
        else :
            device.disconnect()
            device = None