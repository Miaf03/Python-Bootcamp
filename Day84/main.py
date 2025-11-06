import os
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

root = Tk()
root.title("Image Watermark App")
root.config(padx=20, pady=20, bg="#0d1117")

img_path = None
img_preview = None

def select_image():
    """Open file dialog to choose an image"""
    global img_path, img_preview
    img_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
    )

    if not img_path:
        return

    img = Image.open(img_path)
    img.thumbnail((400, 300))
    img_preview = ImageTk.PhotoImage(img)
    canvas.create_image(200, 150, image=img_preview)
    canvas.image = img_preview

    messagebox.showinfo("Image loaded", "Your image has been loaded successfully!")


def add_watermark():
    """Add a watermark text to the selected image."""
    global img_path
    if not img_path:
        messagebox.showwarning("Error", "Please select an image first")
        return

    text = watermark_entry.get().strip()
    if not text:
        messagebox.showwarning("Error", "Please enter watermark text")
        return

    try:
        image = Image.open(img_path).convert("RGBA")
        width, height = image.size

        txt_layer = Image.new("RGBA", image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(txt_layer)

        font_size = int(height * 0.07)
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            font = ImageFont.load_default()

        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = width - text_width - 30
        y = height - text_height - 30

        draw.text((x+2, y+2), text, font=font, fill=(0, 0, 0, 120))
        draw.text((x, y), text, font=font, fill=(255, 255, 255, 200))

        watermarked = Image.alpha_composite(image, txt_layer).convert("RGB")

        base, ext = os.path.splitext(img_path)
        output_path = f"{base}_watermarked{ext}"
        watermarked.save(output_path)

        messagebox.showinfo("Success", f"Watermark added successfully!\nSaved as:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")


title_label = Label(root, text="Image Watermark App", font=("Arial", 22, "bold"), fg="#58a6ff", bg="#0d1117")
title_label.grid(row=0, column=0, columnspan=3, pady=10)

canvas = Canvas(width=400, height=300, bg="#161b22", highlightthickness=0)
canvas.grid(row=1, column=0, columnspan=3, pady=15)

btn_select = Button(root, text="Select Image", command=select_image,
                    bg="#238636", fg="black", font=("Arial", 12, "bold"), width=15, relief="flat")
btn_select.grid(row=2, column=0, pady=10)

watermark_entry = Entry(root, width=30, bg="#21262d", fg="#c9d1d9",
                        insertbackground="#c9d1d9", font=("Arial", 12), justify="center")
watermark_entry.insert(0, "Your watermark text")
watermark_entry.grid(row=2, column=1, padx=10)

btn_apply = Button(root, text="Add Watermark", command=add_watermark,
                   bg="#1f6feb", fg="black", font=("Arial", 12, "bold"), width=15, relief="flat")
btn_apply.grid(row=2, column=2, pady=10)

root.mainloop()