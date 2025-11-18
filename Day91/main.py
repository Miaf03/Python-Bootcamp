# ============================================================
# Generador de Paleta de Colores
# ============================================================

import os
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from tkinter import filedialog, messagebox

# ============================================================
# CONFIGURACIÓN GENERAL
# ============================================================

PALETTE_SIZE = 10
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

BG = "#1e1e1e"
FG = "#f0f0f0"
BTN = "#3c3c3c"
ACCENT = "#007acc"


# ============================================================
# FUNCIONES DE PROCESAMIENTO
# ============================================================

def rgb_to_hex(rgb):
    """Convierte un valor RGB en formato hexadecimal"""
    return "#{:02x}{:02x}{:02x}".format(*rgb)


def get_most_common_colours(image_path, top_n=10):
    """Obtiene los colores más comunes de una imagen"""
    img = Image.open(image_path).convert("RGB")
    img_small = img.resize((150, 150))
    pixels = np.array(img_small).reshape(-1, 3)

    unique, counts = np.unique(pixels, axis=0, return_counts=True)
    sorted_idx = np.argsort(counts)[::-1]

    colours = unique[sorted_idx][:top_n]
    counts = counts[sorted_idx][:top_n]

    return colours, counts


def generate_palette_image(colours):
    """Genera una imagen horizontal con bloques de colores"""
    block_width = 80
    palette = Image.new("RGB", (block_width * len(colours), 100))

    for i, col in enumerate(colours):
        block = Image.new("RGB", (block_width, 100), tuple(col))
        palette.paste(block, (i * block_width, 0))

    return palette


def generate_pdf(colours, counts, save_path):
    """Genera un reporte PDF con código RGB, Hexadecimales y porcentajes"""
    c = canvas.Canvas(save_path, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, height - 50, "Reporte de Paleta de Colores")

    y = height - 120

    c.setFont("Helvetica", 12)
    total = sum(counts)

    for rgb, count in zip(colours, counts):
        
        rgb = tuple(int(x) for x in rgb)
        hexcolor = rgb_to_hex(rgb)
        
        percentage = (count / total) * 100

        c.setFillColorRGB(rgb[0]/255, rgb[1]/255, rgb[2]/255)
        c.rect(50, y - 10, 40, 40, fill=True)

        c.setFillColorRGB(0, 0, 0)
        c.drawString(100, y + 10, f"RGB: {tuple(rgb)}   HEX: {hexcolor}   {percentage:.2f}%")

        y -= 60

    c.save()


# ============================================================
# INTERFAZ GRÁFICA
# ============================================================

class ColourApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Paleta de Colores")
        self.root.geometry("780x630")
        self.root.config(bg=BG)

        self.image_path = None
        self.palette_img = None

        self.create_widgets()

    def create_widgets(self):

        # TÍTULO
        title = tk.Label(
            self.root,
            text="Generador de Paleta de Colores",
            font=("Arial", 20, "bold"),
            bg=BG,
            fg=FG
        )
        title.pack(pady=15)

        # PREVISUALIZACIÓN DE IMAGEN
        self.image_label = tk.Label(self.root, bg=BG)
        self.image_label.pack(pady=10)

        # BOTONES
        btn_frame = tk.Frame(self.root, bg=BG)
        btn_frame.pack(pady=10)

        style = ttk.Style()
        style.configure("TButton", font=("Arial", 12), padding=6)

        upload_btn = ttk.Button(btn_frame, text="Cargar Imagen", command=self.load_image)
        upload_btn.grid(row=0, column=0, padx=10)

        palette_btn = ttk.Button(btn_frame, text="Generar Paleta", command=self.process_image)
        palette_btn.grid(row=0, column=1, padx=10)

        pdf_btn = ttk.Button(btn_frame, text="Exportar PDF", command=self.export_pdf)
        pdf_btn.grid(row=0, column=2, padx=10)

        # PALETA RESULTANTE
        self.palette_label = tk.Label(self.root, bg=BG)
        self.palette_label.pack(pady=20)


    def load_image(self):
        """Carga una imagen desde el explorador"""
        path = filedialog.askopenfilename(
            title="Selecciona una imagen",
            filetypes=[("Imágenes", "*.png *.jpg *.jpeg *.bmp")]
        )
        if not path:
            return

        self.image_path = path

        img = Image.open(path).resize((350, 250))
        tk_img = ImageTk.PhotoImage(img)

        self.image_label.config(image=tk_img)
        self.image_label.image = tk_img


    def process_image(self):
        """Genera la paleta de colores a partir de la imagen cargada"""
        if not self.image_path:
            messagebox.showwarning("Advertencia", "Primero carga una imagen")
            return

        colours, counts = get_most_common_colours(self.image_path, PALETTE_SIZE)
        self.palette_img = generate_palette_image(colours)

        tk_palette = ImageTk.PhotoImage(self.palette_img)
        self.palette_label.config(image=tk_palette)
        self.palette_label.image = tk_palette

        self.colours = colours
        self.counts = counts


    def export_pdf(self):
        """Exporta la paleta generada a un archivo PDF"""
        if not self.palette_img:
            messagebox.showwarning("Advertencia", "Genera una paleta primero")
            return

        save_path = os.path.join(OUTPUT_DIR, "palette_report.pdf")
        generate_pdf(self.colours, self.counts, save_path)

        messagebox.showinfo("Éxito", f"PDF generado en:\n{save_path}")

# ============================================================
# EJECUCIÓN DE LA APLICACIÓN
# ============================================================

root = tk.Tk()
app = ColourApp(root)
root.mainloop()