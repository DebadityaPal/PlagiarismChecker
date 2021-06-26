import requests
import re
import math
from collections import Counter
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


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())

    # calculating numerator
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    # calculating denominator
    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    # checking for divide by zero
    if denominator == 0:
        return 0.0
    else:
        return float(numerator) / denominator


# converts given text into a vector
def text_to_vector(text):
    # uses the Regular expression above and gets all words
    words = WORD.findall(text)
    # returns a counter of all the words (count of number of occurences)
    return Counter(words)


# returns cosine similarity of two words
# uses: text_to_vector(text) and get_cosine(v1,v2)
def cosineSim(text, url, array, process=0):
    threshold = 0.8
    vector1 = text_to_vector(text)
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
        # x = re.compile(r"\W+", re.UNICODE).split(sentence)
        # x = [ele for ele in x if ele != ""]
        vector2 = text_to_vector(sentence)
        cosine = get_cosine(vector1, vector2)
        print(cosine)
        if cosine > threshold:
            array[process] = True
            break
    return
