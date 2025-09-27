# Q8. File Export (PDF, CSV)
from abc import ABC, abstractmethod

class FileExporter(ABC):
    @abstractmethod
    def export(self, data):
        pass

class PDFExporter(FileExporter):
    def export(self, data):
        return f"Exported {data} as PDF"

class CSVExporter(FileExporter):
    def export(self, data):
        return f"Exported {data} as CSV"

f = PDFExporter()
print(f.export("Report"))


# Q8. File Export (PDF, CSV)
# Same kaam: file export karna.
# Lekin agar PDF hai to ek alag library lagegi, CSV ke liye dusri.
# Abstraction: export(data) → backend alag-alag.