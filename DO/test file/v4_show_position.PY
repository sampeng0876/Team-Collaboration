import fitz
import tkinter as tk
from PIL import ImageTk, Image

class PDFCapture:
    def __init__(self, pdf_path, num_selections):
        self.pdf_path = pdf_path
        self.doc = fitz.open(pdf_path)
        self.pages = len(self.doc)
        self.page_index = 0
        self.rectangles = []
        self.num_selections = num_selections
        self.selection_index = 0

        self.root = tk.Tk()
        self.canvas_width = 800
        self.canvas_height = 1000
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.start_selection)

        self.display_page(self.page_index)  # Display the first page initially

        self.root.mainloop()

    def display_page(self, page_number):
        self.page_index = page_number
        self.canvas.delete("all")
        page = self.doc.load_page(page_number)
        pix = page.get_pixmap()
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

        for rect in self.rectangles:
            self.canvas.create_rectangle(*rect, outline="red")

    def start_selection(self, event):
        if self.selection_index >= self.num_selections:
            return

        rect = [event.x, event.y, event.x, event.y]
        self.rectangles.append(rect)
        self.canvas.bind("<B1-Motion>", self.track_selection)
        self.canvas.bind("<ButtonRelease-1>", self.end_selection)

    def track_selection(self, event):
        if self.rectangles:
            rect = self.rectangles[-1]
            rect[2] = event.x
            rect[3] = event.y
            self.display_page(self.page_index)

    def end_selection(self, event):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.selection_index += 1

        if self.selection_index >= self.num_selections:
            self.root.destroy()

    def capture_data(self):
        data = []
        for i, rect in enumerate(self.rectangles):
            x0, y0, x1, y1 = rect
            x0, x1 = min(x0, x1), max(x0, x1)
            y0, y1 = min(y0, y1), max(y0, y1)
            clip_rect = fitz.Rect(x0, y0, x1, y1)
            page = self.doc.load_page(self.page_index)
            text = page.get_text("text", clip=clip_rect)
            if not text:
                text = "N/A"
            data.append(text)
            print(f"Area {i+1} - x: {x0}-{x1}, y: {y0}-{y1}")
        return data


# Usage example
pdf_file = "TAN.pdf"
num_areas = 7
pdf_capture = PDFCapture(pdf_file, num_areas)
captured_data = pdf_capture.capture_data()

for i, data in enumerate(captured_data):
    print(f"Captured Data {i+1}:")
    print(data)
    print()
