# Susana Xiao
# Friday Project 7 
# DS 3850 Section 001
# The following is a database file that stores the user's information.

# Importing sqlite function and establishing a connection to the database file name.
import sqlite3

# Import all functions and variables from tkinter package.
from tkinter import *
from tkinter import ttk

# Creates a new window and names the variable "root."
# A title page "Sign-Up Page."
root = Tk()
root.title ("Sign-Up Page")

# Execution method to the database that types the SQL script.
connection = sqlite3.connect ('user_database.db')
cursor = connection.cursor()
cursor.execute ('''
    CREATE TABLE IF NOT EXISTS users
    (email TEXT PRIMARY KEY, 
    password TEXT)
                ''')

# Executing SQL Query by insert datas into the functions.
def users (email, password):
    email=email.lower()
    cursor.execute (f"""
        INSERT INTO users(email, password)
        VALUES (?,?) """, (email, password))

# A class function for GUIs.
# Two variable assigned the value of ttk.Label and ttk.Entry. Grid function provides a location for the text.
class SignUpApp:
    def __init__ (self, master):
        self.email_label = ttk.Label (master, text = "Email:")
        self.email_label.grid (row = 0, column = 0)
        self.email_entry = ttk.Entry (master)
        self.email_entry.grid (row = 0, column = 1)

        self.password_label1 = ttk.Label (master, text = "Password:")
        self.password_label1.grid (row = 1, column = 0)
        self.password_entry1 = ttk.Entry (master, show = "*")
        self.password_entry1.grid (row = 1, column = 1)

        self.password_label2 = ttk.Label (master, text = "Re-enter Password")
        self.password_label2.grid (row = 2, column = 0)
        self.password_entry2 = ttk.Entry (master, show = "*")
        self.password_entry2.grid (row = 2, column = 1 )

        self.signup_button = ttk.Button (master, text = "Sign Up", command = self.sign_up)
        self.signup_button.grid(row = 3, column = 1)

# Check if password match
# Check if email is valid
# Add user to the database
# Checks if email contains @ and the correct domains.
    def sign_up(self):
        if self.password_entry1.get() ==self.password_entry2.get():
            if '@' in self.email_entry.get() and '.' in self.email_entry.get():
                users(self.email_entry.get(),self.password_entry1.get())
                print("username and password added to database")

            else:
                print("Email need to contain @ and a domain")

        else:
            print("Did not re-enter Password correctly")

# Clear entry field
        self.password_entry1.delete(0,'end')
        self.password_entry2.delete(0,'end')
        self.email_entry.delete(0,'end')

# Start the Tkinter loop
#  Create an instance of the SignInApp class with the Tkinter root window as the master.
Application = SignUpApp (root)
root.mainloop()

# Closing the database connection
connection.commit()
connection.close()

