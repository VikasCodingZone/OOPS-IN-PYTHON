# Q20. Smart Home Device (Light vs Fan)
from abc import ABC, abstractmethod


class SmartDevice(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class SmartLight(SmartDevice):
    def turn_on(self):
        return "Light turned ON "

class SmartFan(SmartDevice):
    def turn_on(self):
        return "Fan turned ON "

s = SmartLight()
print(s.turn_on())


# Q20. Smart Home Device (Light vs Fan)
# Common kaam: device turn on karna.
# Lekin device ke type ke hisaab se implementation alag (Light vs Fan).
# Abstraction: sirf turn_on() method dikhai deta hai.