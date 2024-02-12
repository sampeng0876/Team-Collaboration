import fitz
import tkinter as tk
from PIL import ImageTk, Image

class PDFCapture:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.doc = fitz.open(pdf_path)
        self.page = None
        self.rect = None
        self.selection_complete = False

        self.root = tk.Tk()
        self.canvas_width = 800
        self.canvas_height = 1000
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.start_selection)

        self.display_page(0)  # Display the first page initially

        self.root.mainloop()

    def display_page(self, page_number):
        self.page = self.doc.load_page(page_number)
        pix = self.page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img_width, img_height = img.size
        aspect_ratio = img_width / img_height

        # Adjust the size of the displayed image based on the canvas width and maintain the aspect ratio
        if img_width > self.canvas_width or img_height > self.canvas_height:
            if img_width > img_height:
                new_width = self.canvas_width
                new_height = int(new_width / aspect_ratio)
            else:
                new_height = self.canvas_height
                new_width = int(new_height * aspect_ratio)
            img = img.resize((new_width, new_height))

        self.img_tk = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor="nw", image=self.img_tk)

    def start_selection(self, event):
        self.rect = [event.x, event.y, event.x, event.y]
        self.canvas.bind("<B1-Motion>", self.track_selection)
        self.canvas.bind("<ButtonRelease-1>", self.end_selection)

    def track_selection(self, event):
        self.rect[2] = event.x
        self.rect[3] = event.y
        self.canvas.delete("selection")
        self.canvas.create_rectangle(*self.rect, outline="red", tags="selection")

    def end_selection(self, event):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.selection_complete = True
        self.root.destroy()

    def capture_data(self):
        if self.selection_complete:
            x0, y0, x1, y1 = self.rect
            x0, x1 = min(x0, x1), max(x0, x1)
            y0, y1 = min(y0, y1), max(y0, y1)
            rect = fitz.Rect(x0, y0, x1, y1)
            text = self.page.get_text("text", clip=rect)
            return text
        else:
            return None


# Usage example
pdf_file = r"C:\Users\bob08\Desktop\Team-Collaboration\PDF\unnyeo_elogistek.pdf"
pdf_capture = PDFCapture(pdf_file)
captured_data = pdf_capture.capture_data()

if captured_data:
    print("Captured Data:")
    print(captured_data)
else:
    print("No selection made or capture canceled.")
