import fitz
from openpyxl import load_workbook
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
            (72,126), (271,335), (22,268), (102,321), (336,364), (460,519), (273,429), (22,266)
        ]
        y_positions = [
            (125,135), (316,329), (277,347), (23,46), (317,329), (484,501), (388,445), (219,264)
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
    drive_service = build('drive', 'v3', credentials=my_creds)
    folder_id = '1-_7jf6xZpCi4sI2ne600iOkc0IZj-q1f'
    pdf_paths = []
    page_token = None
    while True:
        response = drive_service.files().list(q=f"'{folder_id}' in parents and mimeType='application/pdf'",
                                              spaces='drive',
                                              fields='nextPageToken, files(id, name)',
                                              pageToken=page_token).execute()
        for file in response.get('files', []):
            pdf_paths.append(file['name'])
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break

    if pdf_paths:
        process_pdf(pdf_paths)
        print("Data captured and saved successfully!")
    else:
        print("No PDF files found in the folder!")


if __name__ == "__main__":
    SERVICE_ACCOUNT_FILE = 'service_account.json'
    SCOPES = ['https://www.googleapis.com/auth/drive']
    my_creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    
    
    scan_and_process_files()
