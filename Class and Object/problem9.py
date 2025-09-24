
9#Class with Conditional Method
class Light:
    def __init__(self, status="off"):
        self.status = status

    def toggle(self):
        if self.status == "off":
            self.status = "on"
        else:
            self.status = "off"
        print(f"Light is {self.status}")

l = Light()
l.toggle()  # Light is on
l.toggle()  # Light is off