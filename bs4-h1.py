from bs4 import BeautifulSoup

# Path to the local HTML file
file_path = 'index.html'

# Open and read the file
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Parse the content with Beautiful Soup
soup = BeautifulSoup(content, 'html.parser')

# Find all h1 tags
h1_tags = soup.find_all('h1')

# Extract the text from each h1 tag
h1_contents = [tag.get_text() for tag in h1_tags]

# Path to the output text file
output_file_path = 'h1_contents.txt'

# Write the h1 contents to the text file
with open(output_file_path, 'w') as output_file:
    for content in h1_contents:
        output_file.write(content + '\n')

print(f'Extracted {len(h1_contents)} h1 tags and saved them to {output_file_path}')
