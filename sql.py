import mysql.connector

try:
    # Replace with a strong, unique password (don't store directly in code)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="vajra@007",
        database="mydb"
    )

    mycurs = mydb.cursor()

    # ... (rest of your code for creating the table)

except mysql.connector.Error as err:
    print("Error connecting or executing SQL:", err)

#mycurs.execute("create table users(name varchar(50),email varchar(50),password varchar(50))")
#mycurs.execute("show tables")
#mycurs.execute("create table users(name varchar(50),email varchar(50),password varchar(50))")
sql = "Insert into users(name,email,password)values(%s,%s,%s)"
val = ("sind","abc@gmail.com","123")
mycurs.execute(sql,val)
for db in mycurs:
    print(db)