# Modules
import string
import random
import pyperclip
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk

# The main app window
app = Tk()
app.iconbitmap("icon/icon.ico")
app.title("Password Generator")
app.resizable(False, False)
app.config(bg="#1e1e1e")

# App menu
app_menu = Menu(app)
app.config(menu=app_menu)

# Title
title = Label(
    app,
    text="Password Generator",
    height=2,
    font=("Arial", 30),
    fg="#ff0000",
    bg="#1e1e1e",
)
title.grid(row=0, column=1, columnspan=3)

# Message label
input_message_label = Label(
    app,
    text=" Enter how many characters for the password: ",
    height=1,
    font=("Arial", 18),
)
input_message_label.grid(row=1, column=0, columnspan=3, padx=10, sticky=W)
input_message_label.config(fg="#ffffff", bg="#1e1e1e")

# Input number entry
num_char = StringVar()
user_input_entry = Entry(
    app, textvariable=num_char, width=30, font=("Arial", 18), fg="#000000", bg="#dce4ee"
)
user_input_entry.grid(row=1, column=2, columnspan=3, padx=10, sticky=E)

# Password label
password_label = Entry(
    app,
    text="",
    font=("Arial", 20),
    width=60,
    borderwidth=2,
    justify=CENTER,
    state=DISABLED,
)
password_label.grid(row=4, column=1, columnspan=3, padx=10, pady=30)


# New window function
def new():
    global password_label
    user_input_entry.delete(0, END)
    password_label.destroy()
    password_label = Entry(
        app,
        text="",
        font=("Arial", 20),
        width=60,
        borderwidth=2,
        justify=CENTER,
        state=DISABLED,
    )
    password_label.grid(row=4, column=1, columnspan=3, padx=10, pady=30)


# New window event function
def new_event(event):
    new()


# Generate password function
def generate_password():
    # Checking input
    if num_char.get() == "":
        messagebox.showwarning("Password Generator", "No value entered")
    else:
        try:
            num_char_value = int(num_char.get())
            if num_char_value < 6:
                messagebox.showwarning("Password Generator", "Out of range (6-52)")
                user_input_entry.delete(0, END)
            elif 52 < num_char_value:
                messagebox.showwarning("Password Generator", "Out of range (6-52)")
                user_input_entry.delete(0, END)
            else:
                # Shuffling
                try:
                    low_case = list(string.ascii_lowercase)
                    up_case = list(string.ascii_uppercase)
                    digital = list(string.digits)
                    punctual = list(string.punctuation)
                    random.shuffle(low_case)
                    random.shuffle(up_case)
                    random.shuffle(digital)
                    random.shuffle(punctual)
                except:
                    pass
                # Calculating
                try:
                    part1 = round(num_char_value * (30 / 100))
                    part2 = round(num_char_value * (20 / 100))
                except:
                    pass
                # Generating
                try:
                    global password
                    password = []
                    for char in range(part1):
                        password.append(low_case[char])
                        password.append(up_case[char])
                    for char in range(part2):
                        password.append(digital[char])
                        password.append(punctual[char])
                    random.shuffle(password)
                    password = "".join(password[0:])
                    if len(password) < num_char_value:
                        password = password + random.choice(
                            low_case + up_case + digital + punctual
                        )
                    elif len(password) > num_char_value:
                        list_password = list(password)
                        list_password.remove(
                            list_password[random.randint(0, len(password))]
                        )
                        password = "".join(list_password[:])
                    password_label = Entry(
                        app,
                        text=str(password),
                        font=("Arial", 20),
                        width=60,
                        borderwidth=2,
                        justify=CENTER,
                    )
                    password_label.grid(row=4, column=1, columnspan=3, padx=10, pady=30)
                    password_label.delete(0, END)
                    password_label.insert(0, str(password))
                    password_label.config(state=DISABLED)
                except:
                    pass
        except:
            messagebox.showwarning("Password Generator", "Only integers allowed")
            user_input_entry.delete(0, END)


# Generate password event function
def generate_password_event(event):
    generate_password()


# Clear label function
def clear_label():
    user_input_entry.delete(0, END)


# Save function
def save():
    try:
        save_file = filedialog.asksaveasfilename(
            initialdir="Desktop/",
            title="Save as",
            defaultextension=".txt",
            filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")),
        )
        if save_file == "":
            pass
        else:
            save_file = open(save_file, "w")
            try:
                save_file.write(password)
                save_file.close()
            except:
                pass
            messagebox.showinfo("Password Generator", "Password saved successfully")
    except:
        pass


# Save event function
def save_event(event):
    save()


# Copying function
def copy():
    try:
        pyperclip.copy(password)
        messagebox.showinfo("Password Generator", "Password copied successfully")
    except:
        pass


