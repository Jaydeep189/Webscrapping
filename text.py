import requests
from bs4 import BeautifulSoup
url = 'http://watchwrestling.mobi/watch-wwe-smackdown-live-4-2-21-2-april-2021/'
r = requests.get(url)
html_content = r.content
soup = BeautifulSoup(html_content, 'html.parser')
title = soup.find('h1', class_= 'entry-title').get_text()
print(title)
img = soup.find('src', id = 'details')
print(img)
video_links = soup.find_all('a', class_='small cool-blue vision-button')
paras = soup.find_all('p', class_='entry-content rich-content')
