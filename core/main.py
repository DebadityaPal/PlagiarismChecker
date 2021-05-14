import requests
import re
import googlesearch
from bs4 import BeautifulSoup


def createQueries(text, n_grams):
    """Processes the input text and generates queries that will be Googled.

    Parameters
    ----------
    text: str
        The input text that is  to be processed.
    n_grams: int
        The maximum number of words each query can have.
    """
    sentenceEnders = re.compile("[.!?]")
    sentences = sentenceEnders.split(text)
    tokenized_sentences = []
    for sentence in sentences:
        x = re.compile(r"\W+", re.UNICODE).split(sentence)
        x = [ele for ele in x if ele != ""]
        tokenized_sentences.append(x)
    final_query = []
    for sentence in tokenized_sentences:
        length = len(sentence)
        if length <= n_grams:
            final_query.append(sentence)
        else:
            length = length // n_grams
            index = 0
            for i in range(length):
                final_query.append(sentence[index : index + n_grams])
                index = index + n_grams - 1
            if index != len(sentence):
                final_query.append(sentence[index:])
    return final_query


def searchGoogle(query):
    """Uses Google Search to fetch urls relevant to the query.

    Parameters
    ----------
    query: str
        query to be searched.
    """
    response = googlesearch.search(
        query, tld="com", lang="en", num="3", stop="3", pause=2
    )
    urls = []
    for url in response:
        urls.append(url)
    return url
