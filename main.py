import tkinter as tk

import os

import mysql.connector as mysql
from mysql.connector import errorcode

def open_manage():
    os.system('python3 login-system.py')

def open_employee():
    os.system('python3 personal-login-system.py')

con = mysql.connect(host="localhost", user="ms_user", password="manageuser", database="ManageEmp")
cursor = con.cursor()

#def executeScript(managmentDatabase):
    #fd = open(managmentDatabase, 'r')
    #sqlfile = fd.read()
    #fd.close()
    #sqlCommands = sqlfile.split(';')

    #for command in sqlCommands:

        #if command.strip() != '':
            #cursor.execute(command)

#executeScript('managmentDatabase.sql')
#con.commit()

root = tk.Tk()
root.title('Desktop App')
root.config(bg='white')

openUser = tk.Button(root, text="Personal Information", font=('italic',20), highlightbackground='#3E4149', command=open_employee)
openUser.place(x=50,y=240)

openManage = tk.Button(root, text="Management", font=('italic',20), highlightbackground='#3E4149', command=open_manage)
openManage.place(x=330,y=240)

root.mainloop()
