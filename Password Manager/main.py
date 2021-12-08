from tkinter import *
from tkinter import messagebox
from password_generator import generate_password
import pyperclip


# generate password
def generate_new_password():
    password_entry.delete(0, END)
    new_password = generate_password()
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)


# Saving Data
def save_data():
    website = website_entry.get()
    email_username = email_entry.get()
    password = password_entry.get()

    if len(website) == 0:
        messagebox.showwarning(title="Empty Website!", message="The Website field is empty!")
    elif len(email_username) == 0:
        messagebox.showwarning(title="Empty Email!", message="The Email field is empty!")
    elif len(password) == 0:
        messagebox.showwarning(title="Empty Password!", message="The Password field is empty!")
    else:
        confirmation_message = f"These are the details to be saved into the file:\n\n" \
                  f"Website: {website}\nEmail: {email_username}\n" \
                  f"Password: {password}\n\nIs it ok to save?"
        go_ahead = messagebox.askokcancel(title="Confirm Info", message=confirmation_message)

        if go_ahead:
            save_to_file(website, email_username, password)
            messagebox.showinfo(title="Success!", message="Your info has been successfully saved!")
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)


# writing to file
def save_to_file(website, email_username, password):
    with open("passwords.txt", mode="a") as file:
        file.write(f"\n--------------------------------------------------------------------------\n "
                   f"Website: {website}\n Email/Username: {email_username}\n Password: {password}\n")


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

website_label = Label(text="Website:   ")
website_label.config(pady=15, font=("Arial", 10, "normal"))
website_label.grid(column=0, row=1)

website_entry = Entry(width=41)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username:     ")
email_label.config(pady=15, font=("Arial", 10, "normal"))
email_label.grid(column=0, row=2)

email_entry = Entry(width=41)
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:   ")
password_label.config(pady=15, font=("Arial", 10, "normal"))
password_label.grid(column=0, row=3)

password_entry = Entry(width=23)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", command=generate_new_password)
password_button.config(padx=17, width=14, font=("Arial", 10, "normal"))
password_button.grid(column=2, row=3, padx=5)

add_button = Button(text="Add", width=39, font=("Arial", 11, "normal"), command=save_data)
add_button.config(pady=10)
add_button.grid(column=1, row=4, columnspan=3, pady=15)

window.mainloop()
