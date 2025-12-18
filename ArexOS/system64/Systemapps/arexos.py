import os
import tkinter as tk
from tkinter import ttk

# -----------------------------
# ArexOS Core
# -----------------------------

APP_NAME = "ArexOS - Dosya Gezgini"
START_DIR = os.path.expanduser("~")  # Kullanıcı klasörü

FILE_TYPES = {
    ".txt": "📄 Metin",
    ".py": "🐍 Python",
    ".exe": "⚙️ Uygulama",
    ".jpg": "🖼️ Resim",
    ".png": "🖼️ Resim",
    ".mp4": "🎬 Video",
    ".mp3": "🎵 Müzik",
    ".pdf": "📕 PDF",
}

def get_file_type(filename):
    ext = os.path.splitext(filename)[1].lower()
    return FILE_TYPES.get(ext, "📦 Dosya")

# -----------------------------
# UI
# -----------------------------

class ArexOS(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_NAME)
        self.geometry("700x450")

        self.path_label = tk.Label(self, text=START_DIR, anchor="w")
        self.path_label.pack(fill="x", padx=10, pady=5)

        self.tree = ttk.Treeview(self, columns=("type",), show="headings")
        self.tree.heading("type", text="Tür")
        self.tree.pack(fill="both", expand=True, padx=10, pady=5)

        self.load_directory(START_DIR)

    def load_directory(self, path):
        self.tree.delete(*self.tree.get_children())
        self.path_label.config(text=path)

        try:
            for item in os.listdir(path):
                full_path = os.path.join(path, item)
                if os.path.isdir(full_path):
                    self.tree.insert("", "end", values=("📁 Klasör",), text=item)
                else:
                    ftype = get_file_type(item)
                    self.tree.insert("", "end", values=(ftype,), text=item)
        except PermissionError:
            self.tree.insert("", "end", values=("⛔ Erişim Yok",))

# -----------------------------
# Start
# -----------------------------

if __name__ == "__main__":
    print("[ArexOS] Sistem baslatildi")
    app = ArexOS()
    app.mainloop()
