from tkinter import *

window = Tk()
window.title("Miles to KM converter")
# window.minsize(width = 500, height = 1000)
window.config(padx = 200, pady = 200)

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text = f"{km}")


miles_input = Entry(width = 5)
miles_input.grid(row = 0, column = 1)

miles_label = Label(text = "Mile")
miles_label.grid(row = 0, column = 2)

is_equal_label = Label(text = "is_equal_to")
is_equal_label.grid(row = 1, column = 0)

km_label = Label(text = "KM")
km_label.grid(row = 2, column = 2)

km_result_label = Label(text = "0")
km_result_label.grid(row = 2, column = 1)

calculate_button = Button(text= "Calculate", command = miles_to_km)
calculate_button.grid(row = 3, column = 1)

# miles_to_km()

window.mainloop()