#!/usr/bin/env python
# código obtenido de https://stackoverflow.com/questions/15517483/how-to-extract-urls-from-an-html-page-in-python
import requests
from bs4 import BeautifulSoup

def getURL(page):
    soup = BeautifulSoup(page, features="html.parser")
    links = soup.find_all('a')
    sources = soup.find_all('source')
    results = []
    for tag in links:
        results.append(tag.get('href'))
    for tag in sources:
        results.append(tag.get('src'))

    return results