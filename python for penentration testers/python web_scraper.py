#python web_scraper.py
#Author: P(codename- STRANGE)
#date: 11/09/2020
"""purpose: Python-based web scraping tool that includes the ability to use proxy servers,
change user-agent string, and identify cookies form target server."""

import requests

proxies = {"http": "139.99.105.5:80"} #Using a free proxy
# device presented to the victim
headers = {"user-agent": "Mozilla/5.0(X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0"}
# Set the target link here
r = requests.get("https://webscraper.io/test-sites/e-commerce/allinone", proxies=proxies, headers=headers)
print(r.text)
# Searching for cookies and print if any.

for cookie in r.cookies:
    print(cookie)
print (r.cookies["TestingGround"])
