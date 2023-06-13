import fitz
from openpyxl import load_workbook
from tkinter import Tk, Label, Button, filedialog, messagebox
import gspread
from google.oauth2.service_account import Credentials

class PDFCapture:
    def __init__(self, pdf_path, num_selections):
        self.pdf_path = pdf_path
        self.doc = fitz.open(pdf_path)
        self.pages = len(self.doc)
        self.page_index = 0
        self.num_selections = num_selections

    def capture_data(self):
        data = []
        x_positions = [
            (29,66), (28,108), (29,292), (235,330), (110,148), (318,367)
        ]
        y_positions = [
            (23,42), (402,420), (267,283), (24,43), (403,419), (403,416)
        ]

        for i in range(self.num_selections):
            x0, x1 = x_positions[i]
            y0, y1 = y_positions[i]
            clip_rect = fitz.Rect(x0, y0, x1, y1)
            page = self.doc.load_page(self.page_index)
            text = page.get_text("text", clip=clip_rect)
            if not text:
                text = "N/A"
            data.append(text)

        return data


def process_pdf(pdf_paths):
    # Load the credentials from the JSON key file
    scopes = ['https://www.googleapis.com/auth/spreadsheets']
    credentials = Credentials.from_service_account_file('service_account.json', scopes=scopes)
    
    # Authorize the credentials and create a client for accessing Google Sheets API
    client = gspread.authorize(credentials)
    
    # Open the Google Sheets file
    spreadsheet = client.open('do_data')
    sheet = spreadsheet.worksheet('SMART')
    
    # Find the next available row
    next_row = len(sheet.get_all_values()) + 1
    
    for pdf_path in pdf_paths:
        # Create an instance of PDFCapture
        pdf_capture = PDFCapture(pdf_path, num_selections=28)
        captured_data = pdf_capture.capture_data()

        # Save the captured data to the next available row
        row_data = [data if data else "N/A" for data in captured_data]
        sheet.insert_row(row_data, next_row)

        next_row += 1


def on_file_select():
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    if file_paths:
        process_pdf(file_paths)
        messagebox.showinfo("Success", "Data captured and saved successfully!")
        root.destroy()


root = Tk()
root.title("DO Extraction")
# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the x and y coordinates for the window to be centered
x = (screen_width - 300) // 2
y = (screen_height - 200) // 2

# Set the position of the window
root.geometry(f"300x200+{x}+{y}")

label = Label(root, text="Select PDF Files")
label.pack(pady=50)

# Function to handle file selection
def select_file():
    on_file_select()

# Create a button for file selection
select_button = Button(root, text="Select Files", command=select_file)
select_button.pack()

root.mainloop()
