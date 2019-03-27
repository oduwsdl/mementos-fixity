#!/usr/bin/python

import sys
import requests
from bs4 import BeautifulSoup


try: from urlparse import urljoin # Python2
except ImportError: from urllib.parse import urljoin # Python3
 
url = sys.argv[1]
 
# Request the HTML code
response = requests.get(url)
 
html_data = response.text
 
soup = BeautifulSoup(html_data, "html5lib")
 
tags = soup.find_all('a')

uris = []
 
# Extracting URLs from "href" in <a> tags.
for tag in tags:
    u = tag.get('href')
    if u not in uris:
        uris.append(u)
for v in uris:
    print urljoin(sys.argv[2], v)

