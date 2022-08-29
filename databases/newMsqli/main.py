import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'ch@rles',
    database = 'tuts', 
    
)

print(db)

cursor = db.cursor()

# cursor.execute('CREATE DATABASE tuts')
# cursor.execute('SHOW DATABASES')

# cursor.execute(
#    'CREATE TABLE user(name VARCHAR(255) , email VARCHAR(255), age INTEGER(10), id INTEGER AUTO_INCREMENT PRIMARY KEY)' 
# )

sql = "INSERT INTO user(name, email, age) VALUES(%s, %s,%s)"
record = ('charles madhuku', 'dastiles@gmail.com', '25')

cursor.execute(sql,record)
db.commit()


