import tkinter as tk
from tkinter import filedialog
import os

# ---- Dosya Tipi Motoru ----
FILE_TYPES = {
    "image": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
    "video": [".mp4", ".avi", ".mkv"],
    "music": [".mp3", ".wav"],
    "text":  [".txt", ".md"],
    "code":  [".py", ".c", ".cpp", ".js", ".html", ".css"],
    "system": [".exe", ".dll"],
}

FILE_COLORS = {
    "image": "#4FC3F7",
    "video": "#FFB74D",
    "music": "#BA68C8",
    "text":  "#E0E0E0",
    "code":  "#81C784",
    "system": "#E57373",
    "unknown": "#9E9E9E"
}

def detect_file_type(filename):
    ext = os.path.splitext(filename)[1].lower()
    for ftype, exts in FILE_TYPES.items():
        if ext in exts:
            return ftype
    return "unknown"

# ---- GUI ----
class ArexExplorer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ArexOS File Explorer")
        self.root.geometry("700x450")
        self.root.configure(bg="#1e1e1e")

        top = tk.Frame(self.root, bg="#111", height=40)
        top.pack(fill="x")

        btn = tk.Button(top, text="📁 Klasör Aç", command=self.open_folder)
        btn.pack(side="left", padx=10, pady=5)

        self.path_label = tk.Label(top, text="Klasör seçilmedi", fg="white", bg="#111")
        self.path_label.pack(side="left", padx=10)

        self.listbox = tk.Listbox(
            self.root,
            bg="#1e1e1e",
            fg="white",
            font=("Consolas", 11),
            selectbackground="#333"
        )
        self.listbox.pack(fill="both", expand=True, padx=10, pady=10)

    def open_folder(self):
        folder = filedialog.askdirectory()
        if not folder:
            return

        self.path_label.config(text=folder)
        self.listbox.delete(0, tk.END)

        try:
            files = os.listdir(folder)
        except PermissionError:
            self.listbox.insert(tk.END, "Erişim reddedildi")
            return

        for f in files:
            ftype = detect_file_type(f)
            color = FILE_COLORS.get(ftype, "#9E9E9E")

            self.listbox.insert(tk.END, f" {f}   [{ftype}]")
            self.listbox.itemconfig(tk.END, fg=color)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    ArexExplorer().run()
