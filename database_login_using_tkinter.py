 # CHARLES MADHUKU               






from tkinter import Tk , StringVar, Label, Entry, Button, Toplevel, Listbox , LEFT,BOTH,Scrollbar, RIGHT, END
from tkinter.messagebox import showinfo, showerror
import sqlite3
from sqlite3 import Error




stiles_table_users = """CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOiNCREMENT,
    username TEXT NOT NULL,
    reg TEXT NOT NULL,
    password TEXT NOT NULL
    );
    """
stiles_table_todos = """CREATE TABLE IF NOT EXISTS todos(
    id INTEGER PRIMARY KEY AUTOiNCREMENT,
    reg TEXT NOT NULL,
    todo TEXT NOT NULL
    );
    """


class Login_system(Tk):
    
    def __init__(self):
        super(Login_system, self).__init__()
        self.geometry("550x600")
        self.title('SLAVA X STLIES')
        self.resizable(False,False)
        self.logged_in = False
        self.username = StringVar()
        self.username_error_label = Label(self,text='',
                            font=('arial',7),                          
                            pady=8,)
        self.password = StringVar()
        self.password_error = Label(self,text='',
                            font=('arial',7),                          
                            pady=8,)
        
        self.sign_password = StringVar()
        self.sign_password_error = Label(self,text='',
                            font=('arial',7),                          
                            pady=8,)
        self.sign_username = StringVar()
        self.sign_username_error = Label(self,text='',
                            font=('arial',7),                          
                            pady=8,)
        self.sign_password = StringVar()
                       
        self.reg = StringVar()
        self.reg_error = Label(self,text='',
                            font=('arial',7),                          
                            pady=8,)
        self.login_btn = Button(self, text='Login',width=25,command=self.login).grid(row=6, column=6)
        self.self_btn = Button(self, text='Login',width=25, command= self.sign_stiles_in).grid(row=15, column=6)
        self.connect = self.connection('./login_system.sql')
        self.execute_query(self.connect, stiles_table_users)
        self.execute_query(self.connect, stiles_table_todos)
        self.layout_design()
        self.todo = StringVar()
        todos = []
        
    def list_box(self,newPage, result):
         # todo list box
        todolist = Listbox(newPage,width=50)
        todolist.grid(row=4, column=6)
        scrollbar = Scrollbar(newPage)

        scrollbar.grid(row=4, column=7)
        
        for i in range(len(result)):
           
            todolist.insert(END,result[i][2])
        todolist.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = todolist.yview)
        
        print(todolist.curselection())
        

    def add_todo_items(self,name, reg, newPage):
        todo = self.todo.get()
        if todo == '':
            showerror(
                        title='error',
                        message='todo is empty'
                    )
        else:
            query = f"INSERT INTO todos(reg,todo) VALUES( '{reg}' , '{todo}')"
            #    create new user
            if self.execute_query(self.connect,query):
                    showinfo(
                        title = 'todo pad',
                            message=f'{todo} has been added'
                        
                    )
                    query = f"SELECT * FROM todos WHERE reg= '{reg}'"
                    result = self.fetch_result(self.connect,query)
                    if len(result) > 0:
                       self.list_box(newPage, result)
                        
                    
            
        
    def newWindow(self, name,reg):
        newPage = Toplevel(self)
        newPage.geometry('550x600')
        newPage.title('SLAVA X STILES')
        header_text = Label(newPage,text=f'Welcome {name} to your Todo App',
                            font=('arial',15),
                            padx=20,
                            pady=20,
                            
                            ).grid(row=0,column=6)
        stiles_login_text = Label(newPage,text=' Todo App',
                            font=('arial',15),
                            
                            pady=10,
                            
                            ).grid(row=1,column=6)
        # todo text input 
        todo_input = Entry(newPage, textvariable=self.todo, width=50).grid(row=2, column=6)
        # todo submit button
        self_btn = Button(newPage, text='Add Todo List Item',width=25, command= lambda:self.add_todo_items(name,reg,newPage)).grid(row=3, column=6)
        query = f"SELECT * FROM todos WHERE reg= '{reg}'"
        result = self.fetch_result(self.connect,query)
        self.list_box(newPage, result)
       
    
        
    def login(self):
        error = False
       
        reg = self.username.get()
        password = self.password.get()
        
        if password == '':
            self.password_error.config(text='Please enter your password ')
            error = True
        else:
            if len(password) < 8:
                self.password_error.config(text='Password is too short')
                error = True
            
        if reg == '':
            self.username_error_label.config(text='Reg number is empty')
            error = True
        else:
            if len(reg) < 6:
                self.username_error_label.config(text='Reg number is too short. please enter 6 digits and above')
                error = True
        
        print(reg,password)
            
        if error:
            return
        else:
            query = f"SELECT * FROM users WHERE reg= '{reg}' AND password = '{password}' "
            result = self.fetch_result(self.connect,query)
            if len(result) > 0:
                name = result[0][1]
                reg = result[0][2]
                self.newWindow(name,reg)
                # showinfo(
                #         title = 'Sign in message',
                #         message=f' Welcome {name} : {reg} to SLAVA X STILES. \n Please use our system wisely thank u'
                        
                #     )
                self.username = ''
                self.password = ''
            else:
                showerror(
                        title='login error',
                        message='Please check your details it seems you are not registered with our system '
                    )
            
      
    def sign_stiles_in(self):
        error = False
        username = self.sign_username.get()
        reg = self.reg.get()
        password = self.sign_password.get()
        
        # validation of inputs 
        if username == '':
            self.sign_username_error.config(text='Please enter your username')            
            error = True
        if password == '':
            self.sign_password_error.config(text='Please enter your password ')
            error = True
        else:
            if len(password) < 8:
                self.sign_password_error.config(text='Password is too short')
                error = True
            
        if reg == '':
            self.reg_error.config(text='Reg number is empty')
            error = True
        else:
            if len(reg) < 6:
                self.reg_error.config(text='Reg number is too short. please enter 6 digits and above')
                error = True
            
        if error:
            return
        else:
            # read reg in the data base to find if its the only one
            query = f"SELECT * FROM users WHERE reg= '{reg}' "
            result = self.fetch_result(self.connect,query)
            print(result)
            if len(result) == 0:
                
                query = f"INSERT INTO users(username,reg,password) VALUES('{username}', '{reg}' , '{password}')"
            #    create new user
                if self.execute_query(self.connect,query) :
                    showinfo(
                        title = 'Sign in message',
                        message=f' Welcome {username} to SLAVA X STILES. \n Please use our system wisely thank u'
                        
                    )
                else:
                    showerror(
                        title='Sign error',
                        message='Something went wrong while signing in'
                    )
            else:
                self.reg_error.config(text='Reg number is already registered')
                return
                
          
    def connection(self,path):
        connection = None
        try:
            connection = sqlite3.connect(path)
            print('connection established')
        except Error as e:
            print(f'error on :{e}')
        return connection
        
    def execute_query(self,connection,query):
        cursor = connection.cursor()
        try:
           cursor.execute(query)
           connection.commit()
           print('Query was sucessfull')
           return True
        except Error as e:
            print(f'error on :{e}')
            return False
    
    def fetch_result(self,connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            print('Query was sucessfull')
        except Error as e:
            print(f'error at {e}')
        return result
        
    def layout_design(self):
        # header text
        header_text = Label(self,text='SLAVA X STILES SYSTEMS',
                            font=('arial',20),
                            padx=20,
                            pady=20,
                            
                            ).grid(row=0,column=6)
        stiles_login_text = Label(self,text='LOG IN',
                            font=('arial',15),
                            
                            pady=10,
                            
                            ).grid(row=1,column=6)
        # login form
        username_label = Label(self,text="Reg number").grid(row=2,column=5)
        username_input = Entry(self, textvariable=self.username, width=50).grid(row=2, column=6)
        self.username_error_label.grid(row=3,column=6)
        password_label = Label(self,text="Password").grid(row=4,column=5)
        password_input = Entry(self, textvariable=self.password,width=50).grid(row=4, column=6)
        self.password_error.grid(row=5,column=6)
        
        # signinform
        
        signin_header_label = Label(self,text="Please sign in below if do not have an account with us", font=('arial',10),                          
                            pady=15,).grid(row=7,column=6)
        stiles_sign_label = Label(self,text="SIGN IN", font=('arial',15),                          
                            pady=15,).grid(row=8,column=6)
        signin_username_label = Label(self,text="Username").grid(row=9,column=5)
        signIn_username_input = Entry(self, textvariable=self.sign_username,width=50).grid(row=9, column=6)
        self.sign_username_error.grid(row=10,column=6)
        reg_label = Label(self,text="Reg Number", padx=10).grid(row=11,column=5)
        reg_input = Entry(self, textvariable=self.reg,width=50).grid(row=11, column=6)
        self.reg_error.grid(row=12,column=6)
        password_label = Label(self,text="Password").grid(row=13,column=5)
        password_input = Entry(self, textvariable=self.sign_password ,width=50).grid(row=13, column=6)
        self.sign_password_error.grid(row=14,column=6)
        
        



form = Login_system()
form.mainloop()