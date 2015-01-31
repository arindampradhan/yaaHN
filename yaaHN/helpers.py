from .models.comment import Comment
from .models.story import Story
from .models.item import Item
from .models.user import User
from .models.poll import Poll
from .models.update import Update
from thread_request import *
import requests
import urlparse

API_VERSION = 0

# urls
API_BASE = "https://hacker-news.firebaseio.com/v{}/".format(API_VERSION)
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
UPDATES_URL = "https://hacker-news.firebaseio.com/v0/updates.json?print=pretty"

# https://hacker-news.firebaseio.com/v0/user/jl.json?print=pretty


def user_parser(user):
    return User(
        user['id'],
        user['delay'],
        user['created'],
        user['karma'],
        user['about'],
        user['submitted'],
    )


# https://hacker-news.firebaseio.com/v0/item/8863.json?print=pretty
def story_parser(story):
    return Story(
        check_key('id', story),
        check_key('by', story),
        check_key('kids', story),
        check_key('score', story),
        check_key('time', story),
        check_key('title', story),
        check_key('type', story),
        check_key('url', story),
    )

# https://hacker-news.firebaseio.com/v0/item/2921983.json?print=pretty


def comment_parser(comment):
    return Comment(
        comment['id'],
        comment['by'],
        comment['kids'],
        comment['parent'],
        comment['text'],
        comment['time'],
        comment['type'],
    )

# https://hacker-news.firebaseio.com/v0/item/126809.json?print=pretty


def poll_parser(poll):
    return Poll(
        poll['id'],
        poll['by'],
        check_key('kids', poll),
        check_key('parts', poll),
        poll['score'],
        poll['text'],
        poll['time'],
        poll['title'],
        poll['type'],
    )


# https://hacker-news.firebaseio.com/v0/item/2921983.json?print=pretty
def item_parser(item):
    return Item(
        check_key('id', item),
        check_key('deleted', item),
        check_key('type', item),
        check_key('by', item),
        check_key('time', item),
        check_key('text', item),
        check_key('dead', item),
        check_key('parent', item),
        check_key('kids', item),
        check_key('url', item),
        check_key('score', item),
        check_key('title', item),
        check_key('parts', item),
    )

# https://hacker-news.firebaseio.com/v0/updates.json?print=pretty


def update_parser(update):
    return Update(
        update['items'],
        update['profiles'],
    )


def check_key(key, item):
    try:
        return item[key]
    except KeyError:
        return None


def request_item(id):
    return requests.get(API_BASE + "item/" + str(id) + '.json').json()


def request_user(id):
    return requests.get(API_BASE + 'user/' + str(id) + '.json').json()
