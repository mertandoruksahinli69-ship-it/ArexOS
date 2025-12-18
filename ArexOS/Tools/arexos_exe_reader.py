import tkinter as tk
from tkinter import filedialog, messagebox
import os, struct, subprocess

# -------- Dosya Tipi Motoru --------
FILE_TYPES = {
    "image": [".png", ".jpg", ".jpeg", ".gif"],
    "video": [".mp4", ".avi", ".mkv"],
    "music": [".mp3", ".wav"],
    "text":  [".txt", ".md"],
    "code":  [".py", ".c", ".cpp", ".js"],
    "system": [".exe"]
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

def detect_file_type(name):
    ext = os.path.splitext(name)[1].lower()
    for t, exts in FILE_TYPES.items():
        if ext in exts:
            return t
    return "unknown"

# -------- GUI --------
class ArexOS:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ArexOS Explorer")
        self.root.geometry("900x500")
        self.root.configure(bg="#1e1e1e")

        top = tk.Frame(self.root, bg="#111", height=40)
        top.pack(fill="x")
        tk.Button(top, text="📁 Klasör Aç", command=self.open_folder).pack(side="left", padx=10)
        self.path_lbl = tk.Label(top, text="Klasör yok", fg="white", bg="#111")
        self.path_lbl.pack(side="left")

        main = tk.PanedWindow(self.root, sashrelief="raised")
        main.pack(fill="both", expand=True)

        self.listbox = tk.Listbox(main, bg="#1e1e1e", fg="white", font=("Consolas", 11))
        self.preview = tk.Text(main, bg="#111", fg="lime", font=("Consolas", 11))
        main.add(self.listbox, width=350)
        main.add(self.preview)

        self.listbox.bind("<Button-3>", self.right_click)

        self.menu = tk.Menu(self.root, tearoff=0)
        self.menu.add_command(label="Aç / Önizle", command=self.open_item)
        self.menu.add_command(label="EXE Bilgi", command=self.exe_info)
        self.menu.add_command(label="EXE Çalıştır", command=self.run_exe)

        self.current_folder = ""
        self.files = []

    def open_folder(self):
        folder = filedialog.askdirectory()
        if not folder: return
        self.current_folder = folder
        self.path_lbl.config(text=folder)
        self.listbox.delete(0, tk.END)
        self.preview.delete("1.0", tk.END)

        self.files = os.listdir(folder)
        for f in self.files:
            t = detect_file_type(f)
            self.listbox.insert(tk.END, f" {f} [{t}]")
            self.listbox.itemconfig(tk.END, fg=FILE_COLORS[t])

    def selected_file(self):
        try:
            idx = self.listbox.curselection()[0]
            return os.path.join(self.current_folder, self.files[idx])
        except:
            return None

    def open_item(self):
        path = self.selected_file()
        if not path: return
        ext = os.path.splitext(path)[1].lower()
        self.preview.delete("1.0", tk.END)

        if ext in [".txt", ".py", ".md"]:
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    self.preview.insert(tk.END, f.read())
            except Exception as e:
                self.preview.insert(tk.END, str(e))
        else:
            self.preview.insert(tk.END, "Önizleme yok.")

    def exe_info(self):
        path = self.selected_file()
        if not path or not path.lower().endswith(".exe"): return
        self.preview.delete("1.0", tk.END)
        try:
            with open(path, "rb") as f:
                if f.read(2) != b"MZ":
                    self.preview.insert(tk.END, "Geçersiz EXE")
                    return
                f.seek(0x3C)
                pe = struct.unpack("<I", f.read(4))[0]
                f.seek(pe + 4)
                machine = struct.unpack("<H", f.read(2))[0]
                arch = "x64" if machine == 0x8664 else "x86" if machine == 0x014c else "Bilinmeyen"
                self.preview.insert(tk.END, f"EXE Bilgi\nMimari: {arch}\nBoyut: {os.path.getsize(path)} byte")
        except Exception as e:
            self.preview.insert(tk.END, str(e))

    def run_exe(self):
        path = self.selected_file()
        if not path or not path.lower().endswith(".exe"): return
        if messagebox.askyesno("EXE Çalıştır", "Program çalıştırılsın mı?"):
            subprocess.Popen(path)

    def right_click(self, e):
        self.listbox.selection_clear(0, tk.END)
        self.listbox.selection_set(self.listbox.nearest(e.y))
        self.menu.tk_popup(e.x_root, e.y_root)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    ArexOS().run()
