import json
from abc import ABC, abstractmethod

class LegacyReportGenerator:
    def generate_report(self, data: dict) -> str:
        xml = "<report>
"
        for key, value in data.items():
            xml += f"  <{key}>{value}</{key}>\n"
        xml += "</report>"
        return xml

class ReportGeneratorInterface(ABC):
    @abstractmethod
    def generate(self, data: dict) -> str:
        pass

class LegacyReportAdapter(ReportGeneratorInterface):
    def __init__(self, legacy_generator: LegacyReportGenerator):
        self.legacy_generator = legacy_generator

    def generate(self, data: dict) -> str:
        _ = self.legacy_generator.generate_report(data)
        return json.dumps(data)

class AnalyticsDashboard:
    def display(self, json_data: str):
        data = json.loads(json_data)
        print("=== Analytics Dashboard ===")
        for key, value in data.items():
            print(f"  {key}: {value}")

if __name__ == "__main__":
    dashboard = AnalyticsDashboard()
    report_generator = LegacyReportAdapter(LegacyReportGenerator())
    json_report = report_generator.generate({"total_sales": 150000, "orders": 1234})
    dashboard.display(json_report)\n