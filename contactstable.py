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
#execute_query(connection, query)  

# create menu list for the contacts table database
menu = ('MENU\n'
        'a - Add contact\n'
        'd - Remove contact\n'
        'u - Update contact details\n'
        'b - Output all contacts in alphabetical order\n'
        'c - Output all contacts by creation date\n'
        'o - Output all contacts\n'
        'q - Quit\n')

option = ''
while option != 'q':
    print(menu)
    option = input('Choose an option: ')
    
    # add a new contact to the contact table
    if option == 'a':
        cDate = datetime.datetime(2020,10,20)
        str_cDate = cDate.date().isoformat()
        lastname = input('Enter lastname:\n')
        firstname = input('Enter firstname\n')
        contactDetails = input('Enter contact details\n')
        creationDate = input('Enter date\n')
        query = "INSERT INTO contacts (lastname, firstname, contactDetails, creationDate) VALUES ('%s','%s','%s','" + str_cDate + "')" % (lastname, firstname, contactDetails, creationDate, str_cDate)
        execute_query(connection, query)

    # remove a contact from the contact table
    elif option == 'd':
        contact_remove = input('Enter id number:\n')
        delete_query = 'DELETE FROM contacts WHERE id = %s' % (contact_remove)
        execute_query(connection, delete_query)

    # update contact details
    elif option == 'u':
        new_contactDetails = input('Enter new contact details:\n')
        update_contactDetails_query = "UPDATE contacts SET contactDetails = '%s' WHERE id = 4 " % (new_contactDetails)
        execute_query(connection, update_contactDetails_query)

    # output all contacts
    elif option == 'o':
        select_contacts = 'SELECT * FROM contacts'
        contacts = execute_read_query(connection, select_contacts)

        for contact in contacts:
            print(contact)


