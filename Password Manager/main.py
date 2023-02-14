from tkinter import *
from tkinter import messagebox
import string
import random 
import json

entered_file = True

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

def search():
    website = website_entry.get()
    with open("secure.json", "r") as data_file:
        data = json.load(data_file)
        for key,value in data.items():
            if key == website:
                messagebox.showinfo(title=f"{website}", message=f"Email: {data[key]['E-mail']} \nPassword: {data[key]['Password']}")
        if website not in data.keys():
                messagebox.showerror(title=f"Error!", message=f"No entry for {website} found")    

def save_to_file():
    global entered_file
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    data = {website: {"E-mail": username,"Password": password}}
    
    if website == "" and password == "":
        messagebox.showerror(title="Missing values", message="Please make sure sufficient data is entered")
    else:
        if entered_file == False:    
            with open("secure.json", "r") as data_file:
                view_data = json.load(data_file)
                view_data.update(data)
        with open("secure.json", "w") as data_file:
            if entered_file == True:
                json.dump(data, data_file, indent=4)
                entered_file = False 
            else:
                json.dump(view_data, data_file, indent=4)
            messagebox.showinfo(title="Success!", message="Credentials saved")           
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

website_entry = Entry(width=25)
website_entry.grid(column=1, row=1, sticky=EW)
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

search_button = Button(text="Search",font=("Arial", 10, "bold"), command=search)
search_button.grid(column=2, row=1, sticky=EW)

window.mainloop()

