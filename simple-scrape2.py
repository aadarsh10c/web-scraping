from bs4 import BeautifulSoup
import requests

#headers={ 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66'}

headers={ 'user-agent': 'Edg/87.0.664.66'}

data = requests.get("https://theprint.in", headers=headers)
print(data.status_code)
"""
with open('lexfrdman.html','w') as f:
    soup= BeautifulSoup(data.text , 'lxml')
    
    Extract intro about lexfridman
    
    intro = soup.find('div', class_="intro")
    name = intro.div.p
    print(name)
"""