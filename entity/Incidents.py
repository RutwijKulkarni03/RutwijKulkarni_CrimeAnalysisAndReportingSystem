class Incident:
    def __init__(self, incidentID, incidentType, incidentDate, latitude, longitude, description, status, victimID, suspectID):
        self.__incidentID = incidentID
        self.__incidentType = incidentType
        self.__incidentDate = incidentDate
        self.__latitude = latitude
        self.__longitude = longitude
        self.__description = description
        self.__status = status
        self.__victimID = victimID
        self.__suspectID = suspectID

    def __str__(self):
        return f"Incident(ID: {self.__incidentID}, Type: {self.__incidentType}, Date: {self.__incidentDate}, Status: {self.__status})"
