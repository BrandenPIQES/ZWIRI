import requests
from bs4 import BeautifulSoup

class WebScrap:
    def __init__(self):
        self.url = None
        self.response = None
        self.soup = None

    def readWebInfo(self, url):
        requests.get(url)
        soup = BeautifulSoup(self.response.text, 'html.parser')

        # Extract text from all paragraphs on the web page
        paragraphs = soup.find_all('p')

        # Print the extracted text
        for paragraph in paragraphs:
            print(paragraph.get_text())
    
scrap = WebScrap()
scrap.readWebInfo()