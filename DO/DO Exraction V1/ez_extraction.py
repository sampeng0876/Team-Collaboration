###### V1
# import fitz  # PyMuPDF

# def extract_text_from_pdf(pdf_path):
#     doc = fitz.open(pdf_path)
#     text = ''
#     for page_num in range(doc.page_count):
#         page = doc[page_num]
#         text += page.get_text()
#     doc.close()
#     return text

# pdf_path = r"/Users/Grace/Desktop/Manual/SP/Team-Collaboration/PDF/ez.pdf"
# extracted_text = extract_text_from_pdf(pdf_path)
# print(extracted_text)

###### V2
import fitz

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ''
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    doc.close()
    return text

def organize_and_display_data(text):
    # Your data processing and organization logic here
    organized_data = process_and_organize_text(text)

    # Print or display the organized data
    print(organized_data)

def process_and_organize_text(text):
    # Your data processing and organization logic here
    # This is a placeholder; modify according to your needs
    lines = text.split('\n')
    organized_data = {'lines': lines}

    return organized_data

pdf_path = r"/Users/Grace/Desktop/Manual/SP/Team-Collaboration/PDF/ez.pdf"
extracted_text = extract_text_from_pdf(pdf_path)
organize_and_display_data(extracted_text)


