import tkinter as tk
from tkinter import messagebox

# Global user store
users = {
    "admin": "admin123",
    "user1": "pass1"
}

# Main app window
root = tk.Tk()
root.title("Grand Prix Ticketing System")
root.geometry("800x800")

# Functions


def login():
    username = username_entry.get()
    password = password_entry.get()

    if username in users and users[username] == password:
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def open_register_window():
    def register_user():
        new_user = entry_username.get()
        new_pass = entry_password.get()

        if new_user in users:
            messagebox.showerror("Error", "Username already exists.")
        elif not new_user or not new_pass:
            messagebox.showerror("Error", "Fields cannot be empty.")
        else:
            users[new_user] = new_pass
            messagebox.showinfo("Success", f"Account created for {new_user}.")
            reg_window.destroy()

    reg_window = tk.Toplevel(root)
    reg_window.title("Create Account")
    reg_window.geometry("300x200")

    tk.Label(reg_window, text="New Username:").pack()
    entry_username = tk.Entry(reg_window)
    entry_username.pack()

    tk.Label(reg_window, text="New Password:").pack()
    entry_password = tk.Entry(reg_window, show="*")
    entry_password.pack()

    tk.Button(reg_window, text="Register", command=register_user).pack(pady=10)

def open_tickets_window():
    ticket_window = tk.Toplevel(root)
    ticket_window.title("View Tickets")
    ticket_window.geometry("300x250")

    tk.Label(ticket_window, text="Available Tickets", font=("Arial", 14)).pack(pady=10)

    tickets = [
        "1. Single Race - 100 AED",
        "2. Weekend Pass - 250 AED",
        "3. Season Membership - 800 AED",
        "4. Group Discount - 20% off (min. 4 people)"
    ]

    for t in tickets:
        tk.Label(ticket_window, text=t).pack(anchor="w", padx=20)

def open_admin_dashboard():
    admin_window = tk.Toplevel(root)
    admin_window.title("Admin Dashboard")
    admin_window.geometry("300x200")

    tk.Label(admin_window, text="Admin Controls", font=("Arial", 14)).pack(pady=10)
    tk.Label(admin_window, text="- Track Sales").pack(anchor="w", padx=20)
    tk.Label(admin_window, text="- Modify Discounts").pack(anchor="w", padx=20)
    tk.Label(admin_window, text="- Manage Inventory").pack(anchor="w", padx=20)

def exit_app():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        root.destroy()

# UI Layout


tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Login", width=20, command=login).pack(pady=5)
tk.Button(root, text="Create Account", width=20, command=open_register_window).pack(pady=5)
tk.Button(root, text="View Tickets", width=20, command=open_tickets_window).pack(pady=5)
tk.Button(root, text="Admin Dashboard", width=20, command=open_admin_dashboard).pack(pady=5)
tk.Button(root, text="Exit", width=20, command=exit_app).pack(pady=10)

root.mainloop()
