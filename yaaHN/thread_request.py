# from .helpers import story_parser
import threading
import requests
import Queue
import sys

# urls = [
#     'http://hacker-news.firebaseio.com/v0/item/8964451.json',
#     'http://hacker-news.firebaseio.com/v0/item/8961438.json',
#     'http://hacker-news.firebaseio.com/v0/item/8967339.json',
#     'http://hacker-news.firebaseio.com/v0/item/8971058.json',
# ]


global ohno


def read_url(url, queue):
    data = requests.get(url).json()
    queue.put(data)


def fetch_parallel(urls):
    """
    Returns a queue object of the output
    """
    result = Queue.Queue()
    threads = [
        threading.Thread(target=read_url, args=(url, result)) for url in urls]
    for t in threads:
        t.start()
        # t.daemon = True
    for t in threads:
        t.join()
    return result


def fetch_sequencial():
    result = Queue.Queue()
    for url in urls:
        read_url(url, result)
    return result

# a = fetch_parallel(urls)
