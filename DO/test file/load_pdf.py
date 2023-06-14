import pdfplumber
import pandas as pd
import re

# Open the PDF file
with pdfplumber.open('sample.pdf') as pdf:
    # Iterate over each page
    for page in pdf.pages:
        # Extract the text from the page
        text = page.extract_text()
        
        # Print the extracted text
        print(text)

# Define the regular expressions to capture the date and code
date_pattern = r'(\d{2}-\d{2}-\d{4})'
file_num_pattern = r'([A-Z]{2}-\d+)'
mbl_pattern = r'([A-Z0-9]{16})'
hbl_pattern = r'([A-Z0-9]{16})'
vessel_pattern = r'^([A-Z\s]+[A-Z])$'
# Find matches for the date and code patterns
date = re.findall(date_pattern, text)
ile_num = re.findall(file_num_pattern, text)
mbl_no = re.findall(mbl_pattern, text)
hbl_no = re.findall(mbl_pattern, text)
vessel = re.match(vessel_pattern, text)


# Print the captured date and code

print("Date:", date[0])

print("Code:", ile_num[0])

print("MB/L NO.:", mbl_no[0])

print("HB/L NO.:", hbl_no[1])

print("VESSEL:", vessel)




# i = 0
# for line in pickup_address:
#     print(f'Data {i} {line}')
#     i+=1