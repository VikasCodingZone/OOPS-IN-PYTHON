# Q10. Insurance (Health vs Vehicle)
from abc import ABC, abstractmethod

class Insurance(ABC):
    @abstractmethod
    def get_policy(self):
        pass

class HealthInsurance(Insurance):
    def get_policy(self):
        return "Health Insurance Policy"

class VehicleInsurance(Insurance):
    def get_policy(self):
        return "Vehicle Insurance Policy"

i = VehicleInsurance()
print(i.get_policy())



# Q10. Insurance (Health vs Vehicle)
# Common kaam: insurance policy dena.
# Health insurance aur Vehicle insurance ki policy details alag hoti hain.
# Abstraction → user ko sirf get_policy() dikhai deta hai.