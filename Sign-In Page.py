# Susana Xiao
# Friday Project 7 
# DS 3850 Section 001
# The following is a database file that stores the user's information.

# Importing sqlite function and establishing a connection to the database file name.
import sqlite3
connection = sqlite3.connect ('user_database.db')

# # Import all functions and variables from tkinter package.
from tkinter import *
from tkinter import ttk

# Creates a new window and names the variable "root."
# A title page "Sign-In Page."
root = Tk()
root.title ("Sign-In Page")

# Execution method to the database that types the SQL script.
cursor = connection.cursor()
cursor.execute ("""
CREATE TABLE IF NOT EXISTS users
    (email TEXT PRIMARY KEY,
    password TEXT)
                """)

# Function to check user credentials during sign-in.
def check_password(email,pwd):
    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    user =cursor.fetchall()
    for email in user:
        if email[1] == pwd:
            print("\033[38;2;0;225;0mLog in Successful\033[0m")
        return
    print("\033[38;2;225;0;0mEmail or Password incorrect\033[0m")
    
# Class for sign-up functionality
class SignInApp:
    def __init__ (self, master):
        self.email_label = ttk.Label (master, text = "Email:")
        self.email_label.grid (row = 0, column = 0)
        self.email_entry = ttk.Entry (master)
        self.email_entry.grid (row = 0, column = 1)

        self.password_label1 = ttk.Label (master, text = "Password:")
        self.password_label1.grid (row = 1, column = 0)
        self.password_entry1 = ttk.Entry (master, show = "*")
        self.password_entry1.grid (row = 1, column = 1)

        self.signup_button = ttk.Button (master, text = "Sign In", command = self.sign_in)
        self.signup_button.grid(row = 3, column = 1)

        self.email =""
        self.password =""

# Function to handle sign-up button 
    def sign_in (self):
        self.email = self.email_entry.get()
        self.email=self.email.lower()
        self.password = self.password_entry1.get()

        check_password(self.email,self.password)

        self.password_entry1.delete(0,'end')
        self.email_entry.delete(0,'end')

# Start the Tkinter event loop
# Create an instance of the SignInApp class with the Tkinter root window as the master.
application = SignInApp (root)
root.mainloop()

# Closing that cursor and the database connection.
connection.commit()
connection.close()