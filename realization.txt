# The Interface (Abstract Base Class)
class Printable(ABC):
    @abstractmethod
    def print_details(self) -> None:
        pass

# PDFReport realizes Printable by implementing the abstract method
class PDFReport(Printable):
    def print_details(self) -> None:
        print("Printing PDF report structure...")
