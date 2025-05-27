import os
from tkinter import filedialog
from PIL import Image
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class ImageCompressorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Image Compressor")
        self.geometry("500x300")
        self.selected_image_path = None
        self.compressed_image = None
        self.create_widgets()

    def create_widgets(self):
        self.select_button = ctk.CTkButton(self, text="Select Image", command=self.select_image)
        self.select_button.pack(pady=20)

        self.compress_button = ctk.CTkButton(self, text="Compress Image", command=self.compress_image, state="disabled")
        self.compress_button.pack(pady=10)

        self.size_label = ctk.CTkLabel(self, text="Compressed Image Size: N/A")
        self.size_label.pack(pady=5)

        self.download_button = ctk.CTkButton(self, text="Save Compressed Image", command=self.save_image, state="disabled")
        self.download_button.pack(pady=10)

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Images", "*.jpg *.jpeg *.png")])
        if file_path:
            self.selected_image_path = file_path
            self.compress_button.configure(state="normal")

    def compress_image(self):
        if not self.selected_image_path:
            return
        img = Image.open(self.selected_image_path)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        output_path = "compressed_temp.jpg"
        img.save(output_path, "JPEG", quality=40, optimize=True)
        self.compressed_image = output_path
        size_kb = os.path.getsize(output_path) // 1024
        self.size_label.configure(text=f"Compressed Image Size: {size_kb} KB")
        self.download_button.configure(state="normal")

    def save_image(self):
        if not self.compressed_image:
            return
        save_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                                 filetypes=[("JPEG", "*.jpg")])
        if save_path:
            os.replace(self.compressed_image, save_path)
            self.size_label.configure(text="Image saved successfully.")

if __name__ == "__main__":
    app = ImageCompressorApp()
    app.mainloop()
