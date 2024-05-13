import sys
sys.path.append(r"D:\RUTWIJ DATA\MIT ADT - CSE Notes\HEXAWARE TECHNOLOGIES\Foundational Technical Training\Case Study - Crime Analysis & Reporting System\Crime Reporting System\exception")
from IncidentNumberNotFoundException import IncidentNumberNotFoundException

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='rutwij123',
    port='3306',
    database='crime_analysis_system'
)

mycursor = mydb.cursor()

def check_incident_exists(incident_id):
  sql = "SELECT * FROM incidents WHERE IncidentID = %s"
  val = (incident_id,)
  mycursor.execute(sql, val)
  result = mycursor.fetchone()
  if not result:
    raise IncidentNumberNotFoundException("{}".format(incident_id))

incident_id = int(input("Enter IncidentID: "))

try:
  check_incident_exists(incident_id)

  incident_type = input("Enter IncidentType: ")
  incident_date = input("Enter IncidentDate (YYYY-MM-DD): ")
  latitude = float(input("Enter Latitude: "))
  longitude = float(input("Enter Longitude: "))
  description = input("Enter Description: ")
  status = input("Enter Status: ")
  victim_id = int(input("Enter VictimID: "))
  suspect_id = int(input("Enter SuspectID: "))

  sql = "INSERT INTO incidents (IncidentID, IncidentType, IncidentDate, Latitude, Longitude, Description, Status, VictimID, SuspectID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
  val = (incident_id, incident_type, incident_date, latitude, longitude, description, status, victim_id, suspect_id)

  mycursor.execute(sql, val)
  mydb.commit()

  print(mycursor.rowcount, "Record inserted successfully.")
except IncidentNumberNotFoundException as e:
  print("Error: ", e)
except mysql.connector.Error as err:
  mydb.rollback()
  print("Error inserting data into incidents table:", err)

mydb.close()
