from bs4 import BeautifulSoup

file_path = 'index.html'

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')

title = soup.find('h1').get_text()

print('Title of the webpage:', title)

paragraphs = soup.find_all('p')
for i, paragraph in enumerate(paragraphs, start=1):
    print(f'Paragraph {i}:', paragraph.get_text())
