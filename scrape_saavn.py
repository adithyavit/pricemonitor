import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url='https://www.jiosaavn.com/'
#print(response) #response 503
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

#print(soup)
movie_containers = soup.find_all('span', class_ = 'ellip')

print(movie_containers)