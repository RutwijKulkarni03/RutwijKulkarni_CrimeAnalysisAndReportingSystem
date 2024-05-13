import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='rutwij123',
    port='3306',
    database='crime_analysis_system'
)

mycursor = mydb.cursor()

victim_id = int(input("Enter VictimID: "))
first_name = input("Enter FirstName: ")
last_name = input("Enter LastName: ")
date_of_birth = input("Enter DateOfBirth (YYYY-MM-DD): ")
gender = input("Enter Gender: ")
address = input("Enter Address: ")
phone_number = input("Enter Phone Number: ")

sql = "INSERT INTO victims (VictimID, FirstName, LastName, DateOfBirth, Gender, Address, PhoneNumber) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = (victim_id, first_name, last_name, date_of_birth, gender, address, phone_number)

try:
    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "Record inserted successfully.")
except mysql.connector.Error as err:
    mydb.rollback()
    print("Error inserting data into victims table:", err)

mydb.close()
