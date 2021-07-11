import requests
import re
from bs4 import BeautifulSoup

WORD = re.compile(r"\w+")


def substringMatching(text, url, array, process=0):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0",
        "Accept-Language": "en-US",
        "Accept": "text/html",
    }
    try:
        response = requests.get(url, headers=headers)
    except:
        return
    soup = BeautifulSoup(response.text, "html.parser")
    website_text = soup.get_text()

    website_text = re.sub(r"\W+", "", website_text).lower()
    text = re.sub(r"\W+", "", text).lower()

    if text in website_text:
        array[process] = True
    else:
        array[process] = False
    return


def bagOfWordsValue(set1, set2):
    denominator = len(set1)
    numerator = len(set1.intersection(set2))
    return numerator / denominator


def bagOfWordsSim(text, url, array, process=0):
    threshold = 0.5
    words = WORD.findall(text)
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0",
        "Accept-Language": "en-US",
        "Accept": "text/html",
    }
    try:
        response = requests.get(url, headers=headers)
    except:
        return
    soup = BeautifulSoup(response.text, "html.parser")
    website_text = soup.get_text()
    website_text = re.sub("[^A-Za-z0-9!.? ]+", " ", website_text)
    sentenceEnders = re.compile("[.!?]")
    sentences = sentenceEnders.split(website_text)
    for sentence in sentences:
        sentence_words = WORD.findall(sentence)
        value = bagOfWordsValue(set(words), set(sentence_words))
        if value > threshold:
            array[process] = True
            break
    return
