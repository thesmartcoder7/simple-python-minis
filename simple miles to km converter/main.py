from tkinter import *


def convert():
    value = float(my_input.get())
    result = str(round(value * 1.609344))
    converted_label.config(text=result)


window = Tk()
window.title("Distance Converter")
window.config(padx=50, pady=50)

my_input = Entry(width=10)
my_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 12, "normal"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=0, pady=10)

equal_label = Label(text="is equal to", font=("Arial", 12, "normal"))
equal_label.grid(column=0, row=1)
equal_label.config(padx=0, pady=20)

converted_label = Label(text="0", font=("Arial", 12, "normal"))
converted_label.grid(column=1, row=1)
converted_label.config(padx=10, pady=20)

km_label = Label(text="Kilometers", font=("Arial", 12, "normal"))
km_label.grid(column=2, row=1)
km_label.config(padx=0, pady=20)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

window.mainloop()
