import os

FILE_TYPES = {
    "image": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
    "video": [".mp4", ".avi", ".mkv"],
    "music": [".mp3", ".wav"],
    "text":  [".txt", ".md"],
    "code":  [".py", ".c", ".cpp", ".js", ".html", ".css"],
    "system": [".exe", ".dll"],
}

def detect_file_type(filename):
    ext = os.path.splitext(filename)[1].lower()

    for file_type, extensions in FILE_TYPES.items():
        if ext in extensions:
            return file_type

    return "unknown"
test_files = [
    "foto.png",
    "video.mp4",
    "muzik.mp3",
    "notlar.txt",
    "kernel.c",
    "arex.exe",
    "garip.xyz"
]

for f in test_files:
    print(f, "→", detect_file_type(f))
FILE_COLORS = {
    "image": "lightblue",
    "video": "orange",
    "music": "purple",
    "text":  "white",
    "code":  "lime",
    "system": "red",
    "unknown": "gray"
}
for filename in test_files:
    file_type = detect_file_type(filename)
    print(filename, "→", file_type)