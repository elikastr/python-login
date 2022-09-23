import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Welcome to Luxuriant')

# root window
window_width = 600
window_height = 500

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

radio_frame = ttk.Frame(root)
radio_frame.pack()

radio_buttons = []
for i in range(len(ants)):
    radio_buttons.append(ttk.Radiobutton(
        radio_frame,
        image=ant_imgs[i],
        value=ants[i],
        variable=selected_ant
    ))
    radio_buttons[i].grid(row=1, column=i)
radio_buttons.append(ttk.Radiobutton())

# tuxedo combobox
ttk.Label(root, text="Tuxedo Type:").pack()
selected_tux = tk.StringVar()

combobox = ttk.Combobox(root, textvariable=selected_tux, state='readonly')
combobox['values'] = ['1. Black', '2. White', '3. Penguin', '4. Velvet']
combobox.pack()

# number of ants entry
ttk.Label(text="Number of Ants:").pack()
ants_num = tk.StringVar(value=0)
spinbox = ttk.Spinbox(
    root,
    from_=0,
    to=100,
    textvariable=ants_num,
    wrap=True
)
spinbox.pack()


def clear_fields():
    print(name.get(), address.get(), selected_ant.get(), int(selected_tux.get()[0]), int(ants_num.get()))
    name_entry.delete(0, 'end')
    address_entry.delete(0, 'end')
    selected_ant.set(0)
    selected_tux.set(0)
    ants_num.set(0)


# check if all fields are filled
def check_fields():
    if not (name.get() and address.get() and selected_ant.get() and selected_tux.get() and ants_num.get()):
        return "Please fill out all entries"
    if not ants_num.get().isnumeric():
        return "Invalid ant number chosen"
    return ""


message_label = ttk.Label(root)
success_label = ttk.Label(root, text="You are successfully registered!")

# if all fields are valid, they are cleared and a success message is shown
# otherwise, an error message is shown
def send():
    message = check_fields()
    if message:
        message_label['text'] = message
        message_label.pack()
    else:
        message_label['text'] = "You are successfully registered!"
        clear_fields()
        message_label.pack()


send_button = ttk.Button(
    root,
    text='Send',
    padding=5,
    command=send
)
send_button.pack()


root.mainloop()