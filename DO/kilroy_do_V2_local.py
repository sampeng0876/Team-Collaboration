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
            (336, 438), (121, 182), (66, 380), (354, 400), (202, 223), (486, 543), (530, 571), (230, 384)
        ]
        y_positions = [
            (183, 193), (429, 546), (345, 392), (640, 652), (428, 499), (418, 429), (820, 828), (272, 281)
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
    directory = r'K:\My Drive\Company\FaCai\DO\KILROY'
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
