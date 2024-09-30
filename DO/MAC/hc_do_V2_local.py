import fitz
from openpyxl import load_workbook
from googleapiclient.discovery import build
from google.oauth2 import service_account
import os

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
            (496, 539),  # Area 1
            (43, 122),   # Area 2
            (43, 182),   # Area 3
            (112, 299),  # Area 4
            (214, 252),  # Area 5
            (418, 481),  # Area 6
            (307, 409),  # Area 7
            (449, 511),  # Area 8
            (45, 216)    # Area 9
        ]
        y_positions = [
            (64, 74),    # Area 1
            (576, 700),  # Area 2
            (370, 413),  # Area 3
            (38, 59),    # Area 4
            (575, 586),  # Area 5
            (524, 535),  # Area 6
            (434, 466),  # Area 7
            (337, 350),  # Area 8
            (302, 337)   # Area 9
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
        pdf_capture = PDFCapture(pdf_path, num_selections=9)
        captured_data = pdf_capture.capture_data()

        # Save the captured data to the Google Sheet
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


def scan_and_process_files():
    pdf_paths = []
    directory = r'/Users/champagne/Library/CloudStorage/GoogleDrive-sp.dispatchservice@gmail.com/My Drive/Company/FaCai/DO/HC'
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            pdf_paths.append(os.path.join(directory, filename))

    if pdf_paths:
        process_pdf(pdf_paths)
        print("Data captured and saved successfully!")
    else:
        print("No PDF files found in the directory!")


if __name__ == "__main__":
    scan_and_process_files()
