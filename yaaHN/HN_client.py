import requests
from thread_request import *
from .helpers import (comment_parser, story_parser, poll_parser,
                      user_parser, request_item, request_user,
                      item_parser, TOP_STORIES_URL, UPDATES_URL,
                      API_BASE, update_parser, MAX_URL)


class hn_client(object):

    """client tool for hacker news"""

    def __init__(self):
        self.more = ""

    @classmethod
    def get_user(self, id):
        """
        Get a user object from the given user id
        """
        response = request_user(id)
        return user_parser(response)

    @classmethod
    def get_poll(self, id):
        """
        Get a poll object from the given item id
        """
        response = request_item(id)
        return poll_parser(response)

    @classmethod
    def get_comment(self, id):
        """
        Get a comment object from the given item id
        """
        response = request_item(id)
        return comment_parser(response)

    @classmethod
    def get_story(self, id):
        """
        Get a story object from the given item id
        """
        response = request_item(id)
        return story_parser(response)

    @classmethod
    def top_stories_ids(self):
        """
        Get the top 100 story ids
        """
        response = requests.get(TOP_STORIES_URL).json()
        return response

    @classmethod
    def top_stories(self, limit=5, first=None, last=None, json=False):
        """
        Get the top story objects list

        params :
            limit = (default | 5) number of story objects needed 
            json = (default | False) 

        The method uses asynchronous grequest form gevent 
        """

        story_ids = requests.get(TOP_STORIES_URL).json()
        story_urls = []
        for story_id in story_ids:
            url = API_BASE + "item/" + str(story_id) + '.json'
            story_urls.append(url)

        if first and last:
            story_urls = story_urls[first:last]
            if limit != 5:
                story_urls[:limit]  # default not given
        else:
            story_urls = story_urls[:limit]

        # try:
        #     response_queue = fetch_parallel(story_urls)
        #     if json:
        #         while not response_queue.empty():
        #             yield response_queue.get()
        #     else:
        #         while not response_queue.empty():
        #             yield story_parser(response_queue.get())
        # except AttributeError:
        #     Exception("Too many requests worker!!")

        # using gevent
        response_list = fetch_event(story_urls)
        if json:
            yield response_list
        else:
            for response in response_list:
                yield story_parser(response)

    @classmethod
    def get_comments(self, comment_id=2921983, limit=5, json=False):
        """
        Get the top story objects list

        params :
            comment_id = the id of the story object
            limit = (default = 5) number of story objects needed
            set limit it to None to get all the comments

        The method uses asynchronous grequest form gevent 
        """
        try:
            comment_ids = requests.get(
                API_BASE + "item/" + str(comment_id) + '.json').json()['kids']
        except KeyError:
            return None

        comment_urls = []
        for comment_id in comment_ids:
            url = API_BASE + "item/" + str(comment_id) + '.json'
            comment_urls.append(url)
        comment_urls[:limit]  # default not given

        # try:
        #     response_queue = fetch_parallel(comment_urls)
        #     if json:
        #         while not response_queue.empty():
        #             yield response_queue.get()
        #     else:
        #         while not response_queue.empty():
        #             yield comment_parser(response_queue.get())
        # except AttributeError:
        #     Exception("Too many requests worker!!")

        # using gevent
        response_list = fetch_event(comment_urls)
        response_obj = [comment_parser(comment_json)
                        for comment_json in response_list]
        return response_obj

    @classmethod
    def get_item(self, id):
        """
        Get an item object from the given item id
        """
        response = request_item(id)
        return item_parser(response)

    @classmethod
    def get_max_item(self):
        """
        Returns the largest item
        """
        return requests.get(MAX_URL).json()

    @classmethod
    def updates(self):
        """
        Returns the update object
        update property :
            items - list of updated object
            profiles - list of the profiles updated
        """
        response = requests.get(UPDATES_URL).json()
        return update_parser(response)
