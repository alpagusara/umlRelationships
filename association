class Patient:
    def __init__(self, name: str):
        self.name = name
        self.doctor = None  # Association reference

class Doctor:
    def __init__(self, name: str):
        self.name = name

# The connection is made externally
doctor = Doctor("Dr. Smith")
patient = Patient("John Doe")
patient.doctor = doctor  # Associated but independent lifecycles
