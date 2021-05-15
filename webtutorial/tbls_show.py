from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host = "localhost",
        user = input("Enter username: "),
        password = getpass("Enter password: "),
        database = "testdb"
    ) as connection:
        show_tables_query = "SHOW TABLES"
        with connection.cursor() as cursor:
            cursor.execute(show_tables_query)
            print("Tables in testdb: ")
            for db in cursor:
                print(db)
except Error as e:
    print(e)
    