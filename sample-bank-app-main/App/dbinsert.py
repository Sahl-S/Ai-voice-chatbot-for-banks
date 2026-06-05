import mysql.connector

def userreq(name, dob, mobileno, email, adhaar, address, imgname):
    # Establish a connection to the MySQL database
    mydb = mysql.connector.connect(
        host="localhost"
        , user="root"
        , password="root"
        , port='3306'
        , database="bank"
    )

    mycursor = mydb.cursor()

    # Insert the user's data into the `usereq` table using a parameterized query
    mycursor.execute("INSERT INTO userreq VALUES (%s, %s, %s, %s, %s, %s, %s)", (name, dob, mobileno, email, adhaar, address, imgname))

    # Commit the changes and close the connection
    mydb.commit()
    mydb.close()


