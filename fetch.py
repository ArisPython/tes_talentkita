import requests
from bs4 import BeautifulSoup

# Input Url --> string
input_url = input('Masukkan Url: ')
url = str(input_url)

# mengambil data dari URL
response = requests.get(url)

# parsing konten
soup = BeautifulSoup(response.text , 'html.parser')

# filter tag <a> dari dokumen yg telah terparser
for tag in soup.find_all('a'):
   print(tag)

