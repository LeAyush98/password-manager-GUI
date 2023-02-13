from tkinter import *
from tkinter import messagebox
import string
import random 
import datetime

def password_generator():
    password_entry.delete(0, END)
    list_alpha = list(string.ascii_letters)
    list_numbers = ["0","1","2","3","4","5","6","7","8","9"]
    list_symbols = ["~","`","!","#","$","%","^","&","*","(",")","_","-"]
    password = []
    for place in range(6):
        password.append(random.choice(list_alpha))
        password.append(random.choice(list_numbers))
        password.append(random.choice(list_symbols))
    random.shuffle(password)
    password = "".join(password)
    password_entry.insert(0, password)

def save_to_file():
    messagebox.showinfo(title="Success!", message="Credentials saved")

    save = open("secure.txt", "a")
    read = open("secure.txt", "r")
    now = datetime.datetime.now()
    now = now.strftime("%d-%m-%Y %H:%M:%S")

    if f"{username_entry.get()} | {website_entry.get()} | {password_entry.get()} \n\n" in read.readlines():
        print(f"Entry already exists!")
    else:
        save.write(f"[Update at {now}]: \n")
        save.write(f"{username_entry.get()} | {website_entry.get()} | {password_entry.get()} \n\n") 
    website_entry.delete(0,END)
    password_entry.delete(0,END)
    website_entry.focus()


window = Tk()

window.title("Password Manager")
window.config(padx=50, pady= 50, bg= "white")

canvas = Canvas(width=200, height=200, bg= "white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image= logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ", font=("Arial", 10, "bold"), bg= "white")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky= EW)
website_entry.focus()

username_label = Label(text="Email/Username:  ",font=("Arial", 10, "bold"), bg= "white")
username_label.grid(column=0, row=2)

username_entry = Entry(width=35)
username_entry.insert(0,"ayu.sharma798@gmail.com")
username_entry.grid(column = 1, row=2, columnspan=2, sticky= EW)

password_label = Label(text="Password:  ",font=("Arial", 10, "bold"), bg= "white")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column = 1, row=3, sticky= EW)

generate_password_button = Button(text="Generate Password",font=("Arial", 10, "bold"), command=password_generator)
generate_password_button.grid(column=2, row=3, sticky= EW)

add = Button(text="Add",font=("Arial", 10, "bold"), width=36, command=save_to_file)
add.grid(column=1, row=4, columnspan=2, sticky= EW)

window.mainloop()