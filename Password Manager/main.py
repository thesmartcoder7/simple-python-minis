from tkinter import *
from tkinter import messagebox
from password_generator import generate_password
import pyperclip
import json


# fetching data
def fetch_data():
    website = website_entry.get().lower()
    if len(website) == 0:
        messagebox.showwarning(title="Empty Search Item!", message="The search field is empty!")
    else:
        try:
            with open("passwords.json", mode="r") as passwords:
                data = json.load(passwords)
        except FileNotFoundError:
            messagebox.showwarning(title="No File Entry!", message="You have not saved anything yet!")
        else:
            try:
                info = data[website]
            except KeyError:
                messagebox.showwarning(title="Entry not Found!",
                                       message=f"You have not saved details for {website.title()} yet")
            else:
                messagebox.showinfo(title=f"{website.title()} Details",
                                    message=f"\n\nEmail/Username: {info['email/username']}\
                                    \nPassword: {info['password']}\n\n")


# generate password
def generate_new_password():
    password_entry.delete(0, END)
    new_password = generate_password()
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)


# Saving Data
def save_data():
    website = website_entry.get().lower()
    url = url_entry.get()
    email_username = email_entry.get()
    password = password_entry.get()

    new_entry = {
        website: {
            "url": url,
            "email/username": email_username,
            "password": password
        }
    }

    if len(website) == 0:
        messagebox.showwarning(title="Empty Website!", message="The Website field is empty!")
    elif len(email_username) == 0:
        messagebox.showwarning(title="Empty Email!", message="The Email field is empty!")
    elif len(password) == 0:
        messagebox.showwarning(title="Empty Password!", message="The Password field is empty!")
    else:
        confirmation_message = f"These are the details to be saved into the file:\n\n" \
                               f"Website: {website}\nUrl: {url}\nEmail: {email_username}\n" \
                               f"Password: {password}\n\nIs it ok to save?"
        go_ahead = messagebox.askokcancel(title="Confirm Info", message=confirmation_message)

        if go_ahead:
            try:
                with open("passwords.json", mode="r") as passwords:
                    data = json.load(passwords)
            except FileNotFoundError:
                with open("passwords.json", mode="w") as passwords:
                    json.dump(new_entry, passwords, indent=4)
            else:
                data.update(new_entry)
                with open("passwords.json", mode="w") as passwords:
                    json.dump(data, passwords, indent=4)
            finally:
                messagebox.showinfo(title="Success!", message="Your info has been successfully saved!")
                website_entry.delete(0, END)
                url_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(width=500, height=500, padx=100, pady=80)
window.option_add('*Dialog.msg.font', 'Arial 10')
window.option_add('*Dialog.msg.width', 50)
window.option_add('*Dialog.msg.height', 40)

canvas = Canvas(highlightthickness=0)
logo = PhotoImage(file="padlock.png")
canvas.create_image(190, 90, image=logo)
canvas.grid(column=0, row=0, columnspan=3)

website_label = Label(text="Website Name:   ")
website_label.config(pady=15, font=("Arial", 10, "normal"))
website_label.grid(column=0, row=1)

website_entry = Entry(width=22)
website_entry.focus()
website_entry.grid(column=1, row=1)

search_button = Button(text="Search", command=fetch_data)
search_button.config(padx=18, width=14, font=("Arial", 10, "normal"))
search_button.grid(column=2, row=1, padx=5)

url_label = Label(text="Website url (optional):   ")
url_label.config(pady=15, font=("Arial", 10, "normal"))
url_label.grid(column=0, row=2)

url_entry = Entry(width=41)
url_entry.grid(column=1, row=2, columnspan=2)

email_label = Label(text="Email/Username:     ")
email_label.config(pady=15, font=("Arial", 10, "normal"))
email_label.grid(column=0, row=3)

email_entry = Entry(width=41)
email_entry.grid(column=1, row=3, columnspan=2)

password_label = Label(text="Password:   ")
password_label.config(pady=15, font=("Arial", 10, "normal"))
password_label.grid(column=0, row=4)

password_entry = Entry(width=23)
password_entry.grid(column=1, row=4)

password_button = Button(text="Generate Password", command=generate_new_password)
password_button.config(padx=17, width=14, font=("Arial", 10, "normal"))
password_button.grid(column=2, row=4, padx=5)

add_button = Button(text="Add", width=39, font=("Arial", 11, "normal"), command=save_data)
add_button.config(pady=10)
add_button.grid(column=1, row=5, columnspan=3, pady=15)

window.mainloop()
