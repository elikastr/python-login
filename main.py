from re import A
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


# name entry
ttk.Label(root, text="Full Name:").pack()
name = tk.StringVar()
name_entry = ttk.Entry(root, textvariable=name)
name_entry.pack()

# address entry
ttk.Label(root, text="Address:").pack()
address = tk.StringVar()
address_entry = ttk.Entry(root, textvariable=address)
address_entry.pack()

# preferable ant radio buttons
ttk.Label(text="Preferable Ant:").pack()
selected_ant = tk.StringVar()
ants = ['argentine',
        'black',
        'carpenter', 
        'fire']
ant_imgs = [tk.PhotoImage(file='./assets/argentine.png'),
            tk.PhotoImage(file='./assets/black.png'),
            tk.PhotoImage(file='./assets/carpenter.png'),
            tk.PhotoImage(file='./assets/fire.png')]

radio_buttons = []
for i in range(len(ants)):
    radio_buttons.append(ttk.Radiobutton(
        root,
        image=ant_imgs[i],
        value=ants[i],
        variable=selected_ant
    ))
    radio_buttons[i].pack()
radio_buttons.append(ttk.Radiobutton())

def clear_fields():
    print(name.get(), address.get(), selected_ant.get())
    name_entry.delete(0, 'end')
    address_entry.delete(0, 'end')
    selected_ant.set(0)

# check if all fields are filled
def check_fields():
    if not name.get(): return False
    if not address.get(): return False
    if not selected_ant.get(): return False
    return True


error_label = ttk.Label(root, text="Please fill out all entries")
success_label = ttk.Label(root, text="You are successfully registered!")

# if all fields are filled, they are cleared and a success message is shown
# otherwise, an error message is shown
def send():
    if not check_fields():
        error_label.pack()
    else:
        error_label.pack_forget()
        clear_fields()
        success_label.pack()


send_button = ttk.Button(
    root,
    text='Send',
    command=send
)
send_button.pack()


root.mainloop()