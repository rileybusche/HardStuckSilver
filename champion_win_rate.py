import requests
from bs4 import BeautifulSoup

url = 'https://na.op.gg/statistics/champion/'

page = requests.get(url)

if page.status_code == 200:
    soup = BeautifulSoup(page.text, 'html.parser')
    # print(soup.prettify())
    table = soup.find_all('tbody')
    print(table)
    
