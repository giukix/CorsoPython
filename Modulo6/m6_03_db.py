import mysql.connector

DATABASE_CONFIG = {
            'user': 'test',
            'password': 'test',
            'host': 'localhost',
            'database': 'TEST',
            'port': 3306
        }

try:
    connection = mysql.connector.connect(**DATABASE_CONFIG)
    cursor = connection.cursor()
    chiave = "100"
    descrizione = "una descrizione"
    cursor.execute("""
        SELECT CHIAVE, DESCRIZIONE FROM TEST_TABLE
        WHERE chiave <> %s AND descrizione <> %s
    """, (chiave, descrizione))
    result = cursor.fetchall()
    for myrow in result:
        print(myrow)
except mysql.connector.Error as error:
    print(error)
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals():
        connection.close()
