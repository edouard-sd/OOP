from abc import ABC, abstractmethod
import json

class FormatStrategy(ABC):
    @abstractmethod
    def format(self, data: list) -> str:
        pass

class PDFFormatStrategy(FormatStrategy):
    def format(self, data): return "PDF REPORT...\n"

class ExcelFormatStrategy(FormatStrategy):
    def format(self, data): return "EXCEL REPORT...\n"

class CSVFormatStrategy(FormatStrategy):
    def format(self, data): return "CSV REPORT...\n"

class JSONFormatStrategy(FormatStrategy):
    def format(self, data): return json.dumps(data)

class HTMLFormatStrategy(FormatStrategy):
    def format(self, data): return "<html><body>HTML REPORT...</body></html>"

class ReportGenerator:
    def __init__(self, data: list):
        self.data = data
        self.strategy = None

    def set_strategy(self, strategy: FormatStrategy):
        self.strategy = strategy

    def generate_report(self) -> str:
        return self.strategy.format(self.data)

    def save_report(self, filename: str):
        content = self.generate_report()
        with open(filename + ".txt", "w") as f:
            f.write(content)

if __name__ == "__main__":
    data = [{"name": "Sales Q1", "value": 15000}]
    generator = ReportGenerator(data)
    
    generator.set_strategy(PDFFormatStrategy())
    print("=== PDF FORMAT ===\n" + generator.generate_report())
    
    generator.set_strategy(CSVFormatStrategy())
    print("=== CSV FORMAT ===\n" + generator.generate_report())
    
    generator.set_strategy(JSONFormatStrategy())
    print("=== JSON FORMAT ===\n" + generator.generate_report())

    generator.set_strategy(HTMLFormatStrategy())
    print("=== HTML FORMAT (NEW!) ===\n" + generator.generate_report())\n