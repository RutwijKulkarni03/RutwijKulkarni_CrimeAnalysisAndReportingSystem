import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='rutwij123',
    port='3306',
    database='crime_analysis_system'
)

mycursor = mydb.cursor()

report_id = int(input("Enter ReportID: "))
incident_id = int(input("Enter IncidentID: "))
reporting_officer_id = int(input("Enter ReportingOfficerID: "))
report_date = input("Enter ReportDate (YYYY-MM-DD): ")
report_details = input("Enter ReportDetails: ")
status = input("Enter Status: ")

sql = "INSERT INTO reports (ReportID, IncidentID, ReportingOfficerID, ReportDate, ReportDetails, Status) VALUES (%s, %s, %s, %s, %s, %s)"
val = (report_id, incident_id, reporting_officer_id, report_date, report_details, status)

try:
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "Record inserted successfully.")
except mysql.connector.Error as err:
    mydb.rollback()
    print("Error inserting data into reports table:", err)

mydb.close()
