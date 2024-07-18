import mysql.connector
import pandas as pd

#function to check if the modifications to the academic world db have been created already
def initialize_database(dbuser, dbpassword, dbport):
    cxn = mysql.connector.connect(user=dbuser, password=dbpassword, host = dbport, database = 'academicworld')
    cursor = cxn.cursor()

    cursor.execute("SHOW TABLES")
    result = cursor.fetchall()
    
    if "user_interests" not in [table[0] for table in result]:
        createTableQuery = """ CREATE TABLE user_interests (
        id INT NOT NULL,
        name VARCHAR(256) NOT NULL,
        PRIMARY KEY (id));
        """
        cursor.execute(createTableQuery)
    cursor.close()

if __name__ == "__main__":
    initialize_database("root", "root_user", "127.0.0.1")
