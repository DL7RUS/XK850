import tkinter as tk
from functools import partial

# test ist immer gut

def button_click(value):
    if value == "ENT":
        # Hier die Logik für die Eingabebehandlung implementieren
        print(f"Eingabe: {entry.get()}")
        entry.delete(0, tk.END)  # Eingabefeld löschen
    else:
        entry.insert(tk.END, value)  # Fügt den Wert am Ende der aktuellen Eingabe hinzu

root = tk.Tk()
root.title("Kommando-Sender")
root.geometry("800x480")  # Für Landscape-Format

frame = tk.Frame(root)
frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

entry = tk.Entry(frame, font=("Helvetica", 18))
entry.grid(row=0, column=0, columnspan=3, pady=(0, 20), sticky="ew")

# Ziffernblock
buttons = [
    "AME", "USB", "LSB",
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9",
    ".", "0", "ENT"
]

for i, button in enumerate(buttons):
    tk.Button(frame, text=button, font=("Helvetica", 18), command=partial(button_click, button)).grid(row=1+i//3, column=i%3, sticky="ewns", padx=5, pady=5)

# Zusätzliche Tasten
extra_buttons = ["EXT", "BFO", "CH", "FRQ"]
for i, button in enumerate(extra_buttons):
    tk.Button(frame, text=button, font=("Helvetica", 18), command=partial(button_click, button)).grid(row=1+i, column=3, sticky="ewns", padx=(20, 0), pady=5)

# Anpassungen für Layout
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)
for i in range(5):
    frame.rowconfigure(i, weight=1)

root.mainloop()
