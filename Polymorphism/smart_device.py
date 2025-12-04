class Smart_device:
    def turn_on(self):
        return f"Your device is turning on"
    def turn_off(self):
        return f"You device is stopping"
    
class SmartLight(Smart_device):
    def turn_on(self):
        return f"Light is turning on"
    def turn_off(self):
        return f"Light is turning off"
    
class SmartFan(Smart_device):
    def turn_on(self):
        return f"Fan is turning on"
    def turn_off(self):
        return f"Fan is turning off"
    
class SmartAC(Smart_device):
    def turn_on(self):
        return f"AC is turning on"
    def turn_off(self):
        return f"AC is turning off"

devices = [SmartLight(), SmartFan(), SmartAC()]

for device in devices:
    print(device.turn_on())
    print(device.turn_off())
    print("---")
