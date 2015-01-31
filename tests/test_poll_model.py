import httpretty
import unittest
import requests
import sys

from os import path
from yaaHN.models import poll
from yaaHN import hn_client
from yaaHN.helpers import poll_parser, API_BASE
from test_utils import get_content, PRESET_DIR


class TestPoll(unittest.TestCase):

    def setUp(self):
        httpretty.HTTPretty.enable()
        httpretty.register_uri(
            httpretty.GET, '{0}{1}'.format(API_BASE, 'item/126809.json'),
            body=get_content('poll_126809.json'), status=200,
            content_type='text/json')

        response = requests.get(
            'https://hacker-news.firebaseio.com/v0/item/126809.json')

        self.PY2 = sys.version_info[0] == 2
        if not self.PY2:
            self.text_type = [str]
        else:
            self.text_type = [unicode, str]
        self.pool_type = ['poll', 'pollopt']
        self.poll = hn_client.get_poll('126809')

    def tearDown(self):
        httpretty.HTTPretty.disable()

    def test_poll_data_type(self):
        """
        Test types of fields of a Poll object
        """

        assert type(self.poll.id) == int
        assert type(self.poll.score) == int
        assert type(self.poll.time) == int
        assert type(self.poll.kids) == list
        assert type(self.poll.parts) == list
        assert type(self.poll.type) in self.pool_type
        assert type(self.poll.title) in self.text_type
        assert type(self.poll.by) in self.text_type
        assert type(self.poll.text) in self.text_type

    def test_poll_by(self):
        """
        Tests the submitter name
        """
        self.assertEqual(self.poll.by, 'pg')


if __name__ == '__main__':
    unittest.main()
