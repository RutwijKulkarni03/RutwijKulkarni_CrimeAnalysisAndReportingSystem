import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='rutwij123',
    port='3306',
    database='crime_analysis_system1'
)

mycursor = mydb.cursor()

officer_id = int(input("Enter OfficerID: "))
first_name = input("Enter FirstName: ")
last_name = input("Enter LastName: ")
badge_number = input("Enter BadgeNumber: ")
officer_rank = input("Enter OfficerRank: ")
contact_info = input("Enter Contact Information: ")
agency_id = int(input("Enter AgencyID: "))

sql = "INSERT INTO officers (OfficerID, FirstName, LastName, BadgeNumber, OfficerRank, ContactInformation, AgencyID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = (officer_id, first_name, last_name, badge_number, officer_rank, contact_info, agency_id)

try:
    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "Record inserted successfully.")
except mysql.connector.Error as err:
    mydb.rollback()
    print("Error inserting data into officers table:", err)

mydb.close()
