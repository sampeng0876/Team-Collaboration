from google.oauth2 import service_account
from googleapiclient.discovery import build

# Set up credentials
SERVICE_ACCOUNT_FILE = 'service_account.json'
SCOPES = ['https://www.googleapis.com/auth/drive']
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Build the drive service
drive_service = build('drive', 'v3', credentials=credentials)

# Define folder ID
folder_id = '1-_7jf6xZpCi4sI2ne600iOkc0IZj-q1f'

# Retrieve folder name
folder = drive_service.files().get(fileId=folder_id, fields='name').execute()
folder_name = folder.get('name', 'Unknown Folder')

# Define MIME type for PDF files
mime_type = 'application/pdf'

# Retrieve all PDF files in the specified folder
results = drive_service.files().list(
    q=f"'{folder_id}' in parents and mimeType='{mime_type}'",
    fields='nextPageToken, files(id, name)').execute()

files = results.get('files', [])
pdf_count = len(files)

# Print folder name and count
print(f"Folder Name: {folder_name}")
print(f"Number of PDF files in the folder: {pdf_count}")

# Print names of PDF files
print("PDF files:")
for file in files:
    print(file['name'])
