import re
import googlesearch
import sys
from extractdocx import extractDocx
from similarity import substringMatching


def createQueries(text):
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
        if sentence:
            final_query.append(sentence)
    return final_query


def searchGoogle(query):
    """Uses Google Search to fetch urls relevant to the query.

    Parameters
    ----------
    query: str
        query to be searched.
    """
    response = googlesearch.search(query, tld="com", lang="en", num=1, stop=1, pause=2)
    urls = []
    for url in response:
        urls.append(url)
    return urls


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py <input-filename>.txt <output-filename>.txt")
        sys.exit()
    if sys.argv[1].endswith(".docx"):
        text = extractDocx(sys.argv[1])
    else:
        text = open(sys.argv[1], "r")
        if not text:
            print("Invalid Filename")
            print("Usage: python main.py <input-filename>.txt <output-filename>.txt")
            sys.exit()
        text = text.read()
    queries = createQueries(text)
    queries = [" ".join(word) for word in queries]
    urls = []
    for query in queries:
        url = searchGoogle(query)
        print(substringMatching(text, url[0]))