# About function
def about():
    # Create the about window
    about_window = Toplevel()
    about_window.iconbitmap("icon/icon.ico")
    about_window.title("About")
    about_window.config(bg="#1E1E1E")
    about_window.resizable(False, False)
    about_window.focus_set()
    about_window.grab_set()
    # Title
    title = Label(
        about_window,
        text="Password Generator",
        height=2,
        font=("Arial", 20),
        fg="#ff0000",
    )
    title.grid(row=0, column=0, columnspan=2)
    title.config(bg="#1e1e1e")
    # Show app icon
    app_icon = ImageTk.PhotoImage(Image.open("icon/png.png"))
    icon_label = Label(about_window, image=app_icon)
    icon_label.grid(row=0, column=2, columnspan=2, padx=20, pady=30)
    icon_label.config(bg="#1e1e1e")
    # Create about label
    about_label = Label(
        about_window,
        text="Devlopper: Sba3i\nVersion: v1.0\n\nPassword generator is an app for create a powerful password for protect your account",
        height=8,
        font=("Arial", 12),
    )
    about_label.grid(row=1, column=1, columnspan=2, padx=20, pady=30)
    about_label.config(fg="#ffffff", bg="#1e1e1e")
    # Create exit button
    close_button = Button(
        about_window,
        text="Close",
        width=20,
        height=2,
        borderwidth=0,
        fg="#dce4ee",
        bg="#1f6aa5",
        activeforeground="#000000",
        activebackground="#ff0000",
        command=about_window.destroy,
    )
    close_button.grid(row=2, column=1, columnspan=2, pady=30)
    # Running window
    about_window.mainloop()


# Exit event function
def exit_event(event):
    app.quit()


# File Menu
file_casecade = Menu(app_menu, tearoff=False)
app_menu.add_cascade(label="File", menu=file_casecade)
file_casecade.add_command(label="New                Ctrl+N", command=new)
file_casecade.add_command(label="Save                Ctrl+S", command=save)
file_casecade.add_separator()
file_casecade.add_command(label="Exit                  Ctrl+Q", command=app.quit)
file_casecade.config(fg="#ffffff", bg="#323233")

# Edit Menu
edit_casecade = Menu(app_menu, tearoff=False)
app_menu.add_cascade(label="Edit", menu=edit_casecade)
edit_casecade.add_command(label="Copy", command=copy)
edit_casecade.config(fg="#ffffff", bg="#323233")


# Help Menu
help_casecade = Menu(app_menu, tearoff=False)
app_menu.add_cascade(label="Help", menu=help_casecade)
help_casecade.add_command(label="About                    ", command=about)
help_casecade.config(fg="#ffffff", bg="#323233")

# Generate button
generate_button = Button(
    app,
    text="Generate",
    width=20,
    height=2,
    borderwidth=0,
    fg="#dce4ee",
    bg="#1f6aa5",
    activeforeground="#dce4ee",
    activebackground="#144870",
    command=generate_password,
)
generate_button.grid(row=3, column=0, columnspan=3, padx=20, pady=50)

# Clear button
clear_button = Button(
    app,
    text="Clear",
    width=20,
    height=2,
    borderwidth=0,
    fg="#dce4ee",
    bg="#1f6aa5",
    activeforeground="#000000",
    activebackground="#ff0000",
    command=clear_label,
)
clear_button.grid(row=3, column=2, columnspan=3, padx=20, pady=50)

# Save button
save_button = Button(
    app,
    text="Save",
    width=20,
    height=2,
    borderwidth=0,
    fg="#dce4ee",
    bg="#1f6aa5",
    activeforeground="#dce4ee",
    activebackground="#144870",
    command=save,
)
save_button.grid(row=5, column=0, columnspan=3, pady=50)

# Copy button
copy_button = Button(
    app,
    text="Copy",
    width=20,
    height=2,
    borderwidth=0,
    fg="#dce4ee",
    bg="#1f6aa5",
    activeforeground="#dce4ee",
    activebackground="#144870",
    command=copy,
)
copy_button.grid(row=5, column=1, columnspan=3, pady=50)

# Exit button
exit_button = Button(
    app,
    text="Exit",
    width=20,
    height=2,
    borderwidth=0,
    fg="#dce4ee",
    bg="#1f6aa5",
    activeforeground="#000000",
    activebackground="#ff0000",
    command=app.quit,
)
exit_button.grid(row=5, column=2, columnspan=3, padx=50, pady=50, sticky=E)

# New key event
app.bind("<Control-n>", new_event)

# Save key event
app.bind("<Control-s>", save_event)

# Generate key event
app.bind("<Return>", generate_password_event)

# Exit key event
app.bind("<Control-q>", exit_event)

# Running app
app.mainloop()
