import tkinter as tk
root = tk.Tk()
root.title("Login Panel")
root.geometry("300x200")
user_label = tk.Label(root, text="Username:")
user_label.pack()
user_entry = tk.Entry(root)
user_entry.pack()
pass_label = tk.Label(root, text="Password:")
pass_label.pack()
pass_entry = tk.Entry(root, show="*")
pass_entry.pack()
def login():
    username = user_entry.get()
    password = pass_entry.get()
    correct_user = "admin"
    correct_pass = "1234"
    if username == correct_user and password == correct_pass:
        tk.messagebox.showinfo(title="Login Successful", message="You have logged in successfully")
    else:
        tk.messagebox.showerror(title="Login Failed", message="Invalid username or password")
login_button = tk.Button(root, text="Login", command=login)
login_button.pack()
root.mainloop()
