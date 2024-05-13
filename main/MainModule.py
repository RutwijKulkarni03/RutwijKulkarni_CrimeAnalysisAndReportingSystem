import mysql.connector
import sys
sys.path.append(r"D:\RUTWIJ DATA\MIT ADT - CSE Notes\HEXAWARE TECHNOLOGIES\Foundational Technical Training\Case Study - Crime Analysis & Reporting System\Crime Reporting System\dao")
from ICrimeAnalysisService import ICrimeAnalysisService

import sys
sys.path.append(r"D:\RUTWIJ DATA\MIT ADT - CSE Notes\HEXAWARE TECHNOLOGIES\Foundational Technical Training\Case Study - Crime Analysis & Reporting System\Crime Reporting System\exception")
from IncidentNumberNotFoundException import IncidentNumberNotFoundException

class MainModule(ICrimeAnalysisService):
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='rutwij123',
            port='3306',
            database='crime_analysis_system'
        )
        self.mycursor = self.mydb.cursor()
    def display_menu(self):
            print("\nWelcome To Crime Analysis & Reporting System Menu...")
            print("1. Create Incident")
            print("2. Delete Incident")
            print("3. Update Incident Status")
            print("4. Get Incidents in Date Range")
            print("5. Search Incidents")
            print("6. Generate Incident Report")
            print("7. Create Case")
            print("8. Get Case Details")
            print("9. Update Case Details")
            print("10. Get All Cases")
            print("0. Exit")

    def start_application(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (0-10): ")

            if choice == "1":
                self.create_incident()
            elif choice == "2":
                self.delete_incident()
            elif choice == "3":
                self.update_incident_status()
            elif choice == "4":
                self.get_incidents_in_date_range()
            elif choice == "5":
                self.search_incidents()
            elif choice == "6":
                self.generate_incident_report()
            elif choice == "7":
                self.create_case()
            elif choice == "8":
                self.get_case_details()
            elif choice == "9":
                self.update_case_details()
            elif choice == "10":
                self.get_all_cases()
            elif choice == "0":
                print("Exiting Crime Reporting System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 0 to 10.")

            break

    def create_incident(self):
        print("Creating a new incident...")

        incident_id = input("Enter incident id: ")
        incident_type = input("Enter incident type: ")
        incident_date = input("Enter incident date (YYYY-MM-DD): ")
        latitude = input("Enter Latitude: ")
        longitude = input("Enter Longitude: ")
        description = input("Enter description: ")
        status = input("Enter status: ")
        victim_id = int(input("Enter victim ID: "))
        suspect_id = int(input("Enter suspect ID: "))
        try:
            self.mycursor.execute("""
                            INSERT INTO incidents (IncidentID, IncidentType, IncidentDate, Latitude, Longitude, Description, Status, VictimID, SuspectID)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """, (incident_id, incident_type, incident_date, latitude, longitude, description, status, victim_id, suspect_id))

            self.mydb.commit()
            print("Incident created successfully!")

        except Exception as e:
            print("Failed to create incident. Please try again.", e)

    def delete_incident(self):
        print("Deleting an incident...")

        incident_id = input("Enter the ID of the incident to delete: ")

        try:
            # Check if incident exists before deleting
            sql = "SELECT * FROM incidents WHERE IncidentID = %s"
            self.mycursor.execute(sql, (incident_id,))
            if not self.mycursor.fetchone():
                raise IncidentNumberNotFoundException("{}".format(incident_id))

            confirm = input(f"Are you sure you want to delete incident {incident_id}? (y/n): ")
            if confirm.lower() == 'y':
                sql = """
                    DELETE FROM incidents
                    WHERE IncidentID = %s
                """
                self.mycursor.execute(sql, (incident_id,))
                self.mydb.commit()
                print("Incident deleted successfully!")
            else:
                print("Incident deletion cancelled.")

        except IncidentNumberNotFoundException as e:
            print("Error: ", e)
        except Exception as e:
            print("Failed to delete incident:", e)

    def update_incident_status(self):
        print("Updating incident status...")

        incident_id = input("Enter incident ID: ")

        try:
            sql = "SELECT * FROM incidents WHERE IncidentID = %s"
            self.mycursor.execute(sql, (incident_id,))
            if not self.mycursor.fetchone():
                raise IncidentNumberNotFoundException("Incident with ID {} not found.".format(incident_id))

            new_status = input("Enter new status: ")

            sql = """
                UPDATE incidents
                SET Status = %s
                WHERE IncidentID = %s
            """
            self.mycursor.execute(sql, (new_status, incident_id))
            self.mydb.commit()

            print("Incident status updated successfully!")
        except IncidentNumberNotFoundException as e:
            print("Error: ", e)
        except Exception as e:
            print("Failed to update incident status:", e)

    def get_incidents_in_date_range(self):
        print("Getting incidents within date range...")

        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")

        try:
            sql = """
                SELECT *
                FROM incidents
                WHERE IncidentDate BETWEEN %s AND %s
            """
            self.mycursor.execute(sql, (start_date, end_date))

            incidents = self.mycursor.fetchall()

            if incidents:
                print("Incidents within date range:")
                for incident in incidents:
                    print(incident)
            else:
                print("No incidents found within the specified date range.")
        except Exception as e:
            print("Failed to get incidents within date range:", e)

    def search_incidents(self):
        print("Searching for incidents...")

        incident_type = input("Enter incident type to search for: ")

        try:
            sql = """
                SELECT *
                FROM incidents
                WHERE IncidentType = %s
            """
            self.mycursor.execute(sql, (incident_type,))


            incidents = self.mycursor.fetchall()

            if incidents:
                print("Incidents found based on search criteria:")
                for incident in incidents:
                    print(incident)
            else:
                print("No incidents found based on the specified search criteria.")
        except Exception as e:
            print("Failed to search for incidents:", e)

    def generate_incident_report(self):
        print("Generating incident report...")

        incident_id = input("Enter incident ID to generate report: ")

        try:
            sql = """
                SELECT *
                FROM incidents
                WHERE IncidentID = %s
            """
            self.mycursor.execute(sql, (incident_id,))
            incident = self.mycursor.fetchone()

            if incident:
                print("Incident report generated successfully:")
                print(incident)
            else:
                print("Failed to generate incident report. Please check the incident ID and try again.")
        except Exception as e:
            print("Failed to generate incident report:", e)

    def create_case(self):
        print("Creating a new case...")

        case_description = input("Enter case description: ")
        case_id = input("Enter CaseID: ").split(',')

        try:
            sql = """
                INSERT INTO cases (CaseID, CaseDescription)
                VALUES (%s)
            """
            self.mycursor.execute(sql, (case_id, case_description))

            '''case_id = self.mycursor.lastrowid

            for case_id in case_id:
                sql = """
                    INSERT INTO cases (CaseID, CaseDescription)
                    VALUES (%s, %s)
                """
                self.mycursor.execute(sql, (case_id, case_id))'''

            self.mydb.commit()

            print("Case created successfully!")
        except Exception as e:
            print("Failed to create case:", e)

    def get_case_details(self):
        print("Getting case details...")

        case_id = int(input("Enter case ID: "))

        try:
            sql = """
                SELECT * FROM cases WHERE CaseID = %s
            """
            self.mycursor.execute(sql, (case_id,))

            case_details = self.mycursor.fetchone()

            if case_details:
                print("Case details:")
                print("Case ID:", case_details[0])
                print("Case Description:", case_details[1])
            else:
                print("Case not found. Please check the case ID and try again.")
        except Exception as e:
            print("Failed to get case details:", e)

    def update_case_details(self):
        print("Updating case details...")

        case_id = int(input("Enter case ID: "))
        new_description = input("Enter new case description: ")

        try:
            sql = """
                UPDATE cases SET CaseDescription = %s WHERE CaseID = %s
            """
            self.mycursor.execute(sql, (new_description, case_id))

            self.mydb.commit()

            if self.mycursor.rowcount > 0:
                print("Case details updated successfully!")
            else:
                print("Failed to update case details. Please check the case ID and try again.")
        except Exception as e:
            print("Failed to update case details:", e)

    def get_all_cases(self):
        print("Getting all cases...")

        try:
            sql = "SELECT * FROM cases"

            self.mycursor.execute(sql)

            all_cases = self.mycursor.fetchall()

            if all_cases:
                print("All cases:")
                for case in all_cases:
                    print(case)
            else:
                print("No cases found.")
        except Exception as e:
            print("Failed to get all cases:", e)


if __name__ == "__main__":
    main_module = MainModule()
    main_module.start_application()


