import requests
from thread_request import *
from .helpers import (comment_parser, story_parser, poll_parser,
                      user_parser, request_item, request_user,
                      item_parser, TOP_STORIES_URL, UPDATES_URL, API_BASE, update_parser)


class hn_client(object):

    """client tool for hacker news"""

    def __init__(self):
        self.more = ""

    @classmethod
    def get_user(self, id):
        response = request_user(id)
        return user_parser(response)

    @classmethod
    def get_poll(self, id):
        response = request_item(id)
        return poll_parser(response)

    @classmethod
    def get_comment(self, id):
        response = request_item(id)
        return comment_parser(response)

    @classmethod
    def get_story(self, id):
        response = request_item(id)
        return story_parser(response)

    @classmethod
    def top_stories_ids(self):
        response = requests.get(TOP_STORIES_URL).json()
        return response

    @classmethod
    def top_stories(self, limit=5, json=False):
        ids = requests.get(TOP_STORIES_URL).json()
        # count = 0
        # for id in response:
        #     count = count + 1
        #     if count > limit:
        #         break
        #     story = self.get_story(id)
        #     story_objs.append(story)
        #     yield story
        story_urls = []
        for id in ids:
            url = API_BASE + "item/" + str(id) + '.json'
            story_urls.append(url)

        story_urls = story_urls[:limit]

        response_queue = fetch_parallel(story_urls)
        list_response = []

        while not response_queue.empty():
            yield story_parser(response_queue.get())
        #     list_response.append(a)
        # yield list_response

    @classmethod
    def get_comments(self, story_id, limit=5):
        response = request_item(story_id)
        comments = response['kids']
        comments = comments[:limit]
        comments_url = []
        for id in ids:
            url = API_BASE + "item/" + str(id) + '.json'
            comments_url.append(url)

        response_queue = fetch_parallel(comments_url)
        list_response = []

        while not response_queue.empty():
            yield comment_parser(response_queue.get())
        #     list_response.append(a)
        # yield list_response

    @classmethod
    def get_item(self, id):
        response = request_item(id)
        return item_parser(response)

    @classmethod
    def get_max_item(self):
        id = item_parser(response)
        response = request_item(id)
        return item_parser(response)

    @classmethod
    def updates(self):
        response = requests.get(UPDATES_URL).json()
        return update_parser(response)
