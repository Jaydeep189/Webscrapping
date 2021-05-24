import requests
from bs4 import BeautifulSoup
upvotes = []
url = 'https://www.reddit.com/r/memes/top/?t=all'
r = requests.get(url)
html_content = r.content
soup = BeautifulSoup(html_content, 'html.parser')
upvote = soup.find_all('', class_ ='_1rZYMD_4xY3gRcSS3p8ODO _3a2ZHWaih05DgAOtvu6cIo')
for num in upvote:
    upvotes.append(num.get('div'))
print(upvotes)