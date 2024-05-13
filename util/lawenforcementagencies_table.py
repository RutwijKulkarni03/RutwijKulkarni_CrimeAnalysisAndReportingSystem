import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='rutwij123',
    port='3306',
    database='crime_analysis_system'
)

mycursor = mydb.cursor()

agency_id = int(input("Enter AgencyID: "))
agency_name = input("Enter AgencyName: ")
jurisdiction = input("Enter Jurisdiction: ")
contact_info = input("Enter Contact Information: ")

sql = "INSERT INTO lawenforcementagencies (AgencyID, AgencyName, Jurisdiction, ContactInformation) VALUES (%s, %s, %s, %s)"
val = (agency_id, agency_name, jurisdiction, contact_info)

try:
    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "Record inserted successfully.")
except mysql.connector.Error as err:
    mydb.rollback()
    print("Error inserting data into lawenforcementagencies table:", err)

mydb.close()
