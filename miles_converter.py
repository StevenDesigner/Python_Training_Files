import tkinter as tk

def convert():
    miles = float(entry_miles.get())
    kilometers = miles * 1.60934
    label_result.config(text=f"{miles} miles is equal to {kilometers:.2f} kilometers.")

# Create the main window
root = tk.Tk()
root.title("Miles to Kilometers Converter")

# Create widgets
label_miles = tk.Label(root, text="Enter distance in miles:")
entry_miles = tk.Entry(root)
button_convert = tk.Button(root, text="Convert", command=convert)
label_result = tk.Label(root, text="")

# Layout widgets using grid
label_miles.grid(row=0, column=0, padx=10, pady=10)
entry_miles.grid(row=0, column=1, padx=10, pady=10)
button_convert.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
label_result.grid(row=2, column=0, columnspan=2)

root.mainloop()
