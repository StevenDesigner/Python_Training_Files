import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = 'http://example.com'

# Send a GET request to the webpage
response = requests.get(url)

# Parse the content of the request with Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the title tag and get its text
title = soup.find('title').get_text()

# Print the title
print('Title of the webpage:', title)
