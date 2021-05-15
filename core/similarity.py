import requests
import re
from bs4 import BeautifulSoup


def substringMatching(text, url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0",
        "Accept-Language": "en-US",
        "Accept": "text/html",
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    website_text = soup.get_text()

    website_text = re.sub(r"\W+", "", website_text).lower()
    text = re.sub(r"\W+", "", text).lower()

    if text in website_text:
        return True
    else:
        return False
