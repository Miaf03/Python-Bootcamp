import os
import shutil
import hashlib
from datetime import datetime

BASE_DIR = "Day97"
TARGET_BASE = os.path.join(BASE_DIR, "MisArchivos")
LOG_FILE = os.path.join(BASE_DIR, "logs.txt")

CATEGORIES = {
    "Imagenes": [".png", ".jpg", ".jpeg", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".md"],
    "Videos": [".mp4", ".mov", ".mkv"],
    "Comprimidos": [".zip", ".rar", ".7z"]
}

def log(message):
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")
    print(message)

def file_hash(filepath):
    h = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def detect_category(ext):
    for cat, exts in CATEGORIES.items():
        if ext.lower() in exts:
            return cat
    return "Otros"

def organize_files():
    log("Iniciando organización")

    os.makedirs(TARGET_BASE, exist_ok=True)
    seen_hashes = {}

    for filename in os.listdir(BASE_DIR):
        path = os.path.join(BASE_DIR, filename)

        if filename in ["main.py", "logs.txt", "MisArchivos"]:
            continue

        if not os.path.isfile(path):
            continue

        _, ext = os.path.splitext(filename)

        category = detect_category(ext)

        file_md5 = file_hash(path)
        if file_md5 in seen_hashes:
            log(f"Duplicado eliminado: {filename}")
            os.remove(path)
            continue
        else:
            seen_hashes[file_md5] = filename

        created_ts = os.path.getmtime(path)
        created_date = datetime.fromtimestamp(created_ts)
        month_name = created_date.strftime("%B")

        category_dir = os.path.join(TARGET_BASE, category)
        month_dir = os.path.join(category_dir, month_name)

        os.makedirs(month_dir, exist_ok=True)

        target_path = os.path.join(month_dir, filename)
        shutil.move(path, target_path)
        log(f"Movido: {filename} → {category}/{month_name}")

    log("Organización completada")

if __name__ == "__main__":
    organize_files()