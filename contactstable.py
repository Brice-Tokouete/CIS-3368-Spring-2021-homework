# import of contact class
# import of datetime library and mysql connector
from contact import Contact
import datetime
from datetime import date
import mysql.connector
from mysql.connector import Error

# defined the creation of the connection to the database from inclass example
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

# defined the query and read execution function from inclass example
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

# Let make the connection to the cis3368 database on mysql
connection = create_connection("cis3368.c3rczxv5d35n.us-east-1.rds.amazonaws.com", "admin", "99Nav&Har14$", "cis3368db")

# create a new contact to the contactstable
cDate = datetime.datetime(2019,3,20)
str_cDate = cDate.date().isoformat()
query = "INSERT INTO contacts (lastname, firstname, contactDetails, creationDate) VALUES ('McSauer','Mike','President of Student Council','"+str_cDate+"')"
 

select_contacts = "SELECT * FROM contacts"
contacts = execute_read_query(connection, select_contacts)
