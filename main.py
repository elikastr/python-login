import json
import os
import tkinter as tk
from tkinter import ttk


JSON_FILE_PATH = 'luxuriant.json'
ASSESTS_DIR_PATH = './assets'

root = tk.Tk()

# global variables to hold the user's inputs
name = tk.StringVar()
address = tk.StringVar()
selected_ant = tk.StringVar()
selected_tux = tk.StringVar()
ants_num = tk.StringVar()


def clear_fields():
    name.set('')
    address.set('')
    selected_ant.set('')
    selected_tux.set('')
    ants_num.set('')


def write_to_json():
    new_data = {
        "name": name.get(),
        "address": address.get(),
        "selected ant": selected_ant.get(),
        "selected tuxedo": int(selected_tux.get()[0]),
        "ants number": int(ants_num.get())
    }
    
    data = []

    # there is no way to directly add data to an existing json file
    # if the file already exists, read it and save the data
    # then rewrite the file with the saved and the new data
    if os.path.isfile(JSON_FILE_PATH):
        with open(JSON_FILE_PATH) as feedsjson:
            data = json.load(feedsjson)
        
    data.append(new_data)
    
    with open(JSON_FILE_PATH, mode='w') as f:
        f.write(json.dumps(data, indent=4))

    clear_fields()


# check if all fields are filled and valid, return error message if not
def check_fields():
    if not (name.get() and address.get() and selected_ant.get() and selected_tux.get() and ants_num.get()):
        return "Please fill out all entries"
    if not ants_num.get().isnumeric():
        return "Invalid ant number chosen"
    return ""


message_label = ttk.Label(root)

# if all fields are valid, the data is saved and a success message is shown
# otherwise, an error message is shown
def send():
    message = check_fields()

    if message:
        message_label['text'] = message
        message_label.pack()
    else:
        message_label['text'] = "You are successfully registered!"
        write_to_json()
        message_label.pack()


def main():
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
    logo_img = tk.PhotoImage(file=f'{ASSESTS_DIR_PATH}/logo.png')
    logo_label = ttk.Label(
        root,
        image=logo_img,
        padding=20
    )
    logo_label.pack()

    # name entry
    ttk.Label(root, text="Full Name:").pack()

    name_entry = ttk.Entry(root, textvariable=name)
    name_entry.pack()

    # address entry
    ttk.Label(root, text="Address:").pack()

    address_entry = ttk.Entry(root, textvariable=address)
    address_entry.pack()

    # preferable ant radio buttons
    ttk.Label(text="Preferable Ant:").pack()

    ants = ['argentine',
            'black',
            'carpenter', 
            'fire']
    ant_imgs = [tk.PhotoImage(file=f'{ASSESTS_DIR_PATH}/argentine.png'),
                tk.PhotoImage(file=f'{ASSESTS_DIR_PATH}/black.png'),
                tk.PhotoImage(file=f'{ASSESTS_DIR_PATH}/carpenter.png'),
                tk.PhotoImage(file=f'{ASSESTS_DIR_PATH}/fire.png')]

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

    combobox = ttk.Combobox(root, textvariable=selected_tux, state='readonly')
    combobox['values'] = ['1. Black', '2. White', '3. Penguin', '4. Velvet']
    combobox.pack()

    # number of ants entry
    ttk.Label(text="Number of Ants:").pack()
    spinbox = ttk.Spinbox(
        root,
        from_=0,
        to=100,
        textvariable=ants_num,
        wrap=True
    )
    spinbox.pack()

    send_button = ttk.Button(
        root,
        text='Send',
        padding=5,
        command=send
    )
    send_button.pack()

    root.mainloop()


if __name__ == '__main__':
    main()