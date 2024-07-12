import tkinter as tk
from tkinter import messagebox

def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        result = num1 + num2 + num3
        result_label.config(text=f"Resultaat: {result}")
    except ValueError:
        messagebox.showerror("Ongeldige invoer", "Voer alstublieft geldige nummers in.")

root = tk.Tk()
root.title("Eenvoudige Rekenmachine")

label1 = tk.Label(root, text="Eerste getal:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Tweede getal:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

label3 = tk.Label(root, text="Derde getal:")
label3.pack()

entry3 = tk.Entry(root)
entry3.pack()

add_button = tk.Button(root, text="Tel op", command=add_numbers)
add_button.pack()

result_label = tk.Label(root, text="Resultaat: ")
result_label.pack()

root.mainloop()