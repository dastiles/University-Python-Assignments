from bs4 import Beatifulsoup
import requests


response = requests.get('www.google.com')

soup = Beatifulsoup(response.content,'html-parser')

# getting text by id
title = soup.find('p', id_='contents').text
# getting text by class
title = soup.find('p', class_='contents').text


