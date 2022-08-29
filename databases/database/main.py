import mysql.connector
from tkinter import *


database_connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'ch@rles',
   database = 'mydatabase'
)

cursor = database_connection.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS mydatabase')

create_table = "CREATE TABLE IF NOT EXISTS users(name VARCHAR(255), reg VARCHAR(255), password VARCHAR(255), id INTEGER AUTO_INCREMENT PRIMARY KEY)"

cursor.execute(create_table)





# sql = "UPDATE users SET name = 'stiles' WHERE id = 3"
# cursor.execute(sql)
# database_connection.commit()






app = Tk()
app.geometry('500x500')
app.title('gul')

name = StringVar()
reg = StringVar()
password = StringVar()



def submit_app(name,reg,password):
    print(name)
    sql = 'INSERT INTO users(name,reg,password) VALUES(%s,%s,%s)'
    record = (name, reg,password)
    cursor.execute(sql,record)
    database_connection.commit()
 
def delete_user(id):
    sql = f'DELETE FROM users WHERE id = {id}'
    cursor.execute(sql)
    database_connection.commit()
    
def read_details():
    sql = 'SELECT * FROM users'
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    
       
Entry(app, textvariable=name, width= 50).pack()
Entry(app, textvariable=reg, width= 50).pack()
Entry(app,textvariable=password, width=50).pack()

get_name = name.get()
get_reg = reg.get()
get_pass = password.get()


Button(app,text='submit input', command=lambda: submit_app(get_name,get_reg,get_pass)).pack()
Button(app,text='read', command=read_details).pack()
Button(app,text='delete', command=delete_user).pack()
# Button(app,text='get input', command=lambda: submit_app(get_name)).pack()


app.mainloop()


