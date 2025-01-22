# from googlesearch import search
# Query = input("Ask anything: ")
# for url in search(Query):
#     print(url)
from googlesearch import search
from bs4 import BeautifulSoup
import requests

def get_search_results(query):
    results = []
    for url in search(query, num=10, stop=10):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else 'No title'
            description = soup.find('meta', attrs={'name': 'description'})
            description = description['content'] if description else 'No description'
            results.append({'url': url, 'title': title, 'description': description})
        except Exception as e:
            results.append({'url': url, 'title': 'Error fetching title', 'description': str(e)})
    return results

query = input("Ask anything: ")
search_results = get_search_results(query)

for result in search_results:
    print(f"Title: {result['title']}")
    print(f"Description: {result['description']}")
    print(f"URL: {result['url']}\n")