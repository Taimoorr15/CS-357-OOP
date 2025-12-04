class smart_device:
    def __init__(self,name,status,place):
        self.name = name
        self.status = status
        self.place = place
    def describe(self):
        return f"I am a {self.name} in {self.place}, and I am currently {'ON' if self.status else 'OFF'}"

    
class light(smart_device):
    def __init__(self,name,status,place):
        super().__init__(name,status,place)
    def dim(self):
        return " Dimming the lights!"
    
class fan(smart_device):
    def __init__(self,name,status,place):
        super().__init__(name,status,place)
    def speed(self):
        return "Your fan is very fast!"
    
class AC(smart_device):
    def __init__(self,name,status,place):
        super().__init__(name,status,place)
    def set_temp(self):
        return "You can set your own temperature"
    
class ceiling_light(light):
    def __init__(self,name,status,place):
        super().__init__(name,status,place)
    def dim(self):
        return "Ceiling light in "+self.place+" is dimming"
    
class table_lamp(light):
    def __init__(self,name,status,place):
        super().__init__(name,status,place)
    def dim(self):
        return "The table lamp in "+self.place+" is dimming"
    
class ceiling_fan(fan):
    def __init__(self,name,status,place):
        super().__init__(name,status,place)
    def speed(self):
        return "The ceiling fan in "+self.place+" is slowing"
    
class exhaust_fan(fan):
    def __init__(self,name,status,place):
        super().__init__(name,status,place)
    def speed(self):
        return "The exhaust fan in "+self.place+" is slowing"
    
class split_AC(AC):
    def __init__(self,name,status,place):
        super().__init__(name,status,place)
    def set_temp(self):
        return "The AC in "+self.place+" is setting temperature"
    
cfan1 = ceiling_fan("Ceiling Fan",True,"Bedroom")
print(cfan1.describe())
print(cfan1.speed())