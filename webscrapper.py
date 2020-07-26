import pandas as pd
import requests as rq
from bs4 import BeautifulSoup
import csv

url = rq.get('https://www.azlyrics.com/a.html')
url_text  = url.text
htmlparse = BeautifulSoup(url_text, "html.parser")
tags = htmlparse.findAll('a')

content = []
for a in tags:
    content.append(a.getText().split('\n')[0])
print(content)

with open('index.csv', 'w', encoding='utf-8') as artists:
    for i in content:
        artists.write("".join(i)+"\n")

# fix csv indent 
print (tags)