import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='rutwij123',
    port='3306',
    database='crime_analysis_system'
)

mycursor = mydb.cursor()

evidence_id = int(input("Enter EvidenceID: "))
description = input("Enter Description: ")
location_found = input("Enter Location Found: ")
incident_id = int(input("Enter IncidentID: "))

sql = "INSERT INTO evidence (EvidenceID, Description, LocationFound, IncidentID) VALUES (%s, %s, %s, %s)"
val = (evidence_id, description, location_found, incident_id)

try:
    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "Record inserted successfully.")
except mysql.connector.Error as err:
    mydb.rollback()
    print("Error inserting data into evidence table:", err)

mydb.close()
