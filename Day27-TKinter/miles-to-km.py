from tkinter import *


def convert():
    mile = float(mile_input.get())
    in_km = round(mile * 1.609, 2)
    km_value_label.config(text=in_km)


window = Tk()
window.title("Miles to Km Converter.")
window.config(padx=20, pady=20)

label = Label(text="is equal to")
label.grid(column=0, row=1)
label.config(pady=10, padx=10)

mile_input = Entry(width=15)
mile_input.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)
mile_label.config(padx=10, pady=10)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

km_value_label = Label(text="0")
km_value_label.grid(column=1, row=1)
km_value_label.config(padx=10, pady=10)

button = Button(text="Convert", command=convert)
button.grid(column=1, row=2)

window.mainloop()
