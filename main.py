import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Welcome to Luxuriant')

# root window
window_width = 600
window_height = 800

margin_x = (root.winfo_screenwidth() - window_width) // 2
margin_y = (root.winfo_screenheight() - window_height) // 2

root.geometry(f'{window_width}x{window_height}+{margin_x}+{margin_y}')
root.attributes('-alpha', 0.95)
root.resizable(False, False)

# logo
logo_img = tk.PhotoImage(file='./assets/logo.png')
logo_label = ttk.Label(
    root,
    image=logo_img,
    padding=20
)
logo_label.pack()


# store text inputs
name = tk.StringVar()
address = tk.StringVar()

# name 
name_label = ttk.Label(root, text="Full Name:")
name_label.pack()

name_entry = ttk.Entry(root, textvariable=name)
name_entry.pack()

# address 
address_label = ttk.Label(root, text="Address:")
address_label.pack()

address_entry = ttk.Entry(root, textvariable=address)
address_entry.pack()

def clear_entries():
    name_entry.delete(0, 'end')
    address_entry.delete(0, 'end')


# send button
error_label = ttk.Label(root, text="Please fill out all entries")
success_label = ttk.Label(root, text="You are successfully registered!")

def send():
    if not (name.get() and address.get()):
        error_label.pack()
    else:
        error_label.pack_forget()
        clear_entries()
        success_label.pack()

send_button = ttk.Button(
    root,
    text='Send',
    padding=20,
    command=send
)
send_button.pack()


root.mainloop()