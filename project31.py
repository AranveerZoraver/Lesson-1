from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def execute_command(self, command):
        pass

class SmartLight(SmartDevice):
    def execute_command(self, command):
        return f"{self.name} light: {command}"

class SmartThermostat(SmartDevice):
    def execute_command(self, command):
        return f"{self.name} thermostat: {command}"

class VoiceAssistant:
    def execute_command(self, command):
        return f"Voice assistant heard: {command}"

devices = [
    SmartLight("Living Room"),
    SmartThermostat("Hallway"),
    VoiceAssistant(),
]

for device in devices:
    print(device.execute_command("turn on"))