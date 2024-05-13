import unittest

import sys
sys.path.append(r"D:\RUTWIJ DATA\MIT ADT - CSE Notes\HEXAWARE TECHNOLOGIES\Foundational Technical Training\Case Study - Crime Analysis & Reporting System\Crime Reporting System\dao")
from CrimeAnalysisServiceImpl import CrimeAnalysisServiceImpl

import sys
sys.path.append(r"D:\RUTWIJ DATA\MIT ADT - CSE Notes\HEXAWARE TECHNOLOGIES\Foundational Technical Training\Case Study - Crime Analysis & Reporting System\Crime Reporting System\entity")
from Incidents import Incident


class TestIncidentCreation(unittest.TestCase):
    def setUp(self):
        self.crime_service = CrimeAnalysisServiceImpl()

    def test1(self):
        print("Creating a new incident...")
        incident_data = {
            "incidentID": 1,
            "incidentType": "Robbery",
            "incidentDate": "2024-04-30",
            "latitude": "18.520400",
            "longitude": "73.856700",
            "description": "Robbery at a convenience store",
            "status": "Open",
            "victimID": 1,
            "suspectID": 1
        }
        incident_creation_successful = self.crime_service.create_incident(incident_data)
        self.assertTrue(incident_creation_successful)

        create_incident = self.crime_service.get_incidents_in_date_range("2024-04-01", "2024-05-30")
        if create_incident:
            for incident_dict in create_incident:
                if isinstance(incident_dict, dict):
                    incident = Incident(**incident_dict)
                    self.assertEqual(incident.incidentID, "1")
                    self.assertEqual(incident.incidentType, "Robbery")
                    self.assertEqual(incident.incidentDate, "2024-04-30")
                    self.assertEqual(incident.latitude, "18.520400")
                    self.assertEqual(incident.longitude, "73.856700")
                    self.assertEqual(incident.description, "Robbery at a convenience store")
                    self.assertEqual(incident.status, "Closed")
                    self.assertEqual(incident.victimID, 1)
                    self.assertEqual(incident.suspectID, 1)
                else:
                    print("Unexpected data format retrieved. Test might need adjustment.")

        else:
            print("No incident found in the date range.")

if __name__ == '__main__':
    unittest.main()
