from ICrimeAnalysisService import ICrimeAnalysisService
from DBConnection import DBConnection
import mysql.connector

class CrimeAnalysisServiceImpl(ICrimeAnalysisService):

    def __init__(self):
        self.connection = DBConnection.get_connection()

    def create_incident(self, incidentid):
        incident_creation_successful = True

        if incident_creation_successful:
            return True
        else:
            return False

    def update_incident_status(self, incident_id, new_status):
        try:
            connection = self.connection

            sql = """
                UPDATE incidents
                SET status = %s
                WHERE incidentID = %s
            """

            cursor = connection.cursor()

            cursor.execute(sql, (new_status, incident_id))

            connection.commit()

            return True

        except Exception as e:
            print(f"Error updating incident status: {e}")
            return False

        finally:
            if connection:
                connection.close()

    def get_incidents_in_date_range(self, start_date, end_date):
        print("Getting incidents within date range...")

        try:
            sql = """
                SELECT *
                FROM incidents
                WHERE IncidentDate BETWEEN %s AND %s
                ORDER BY incidentID DESC
            """
            connection = self.connection
            cursor = connection.cursor()
            cursor.execute(sql, (start_date, end_date))

            incidents = cursor.fetchall()

            if incidents:
                return incidents
            else:
                return None
        except Exception as e:
            print("Failed to get incidents within date range:", e)
            return None

    def search_incidents(self):
        pass

    def generate_incident_report(self):
        pass

    def create_case(self):
        pass

    def get_case_details(self):
        pass

    def update_case_details(self):
        pass

    def get_all_cases(self):
        pass

    def get_incident_by_id(self, incident_id):
        query = "SELECT * FROM Incidents WHERE incidentID = %s"
        params = (incident_id,)
        connection = self.connection
        cursor = connection.cursor()
        cursor.execute(query, params)
        incident = cursor.fetchone()
        cursor.close()
        return incident

    def establish_connection(self):
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='rutwij123',
            port='3306',
            database='crime_analysis_system'
        )

    def close_connection(self):
        if self.connection:
            self.connection.close()
