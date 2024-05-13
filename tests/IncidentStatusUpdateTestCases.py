import unittest
import mysql.connector

import sys
sys.path.append(r"D:\RUTWIJ DATA\MIT ADT - CSE Notes\HEXAWARE TECHNOLOGIES\Foundational Technical Training\Case Study - Crime Analysis & Reporting System\Crime Reporting System\dao")
from CrimeAnalysisServiceImpl import CrimeAnalysisServiceImpl

import sys
sys.path.append(r"D:\RUTWIJ DATA\MIT ADT - CSE Notes\HEXAWARE TECHNOLOGIES\Foundational Technical Training\Case Study - Crime Analysis & Reporting System\Crime Reporting System\entity")
from Incidents import Incident


class TestIncidentCreation(unittest.TestCase):
    def setUp(self):
        self.crime_service = CrimeAnalysisServiceImpl()

    def test2(self):
        print("Updating incident status...")
        incident_id = 1
        new_status = "Closed"

        self.crime_service.establish_connection()

        result = self.crime_service.update_incident_status(incident_id, new_status)
        self.assertTrue(result)

        updated_incident = self.crime_service.get_incident_by_id(incident_id)
        if updated_incident is None:
            print("Incident not found after update!")
        else:
            self.assertEqual(updated_incident.status, new_status)

    def tearDown(self):
        self.crime_service.close_connection()

if __name__ == '__main__':
    unittest.main()