class LawEnforcement:
    def __init__(self, agencyID, agencyName, jurisdiction, contactInformation):
        self.__agencyID = agencyID
        self.__agencyName = agencyName
        self.__jurisdiction = jurisdiction
        self.__contactInformation = contactInformation


    def __str__(self):
        return f"LawEnforcement(AgencyID: {self.__agencyID}, AgencyName: {self.__agencyName}, Jurisdiction: {self.__jurisdiction}, ContactInfo: {self.__contactInformation})"
