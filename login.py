import tkinter as tk

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == "user" and password == "password":
        message_label.config(text="Login successful!", fg="green")
    else:
        message_label.config(text="Login failed. Please try again.", fg="red")
    
    # Clear the password entry for security
    password_entry.delete(0, 'end')

# Create the main window
root = tk.Tk()
root.title("Login Form")
root.geometry("300x300")  # Adjusted the height

# Create username label and entry
username_label = tk.Label(root, text="Username", fg="red", pady="12", font="oblique, 12")
username_label.pack()
username_entry = tk.Entry(root, font=("Arial", 12))
username_entry.pack()

# Create password label and entry
password_label = tk.Label(root, text="Password", fg="red", pady="12", font="oblique, 12")
password_label.pack()
password_entry = tk.Entry(root, show="*", font=("Arial", 12))
password_entry.pack()

# Create a login button with a different background color
login_button = tk.Button(root, text="Login", command=login, fg="red", font="oblique, 12", bg="lightblue")
login_button.pack()

# Create a label to display login status
message_label = tk.Label(root, text="", font=("Arial", 12))
message_label.pack()

# Start the main loop
root.mainloop()
