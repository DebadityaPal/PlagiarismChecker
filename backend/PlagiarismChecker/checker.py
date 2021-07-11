import re
import googlesearch
import threading
import time
from PlagiarismChecker.similarity import bagOfWordsSim, substringMatching


def createQueries(text, n_grams=False):
    """Processes the input text and generates queries that will be Googled.

    Parameters
    ----------
    text: str
        The input text that is  to be processed.
    n_grams: int
        The maximum number of words each query can have.
    """
    if n_grams:
        n = 9
        words = text.split(" ")
        tokenized_sentences = []
        for idx in range(len(words) // n):
            tokenized_sentences.append(words[idx * n : (idx + 1) * n])
        tokenized_sentences.append(words[(len(words) // n) * n :])
    else:
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


def searchGoogle(query, num_results=3):
    """Uses Google Search to fetch urls relevant to the query.

    Parameters
    ----------
    query: str
        query to be searched.
    """
    response = googlesearch.search(
        query, tld="com", lang="en", num=num_results, stop=num_results, pause=0
    )
    urls = []
    for url in response:
        urls.append(url)
    return urls


def PlagCheck(text, n_grams=False):
    search_width = 2
    queries = createQueries(text, n_grams)
    queries = [" ".join(word) for word in queries]
    result = []
    for query in queries:
        start = time.time()
        urls = searchGoogle(query, search_width)
        match = [False] * len(urls)
        jobs = []

        for i in range(len(urls)):
            if not n_grams:
                thr = threading.Thread(
                    target=substringMatching, args=(query, urls[i], match, i)
                )
            else:
                thr = threading.Thread(
                    target=bagOfWordsSim, args=(query, urls[i], match, i)
                )
            jobs.append(thr)
            thr.start()

        for thr in jobs:
            thr.join()

        temp_dict = None
        for idx in range(len(urls)):
            if match[idx]:
                temp_dict = {"sentence": query, "match": urls[idx]}

                break
        if temp_dict:
            result.append(temp_dict)

        end = time.time()
        duration = end - start
        if duration < 2:
            time.sleep(2.1 - duration)

    final_result = []

    for i in range(len(result)):
        if i == 0:
            final_result.append(result[i])
        elif result[i]["match"] == result[i - 1]["match"]:
            final_result[-1]["sentence"] = (
                final_result[-1]["sentence"] + result[i]["sentence"]
            )
        else:
            final_result.append(result[i])

    return final_result
