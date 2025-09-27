# Q12. Printer (Inkjet vs Laser)

from abc import ABC, abstractmethod
class Printer(ABC):
    @abstractmethod
    def print_file(self, file):
        pass

class InkjetPrinter(Printer):
    def print_file(self, file):
        return f"Inkjet printing {file}"

class LaserPrinter(Printer):
    def print_file(self, file):
        return f"Laser printing {file}"

p = LaserPrinter()
print(p.print_file("Document.pdf"))


# Q12. Printer (Inkjet vs Laser)
# Printer ka kaam: print_file(file).
# Inkjet aur Laser printing ki technology alag hoti hai.
# User ko detail nahi pata chalti, wo bas print_file() use karta hai.