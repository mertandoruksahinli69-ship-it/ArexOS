import os
import tkinter as tk
from tkinter import filedialog

# Dosya tipleri
FILE_TYPES = {
    "image": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
    "video": [".mp4", ".avi", ".mkv"],
    "audio": [".mp3", ".wav", ".ogg"],
    "text":  [".txt", ".md", ".log"],
    "code":  [".py", ".js", ".java", ".cpp", ".c", ".html", ".css"]
}

ICONS = {
    "folder": "📁",
    "image": "🖼️",
    "video": "🎬",
    "audio": "🎵",
    "text":  "📄",
    "code":  "💻",
    "other": "⚙️"
}

current_path = os.path.expanduser("~")

def get_type(filename):
    ext = os.path.splitext(filename)[1].lower()
    for t, exts in FILE_TYPES.items():
        if ext in exts:
            return t
    return "other"

def refresh():
    listbox.delete(0, tk.END)
    path_label.config(text=current_path)

    try:
        items = os.listdir(current_path)
    except PermissionError:
        return

    folders = []
    files = []

    for item in items:
        full = os.path.join(current_path, item)
        if os.path.isdir(full):
            folders.append(item)
        else:
            files.append(item)

    # Önce klasörler
    for f in sorted(folders):
        listbox.insert(tk.END, f"{ICONS['folder']}  {f}")

    # Sonra dosyalar
    for f in sorted(files):
        ftype = get_type(f)
        icon = ICONS.get(ftype, ICONS["other"])
        listbox.insert(tk.END, f"{icon}  {f}")

def open_item(event):
    global current_path
    if not listbox.curselection():
        return

    name = listbox.get(listbox.curselection())
    real_name = name[3:]  # emoji + boşlukları kes
    new_path = os.path.join(current_path, real_name)

    if os.path.isdir(new_path):
        current_path = new_path
        refresh()

def go_up():
    global current_path
    parent = os.path.dirname(current_path)
    if parent != current_path:
        current_path = parent
        refresh()

def choose_folder():
    global current_path
    folder = filedialog.askdirectory()
    if folder:
        current_path = folder
        refresh()

# --- UI ---
root = tk.Tk()
root.title("ArexExplorer")
root.geometry("750x520")

top = tk.Frame(root)
top.pack(fill="x")

tk.Button(top, text="⬆ Yukarı", command=go_up).pack(side="left", padx=5)
tk.Button(top, text="📁 Klasör Seç", command=choose_folder).pack(side="left")

path_label = tk.Label(root, anchor="w")
path_label.pack(fill="x")

listbox = tk.Listbox(root, font=("Consolas", 11))
listbox.pack(expand=True, fill="both")
listbox.bind("<Double-1>", open_item)

refresh()
root.mainloop()
