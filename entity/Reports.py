class Report:
    def __init__(self, reportID, incidentID, reporting_officer_id, reportDate, reportDetails, reportStatus):
        self.__reportID = reportID
        self.__incidentID = incidentID
        self.__reporting_officer_id = reporting_officer_id
        self.__reportDate = reportDate
        self.__reportDetails = reportDetails
        self.__reportStatus = reportStatus

    def __str__(self):
        return f"Report(ReportID: {self.__reportID}, IncidentID: {self.__incidentID}, ReportingOfficerID: {self.__reporting_officer_id}, Date: {self.__reportDate}, Reporter: {self.__reporterName}, Status: {self.__reportStatus})"
