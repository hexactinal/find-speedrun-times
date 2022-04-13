# webscraping.py -- script that goes out and gets the speedrun times from speedrun.com
# Based on TechWithTim's tutorial at https://www.youtube.com/watch?v=gRLHr664tXA

from bs4 import BeautifulSoup
import requests

url = 'https://www.speedrun.com/sm64'
result = requests.get(url)
print(result.text)
#html parser does NOT work on speedrun.com unfortunately, so I will need to get the
#info using some other method.
#doc = BeautifulSoup(result, "html.parser")
#print(doc.prettify())
