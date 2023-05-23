import requests
from bs4 import BeautifulSoup

# Send a GET request to the login page
login_url = 'https://www.lbct.com/Login/Login'
login_payload = {
    'username': 'p1logistics@mail.com',
    'password': '8802616'
}
session = requests.Session()
session.post(login_url, data=login_payload)

# Send a GET request to the desired page after logging in
data_url = 'https://www.lbct.com/ViewMyList'
response = session.get(data_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the elements with the specified class and extract the data
data_elements = soup.find_all(class_='k-grid k-widget k-display-block')
for element in data_elements:
    print(element.text)
