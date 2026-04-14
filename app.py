import tkinter as tk
from tkinter import ttk
from scanner import run_scan
from report import generate_report

# -----------------------------
# Function to Start Scan
# -----------------------------
def start_scan():
    target = entry.get()
    output.delete(1.0, tk.END)
    
    output.insert(tk.END, "🔍 Starting scan...\n\n")
    root.update()

    results = run_scan(target)

    for res in results:
        output.insert(tk.END, res + "\n")

    generate_report(results)

    output.insert(tk.END, "\n✅ Scan Completed! Report saved as report.pdf")


# -----------------------------
# GUI Setup
# -----------------------------
root = tk.Tk()
root.title("Cyber Security Scanner Pro")
root.geometry("700x500")
root.configure(bg="#1e1e1e")

# -----------------------------
# Title
# -----------------------------
title = tk.Label(
    root,
    text="🔐 Cyber Security Scanner",
    font=("Helvetica", 18, "bold"),
    fg="white",
    bg="#1e1e1e"
)
title.pack(pady=10)

# -----------------------------
# Input Frame
# -----------------------------
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=10)

tk.Label(
    frame,
    text="Target Website:",
    font=("Helvetica", 12),
    fg="white",
    bg="#1e1e1e"
).grid(row=0, column=0, padx=5)

entry = tk.Entry(frame, width=40, font=("Helvetica", 12))
entry.grid(row=0, column=1, padx=5)

scan_btn = tk.Button(
    frame,
    text="Start Scan",
    command=start_scan,
    bg="#007acc",
    fg="white",
    font=("Helvetica", 11, "bold"),
    padx=10,
    pady=5
)
scan_btn.grid(row=0, column=2, padx=10)

# -----------------------------
# Output Box (Terminal Style)
# -----------------------------
output = tk.Text(
    root,
    height=20,
    width=80,
    bg="#0f0f0f",
    fg="#00ff00",
    font=("Consolas", 10)
)
output.pack(pady=10)

# -----------------------------
# Run App
# -----------------------------
root.mainloop()