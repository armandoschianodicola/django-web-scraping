# import required modules
from bs4 import BeautifulSoup
import requests

# get URL
page = requests.get("https://it.wikipedia.org/wiki/Formaggi_italiani")

# scrape webpage
soup = BeautifulSoup(page.content, 'html.parser')

# display scraped data
print(soup.prettify())