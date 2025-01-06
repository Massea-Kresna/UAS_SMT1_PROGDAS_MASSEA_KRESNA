import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

def hitung_tagihan_listrik():
    golongan = golongan_var.get()
    daya = daya_var.get()
    try:
        pemakaian = int(entry_pemakaian.get())
    except ValueError:
        result_label.config(text="Pemakaian harus berupa angka!")
        return

    tarif = {
        ("R1", 1300): 800,
        ("R1", 2200): 1300,
        ("R2", 3500): 1500
    }

    key = (golongan, int(daya))
    if key not in tarif:
        result_label.config(text="Golongan atau daya tidak valid.")
        return

    tarif_per_kwh = tarif[key]
    tagihan = tarif_per_kwh * pemakaian
    result_label.config(text=f"Tagihan listrik Anda: Rp{tagihan:,}")

def update_daya_options(*args):
    golongan = golongan_var.get()
    if golongan == "R1":
        daya_menu["values"] = [1300, 2200]
        daya_var.set(1300)
    elif golongan == "R2":
        daya_menu["values"] = [3500]
        daya_var.set(3500)
    else:
        daya_menu["values"] = []
        daya_var.set("")

root = tk.Tk()
root.title("Hitung Tagihan Listrik")

canvas = tk.Canvas(root, width=300, height=200)
canvas.grid(row=0, column=0, rowspan=5, columnspan=2, sticky="nsew")

bg_image = PhotoImage(file="image.png")
canvas.create_image(0, 0, anchor="nw", image=bg_image)

golongan_var = tk.StringVar()
daya_var = tk.StringVar()

golongan_var.trace("w", update_daya_options)

tk.Label(root, text="Golongan:").grid(row=1, column=0, padx=10, pady=5)
golongan_menu = ttk.Combobox(root, textvariable=golongan_var, state="readonly")
golongan_menu["values"] = ["R1", "R2"]
golongan_menu.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Daya:").grid(row=2, column=0, padx=10, pady=5)
daya_menu = ttk.Combobox(root, textvariable=daya_var, state="readonly")
daya_menu.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Pemakaian (kWh):").grid(row=3, column=0, padx=10, pady=5)
entry_pemakaian = tk.Entry(root)
entry_pemakaian.grid(row=3, column=1, padx=10, pady=5)

tk.Button(root, text="Hitung", command=hitung_tagihan_listrik).grid(row=4, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()