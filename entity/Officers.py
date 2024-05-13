class Officer:
    def __init__(self, officerID, firstName, lastName, badgeNumber, officerRank, contactInformation, agencyID):
        self.__officerID = officerID
        self.__firstName = firstName
        self.__lastName = lastName
        self.__badgeNumber = badgeNumber
        self.__officerRank = officerRank
        self.__contactInformation = contactInformation
        self.__agencyID = agencyID


    def __str__(self):
        return f"Officer(OfficerID: {self.__officerID}, Name: {self.__firstName} {self.__lastName}, BadgeNumber: {self.__badgeNumber}, Rank: {self.__officerRank}, AgencyID: {self.__agencyID})"
