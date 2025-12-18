import tkinter as tk
from tkinter import filedialog

def open_file():
    file = filedialog.askopenfile(mode='r')
    if file:
        text.delete(1.0, tk.END)
        text.insert(tk.END, file.read())
        file.close()

def save_file():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if file:
        file.write(text.get(1.0, tk.END))
        file.close()

root = tk.Tk()
root.title("ArexPad")
root.geometry("800x500")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Dosya", menu=file_menu)
file_menu.add_command(label="Aç", command=open_file)
file_menu.add_command(label="Kaydet", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Çıkış", command=root.quit)

text = tk.Text(root, font=("Consolas", 12))
text.pack(expand=True, fill="both")

root.mainloop()
