import mysql.connector

def connect_to_mysql(host='localhost', user='root', password='rutwij123', port=3306, database='courier_management_system'):
    """Connects to the MySQL database securely."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='rutwij123',
            port=3306,
            database='crime_analysis_system'
        )
        print("Connected to the database successfully.")
        return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

connect_to_mysql()
