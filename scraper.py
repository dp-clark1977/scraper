import requests
from bs4 import BeautifulSoup

URL = "https://thedirect.com/MCU/"
headers = {
7    &#39;User-Agent&#39;: &#39;Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36&#39;,
8}

page = requests.get(URL)

# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="news-ticker")

print(results)
