import fitz
from openpyxl import load_workbook
from tkinter import Tk, Label, Button, filedialog, messagebox
from googleapiclient.discovery import build
from google.oauth2 import service_account

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
            (368, 423), (19, 102), (24, 312), (104, 371), (108, 139), (409, 463), (307, 587), (24, 314)
        ]
        y_positions = [
            (114, 125), (522, 578), (321, 381), (30, 45), (522, 579), (524, 580), (598, 675), (219, 279)
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
    
    SERVICE_ACCOUNT_FILE = 'service_account.json'
    # If modifying these scopes, delete the file token.json.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    my_creds = None
    my_creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # The ID and range of a sample spreadsheet.
    google_sheet_id = '12lnRmQoBsITIYTQPEGYdHGVNUkoPPFQEhx5HaC3JTJQ'
    sheet_name = 'RECORD_DO'
    service = build('sheets', 'v4', credentials=my_creds)
  
    for pdf_path in pdf_paths:
        # Create an instance of PDFCapture
        pdf_capture = PDFCapture(pdf_path, num_selections=8)
        captured_data = pdf_capture.capture_data()

    # Save the captured data to the Google Sheet
        values = []  
        values = [str(data).replace('\n', '').strip() for data in captured_data]
        print(values)
        body = {'values': [values]}


        # Find the next available row
        result = service.spreadsheets().values().get(spreadsheetId=google_sheet_id, range=sheet_name).execute()
        next_row = len(result['values']) + 1
        
        # Write values to the sheet
        service.spreadsheets().values().update(
            spreadsheetId=google_sheet_id,
            range=sheet_name + '!A' + str(next_row),
            valueInputOption='USER_ENTERED',
            body=body
        ).execute()


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

print('Finished')
