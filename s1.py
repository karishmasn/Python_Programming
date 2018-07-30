import requests
import re
from bs4 import BeautifulSoup

url='http://whatismyip.host/'
cont=requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
soup = BeautifulSoup(cont.text, 'html.parser')
l=soup.find(class_="ipaddress").text
print(l)
