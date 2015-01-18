# from .models.story import Story
# from .models.comment import Comment
# from .models.user import User
# from .models.poll import Poll
# import requests
# import urlparse

API_VERSION = 0
API_BASE = "https://hacker-news.firebaseio.com/v{}/".format(API_VERSION)


def story_parser(story):
    return Story(
        story['id'],
        story['by'],
        story['kids'],
        story['score'],
        story['time'],
        story['title'],
        story['type'],
        story['url'],
    )


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


def poll_parser(poll):
    return Poll(
        poll['id'],
        poll['by'],
        poll['kids'],
        poll['score'],
        poll['text'],
        poll['time'],
        poll['title'],
        poll['type'],
    )


def user_parser(user):
    return User(
        user['id'],
        user['delay'],
        user['created'],
        user['karma'],
        user['about'],
        user['submitted'],
    )

# https://hacker-news.firebaseio.com/v0/item/2921983.json?print=pretty


def request_item(id):
    return requests.get(API_BASE + "item/" + str(id) + '.json').json()


def request_user(id):
    return requests.get(API_BASE + 'user/' + str(id) + '.json').json()
