from .models.comment import Comment
from .models.story import Story
from .models.item import Item
from .models.user import User
from .models.poll import Poll
from .models.update import Update
from .models.deleted import Delete
from thread_request import *
import requests
import urlparse

API_VERSION = 0

# urls
API_BASE = "https://hacker-news.firebaseio.com/v{}/".format(API_VERSION)
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
UPDATES_URL = "https://hacker-news.firebaseio.com/v0/updates.json?print=pretty"
MAX_URL = "https://hacker-news.firebaseio.com/v0/maxitem.json"
# https://hacker-news.firebaseio.com/v0/user/jl.json?print=pretty

item_types = ['poll', 'comment', 'story', 'comment', 'pollopt']
poll_types = ['poll', 'pollopt']


def user_parser(user):
    """
    Parses a user object
    """
    if __is_deleted(user):
        return deleted_parser(user)

    if user['id'] in item_types:
        raise Exception('Not a user name')
    if type(user['id']) == int:
        raise Exception('Not a user name')

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
    """
    Parses a story object
    """
    if __is_deleted(story):
        return deleted_parser(story)
    if story['type'] != 'story':
        return item_parser(story)
    return Story(
        __check_key('id', story),
        __check_key('by', story),
        __check_key('kids', story),
        __check_key('score', story),
        __check_key('time', story),
        __check_key('title', story),
        __check_key('type', story),
        __check_key('url', story),
    )

# https://hacker-news.firebaseio.com/v0/item/2921983.json?print=pretty


def comment_parser(comment):
    """
    Parses a comment object
    """
    try:
        if comment['type'] != 'comment':
            return item_parser(comment)
    except KeyError:
        return deleted_parser(comment)
    return Comment(
        comment['id'],
        comment['by'],
        __check_key('kids', comment),  # some comments do not have kids key
        comment['parent'],
        comment['text'],
        comment['time'],
        comment['type'],
    )

# https://hacker-news.firebaseio.com/v0/item/126809.json?print=pretty


def poll_parser(poll):
    """
    Parses a poll object
    """
    if __is_deleted(poll):
        return deleted_parser(poll)
    if poll['type'] not in poll_types:
        raise Exception('Not a poll type')
    return Poll(
        poll['id'],
        poll['by'],
        __check_key('kids', poll),  # poll and pollopt differ this property
        __check_key('parts', poll),  # poll and pollopt differ this property
        poll['score'],
        poll['text'],
        poll['time'],
        poll['title'],
        poll['type'],
    )


# https://hacker-news.firebaseio.com/v0/item/2921983.json?print=pretty
def item_parser(item):
    """
    Parses a item object
    It gives None for the property not present
    Used when some item types do not get parsed easily when using gevent
    """
    if __is_deleted(item):
        return deleted_parser(item)
    return Item(
        __check_key('id', item),
        __check_key('deleted', item),
        __check_key('type', item),
        __check_key('by', item),
        __check_key('time', item),
        __check_key('text', item),
        __check_key('dead', item),
        __check_key('parent', item),
        __check_key('kids', item),
        __check_key('url', item),
        __check_key('score', item),
        __check_key('title', item),
        __check_key('parts', item),
    )

# https://hacker-news.firebaseio.com/v0/item/2924562.json?print=pretty


def deleted_parser(item):
    """
    Parses the update object
    """
    return Delete(
        item['id'],
        item['deleted'],
    )


# https://hacker-news.firebaseio.com/v0/updates.json?print=pretty
def update_parser(update):
    """
    Parses the update object
    """
    return Update(
        update['items'],
        update['profiles'],
    )


def __check_key(key, item):
    """
    Checks if the key is present in the json response
    If not present returns None else initialize the object property
    """
    try:
        return item[key]
    except KeyError:
        return None


def request_item(id):
    """
    Get request on the id url
    """
    return requests.get(API_BASE + "item/" + str(id) + '.json').json()


def request_user(id):
    """
    Get request on the user url
    """
    return requests.get(API_BASE + 'user/' + str(id) + '.json').json()


def __is_deleted(item):
    """
    Checks if the object is deleted 
    If yes parses to Item object
    """
    try:
        if item['deleted'] == "true":
            print "yes yes "
            return True
    except KeyError:
        return False
