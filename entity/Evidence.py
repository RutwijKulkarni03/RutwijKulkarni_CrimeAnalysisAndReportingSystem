class Evidence:
    def __init__(self, evidenceID, description, location_found, incident_id):
        self.__evidenceID = evidenceID
        self.__description = description
        self.__location_found = location_found
        self.__incident_id = incident_id


    def __str__(self):
        return f"Evidence(ID: {self.__evidenceID}, Description: {self.__description}, LocationFound: {self.__location_found}, Incident_ID: {self.__Incident})"
