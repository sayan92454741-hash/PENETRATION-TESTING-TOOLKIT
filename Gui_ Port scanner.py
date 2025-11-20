import socket
import threading
import tkinter as tk
from tkinter import ttk, messagebox


def scan_port(host, port, result_box):
    """Scan a single port"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        sock.connect((host, port))
        result_box.insert(tk.END, f"[OPEN]  Port {port}\n")
    except:
        pass
    finally:
        sock.close()


def start_scan():
    """Start scanning process"""
    host = entry_host.get()
    port_range = entry_ports.get()

    if not host or not port_range:
        messagebox.showwarning("Input Error", "Please enter host and port range!")
        return

    try:
        start_port, end_port = map(int, port_range.split("-"))
    except:
        messagebox.showerror("Format Error", "Port range must be like 1-1000")
        return

    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, f"Scanning {host} from {start_port} to {end_port}...\n\n")

    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(host, port, result_box))
        thread.start()


# ------------------------- GUI ----------------------------

root = tk.Tk()
root.title("Port Scanner Tool")
root.geometry("500x450")
root.resizable(False, False)

title = tk.Label(root, text="Port Scanner", font=("Arial", 20, "bold"))
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="Target IP / Domain:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
entry_host = tk.Entry(frame, font=("Arial", 12), width=25)
entry_host.grid(row=0, column=1)

tk.Label(frame, text="Port Range (ex: 1-500):", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=10)
entry_ports = tk.Entry(frame, font=("Arial", 12), width=25)
entry_ports.grid(row=1, column=1)

scan_button = tk.Button(root, text="Start Scan", font=("Arial", 14), width=20, command=start_scan)
scan_button.pack(pady=10)

result_box = tk.Text(root, height=15, width=58, bg="black", fg="lime", font=("Consolas", 11))
result_box.pack(pady=10)

root.mainloop()
