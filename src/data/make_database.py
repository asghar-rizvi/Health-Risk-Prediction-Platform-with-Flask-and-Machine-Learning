import mysql.connector
__db = None

def create_database():
    global __db
    __db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="asgharroot",
        auth_plugin='mysql_native_password',
        database="testdatabase"
    )


def create_table():
    global __db
    my_cursor = __db.cursor()
    my_cursor.execute("""
        CREATE TABLE IF NOT EXISTS USERS (
            User_Id int PRIMARY KEY AUTO_INCREMENT NOT NULL,
            User_Name varchar(30) NOT NULL,
            User_email varchar(50) NOT NULL,
            User_passwd varchar(60) NOT NULL  -- Increased column size for hashed passwords
        )
    """)
    __db.commit()



def drop_table(table_name):
    global __db
    my_cursor = __db.cursor()
    my_cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    __db.commit()

def insert_values(user_name, user_email, user_passwd):
    global __db
    my_cursor = __db.cursor()
    query = """
        INSERT INTO USERS (User_Name, User_email, User_passwd)
        VALUES (%s, %s, %s)
    """
    values = (user_name, user_email, user_passwd)
    my_cursor.execute(query, values)
    __db.commit()

def view_database():
    global __db
    my_cursor = __db.cursor()
    query = "SELECT * FROM USERS"
    my_cursor.execute(query)
    results = my_cursor.fetchall()
    return results

def search_by_email(email):
    global __db
    if __db is None:
        raise Exception("Database connection not established. Call create_database() first.")

    query = "SELECT * FROM USERS WHERE User_email = %s"
    cursor = __db.cursor()
    cursor.execute(query, (email,))
    records = cursor.fetchall()
    cursor.close()
    return records


def search_by_email_and_password(email, password):
    global __db
    if __db is None:
        raise Exception("Database connection not established. Call create_database() first.")

    query = "SELECT * FROM USERS WHERE User_email = %s AND User_passwd = %s"
    cursor = __db.cursor(dictionary=True)
    cursor.execute(query, (email, password))
    records = cursor.fetchall()
    cursor.close()

    return records

def search_by_user_id(user_id):
    global __db
    if __db is None:
        raise Exception("Database connection not established. Call create_database() first.")

    query = "SELECT * FROM USERS WHERE User_Id = %s"
    cursor = __db.cursor()
    cursor.execute(query, (user_id,))
    record = cursor.fetchone()
    cursor.close()

    return record

def update_record(user_id, new_name=None, new_email=None, new_password=None):
    global __db
    if __db is None:
        raise Exception("Database connection not established. Call create_database() first.")

    cursor = __db.cursor()

    # Initialize a list to store the fields to be updated and their corresponding values
    fields_to_update = []
    values = []

    if new_name:
        fields_to_update.append("User_name = %s")
        values.append(new_name)
    if new_email:
        fields_to_update.append("User_email = %s")
        values.append(new_email)
    if new_password:
        fields_to_update.append("User_passwd = %s")
        values.append(new_password)

    if not fields_to_update:
        raise ValueError("At least one of new_name, new_email, or new_password must be provided.")

    # Construct the SQL query dynamically based on the fields to be updated
    query = f"UPDATE USERS SET {', '.join(fields_to_update)} WHERE User_id = %s"
    values.append(user_id)

    # Execute the query and commit the changes
    cursor.execute(query, tuple(values))
    __db.commit()
    cursor.close()


if __name__ == '__main__':
    create_database()
    create_table()
    # email = 'asghar@gmail.com'
    # records = search_by_email(email)
    # list = records[0]
    # print(list[1])
    #
    #
    # record = search_by_user_id(8)
    # print(record)

    # drop_table("USERS")
    # insert_values("Alice Smith", "alice.smith@example.com", "passwordAlice123")
    # insert_values("Bob Johnson", "bob.johnson@example.com", "passwordBob456")
    # insert_values("Charlie Brown", "charlie.brown@example.com", "passwordCharlie789")

    # records = view_database()
    # for record in records:
    #     print(record)
    # print(records[0][0][1])

    # email = 'alice.smith@example.com'
    # records = search_by_email(email)
    # print(records)
    # print(view_database())
    # update_record(4,'asghar')
    print(view_database())

