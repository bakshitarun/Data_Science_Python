import mysql.connector
mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "root12345",
        database = "testdb",
        )

my_curosr = mydb.cursor()
#my_curosr.execute("CREATE DATABASE testdb")
#
# my_curosr.execute("SHOW DATABASEs")
# for db in my_curosr:
#     print(db[0])

# my_curosr.execute('CREATE TABLE users (name VARCHAR(255),email VARCHAR(255),age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)')
# my_curosr.execute("SHOW TABLES")
# for tb in my_curosr:
#     print(tb[0])
#
# sqlstuff = "INSERT INTO users(name,email,age) VALUES (%s,%s,%s)"
#
# record1 = ("john","john@gmail.com",40)
#
# my_curosr.execute(sqlstuff,record1)
# mydb.commit()

# sqlstuff = "INSERT INTO users(name,email,age) VALUES (%s,%s,%s)"
# records =[
#     ("n","jn@gmail.com",40),
#     ("hn","hn@gmail.com",30),
#     ("ohn","n@gmail.com",20),
# ]
#
# my_curosr.executemany(sqlstuff,records)
# mydb.commit()

my_curosr.execute("SELECT * FROM users")
result = my_curosr.fetchall()
print('Name\tEmail\t\tAge\tId')
print('----\t----\t\t---\t--')

for row in result:
    print(row[0] + "\t%s"  %row[1] + "\t\t%s"  %row[2] + "\t%s"  %row[3])
