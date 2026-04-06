from abc import ABC, abstractmethod
import time

class PipelineTemplate(ABC):
    def run(self) -> str:
        self.connect()
        self.extract()
        self.transform()
        self.validate()
        self.load()
        self.cleanup()
        return f"{self.__class__.__name__} finished"

    def connect(self):
        print("Connecting...")

    @abstractmethod
    def extract(self):
        pass

    @abstractmethod
    def transform(self):
        pass

    def validate(self):
        print("Validating data...")

    def load(self):
        print("Loading...")

    def cleanup(self):
        print("Cleaning up resources...")
        self.data = None

class CSVPipeline(PipelineTemplate):
    def __init__(self, source): self.source = source
    def extract(self): print("Extracting CSV...")
    def transform(self): print("Transforming CSV...")

class APIPipeline(PipelineTemplate):
    def __init__(self, source): self.source = source
    def extract(self): print("Extracting API...")
    def transform(self): print("Transforming API...")

class DatabasePipeline(PipelineTemplate):
    def __init__(self, source): self.source = source
    def extract(self): print("Extracting Database...")
    def transform(self): print("Transforming Database...")

class XMLPipeline(PipelineTemplate):
    def __init__(self, source): self.source = source
    def extract(self): print("Extracting XML...")
    def transform(self): print("Transforming XML...")

if __name__ == "__main__":
    csv_pipeline = CSVPipeline("data/users.csv")
    print(f"\n{csv_pipeline.run()}\n")
    
    api_pipeline = APIPipeline("api_url")
    print(f"\n{api_pipeline.run()}\n")

    db_pipeline = DatabasePipeline("postgres")
    print(f"\n{db_pipeline.run()}\n")

    xml_pipeline = XMLPipeline("data.xml")
    print(f"\n{xml_pipeline.run()}\n")\n