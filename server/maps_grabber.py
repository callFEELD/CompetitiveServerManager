"""
This file grabs all map names from Fakkelbrigade.eu map list
"""

import requests
from bs4 import BeautifulSoup
import json

URL = "http://fakkelbrigade.eu/maps"
MAPS = []

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

rows = soup.find_all('tr')

for count, row in enumerate(rows):
    cells = row.find_all('td')

    if len(cells) > 0:
        MAPS.append((cells[1].a.text.split('.')[0].lower()))

MAPS = list(set(MAPS))
MAPS.sort()

with open("maps.json", "w") as file:
    file.write(json.dumps(MAPS))
