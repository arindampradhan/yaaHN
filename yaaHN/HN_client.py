import requests
from .helpers import comment_parser, story_parser, poll_parser, user_parser, request_item, request_user


class client(object):

    """client tool for hacker news """

    def __init__(self):
        self.more = ""

    def get_user(self, id):
        response = request_user(id)
        return user_parser(response)

    def get_poll(self, id):
        response = request_item(id)
        return poll_parser(response)

    def get_comment(self, id):
        response = request_item(id)
        return comment_parser(response)

    def get_story(self, id):
        response = request_item(id)
        return story_parser(response)

    def top_stories(self, id):
        TOP_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
        response = requests.get(TOP_URL).json()
        return response
