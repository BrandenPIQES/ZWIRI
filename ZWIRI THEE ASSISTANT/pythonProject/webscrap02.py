import pywhatkit as pw
from bs4 import BeautifulSoup
import requests

def search_on_google(query):
    search_results = pw.search(query)
    if search_results:
        first_result = search_results[0]
        page = requests.get(first_result)
        soup = BeautifulSoup(page.content, 'html.parser')
        links = soup.find_all('a')
        urls = [link.get('href') for link in links]
        return urls
    else:
        return []

query = "OpenAI"
urls = search_on_google(query)
for url in urls:
    print(url)
    
'''
from googlesearch import search
from bs4 import BeautifulSoup
import requests

def search_on_google(query):
    search_results = search(query, num_results=5)  # Perform a Google search and get the top 5 results
    urls = []
    for result in search_results:
        urls.append(result)
    return urls



urls = search_on_google("Who is the richest man in the world")
for url in urls:
    print(url)
'''