class IncidentNumberNotFoundException(Exception):

    def __init__(self, incident_number):
        super().__init__(f"Incident number '{incident_number}' not found in the database.")
        self.incident_number = incident_number
