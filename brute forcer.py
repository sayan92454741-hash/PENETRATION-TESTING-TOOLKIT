import tkinter as tk
from tkinter import ttk, messagebox
import time
import threading


# ----------- DEMO LOGIN CHECK ------------
# This is a mock login system for safe testing.
# The "correct" password is stored locally.
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "pass2"


def brute_force(username, passwords, output_box):
    output_box.insert(tk.END, "Starting brute-force (demo mode)...\n\n")
    output_box.see(tk.END)

    for pw in passwords:
        output_box.insert(tk.END, f"Trying {username}:{pw}\n")
        output_box.see(tk.END)
        time.sleep(0.5)  # slow down for visibility (also safe)

        if username == CORRECT_USERNAME and pw == CORRECT_PASSWORD:
            output_box.insert(tk.END, f"\nSUCCESS! Password found: {pw}\n", "success")
            output_box.see(tk.END)
            return

    output_box.insert(tk.END, "\nFinished. Password not found.\n", "fail")
    output_box.see(tk.END)


def start_bruteforce():
    username = entry_user.get()
    wordlist = entry_wordlist.get().split(",")

    if not username or not wordlist:
        messagebox.showwarning("Input Error", "Please enter all fields!")
        return

    output_box.delete(1.0, tk.END)

    thread = threading.Thread(target=brute_force, args=(username, wordlist, output_box))
    thread.start()


# ---------------- GUI ------------------

root = tk.Tk()
root.title("Brute-Forcer (Demo Mode)")
root.geometry("500x450")
root.resizable(False, False)

title = tk.Label(root, text="Brute-Forcer (Safe Demo)", font=("Arial", 18, "bold"))
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Username:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
entry_user = tk.Entry(frame, width=25, font=("Arial", 12))
entry_user.grid(row=0, column=1)

tk.Label(frame, text="Passwords (comma-separated):", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=10)
entry_wordlist = tk.Entry(frame, width=25, font=("Arial", 12))
entry_wordlist.grid(row=1, column=1)

start_button = tk.Button(root, text="Start Brute-Force", font=("Arial", 14), width=20, command=start_bruteforce)
start_button.pack(pady=10)

output_box = tk.Text(root, height=15, width=58, bg="black", fg="lime", font=("Consolas", 11))
output_box.tag_config("success", foreground="yellow")
output_box.tag_config("fail", foreground="red")
output_box.pack(pady=10)

root.mainloop()
