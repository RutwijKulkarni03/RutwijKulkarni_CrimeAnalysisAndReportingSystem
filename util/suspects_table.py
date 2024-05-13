import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='rutwij123',
    port='3306',
    database='crime_analysis_system'
)

mycursor = mydb.cursor()

suspect_id = int(input("Enter SuspectID: "))
first_name = input("Enter FirstName: ")
last_name = input("Enter LastName: ")
date_of_birth = input("Enter DateOfBirth (YYYY-MM-DD): ")
gender = input("Enter Gender: ")
contact_info = input("Enter Contact Information: ")

sql = "INSERT INTO suspects (SuspectID, FirstName, LastName, DateOfBirth, Gender, ContactInformation) VALUES (%s, %s, %s, %s, %s, %s)"
val = (suspect_id, first_name, last_name, date_of_birth, gender, contact_info)

try:
    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "Record inserted successfully.")
except mysql.connector.Error as err:

    mydb.rollback()
    print("Error inserting data into suspects table:", err)

mydb.close()
