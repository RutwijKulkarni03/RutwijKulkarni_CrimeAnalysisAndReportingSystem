from abc import ABC, abstractmethod
from typing import List, Collection

import sys
sys.path.append(r"D:\RUTWIJ DATA\MIT ADT - CSE Notes\HEXAWARE TECHNOLOGIES\Foundational Technical Training\Case Study - Crime Analysis & Reporting System\Crime Reporting System\entity")
from Incidents import Incident

import sys
sys.path.append(r"D:\RUTWIJ DATA\MIT ADT - CSE Notes\HEXAWARE TECHNOLOGIES\Foundational Technical Training\Case Study - Crime Analysis & Reporting System\Crime Reporting System\entity")
from Cases import Case

import sys
sys.path.append(r"D:\RUTWIJ DATA\MIT ADT - CSE Notes\HEXAWARE TECHNOLOGIES\Foundational Technical Training\Case Study - Crime Analysis & Reporting System\Crime Reporting System\entity")
from Reports import Report

class ICrimeAnalysisService(ABC):
    @abstractmethod
    def create_incident(self):
        pass

    @abstractmethod
    def update_incident_status(self):
        pass

    @abstractmethod
    def get_incidents_in_date_range(self):
        pass

    @abstractmethod
    def search_incidents(self):
        pass

    @abstractmethod
    def generate_incident_report(self):
        pass

    @abstractmethod
    def create_case(self):
        pass

    @abstractmethod
    def get_case_details(self):
        pass

    @abstractmethod
    def update_case_details(self):
        pass

    @abstractmethod
    def get_all_cases(self):
        pass
