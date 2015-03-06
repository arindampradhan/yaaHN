import httpretty
import unittest
from os import path
import sys
import requests
import types
from yaaHN.models import user
from yaaHN import hn_client
from yaaHN.helpers import user_parser, API_BASE
from test_utils import get_content, PRESET_DIR


class TestUser(unittest.TestCase):

    def setUp(self):
        httpretty.HTTPretty.enable()
        httpretty.register_uri(
            httpretty.GET, '{0}{1}'.format(API_BASE,
                                           'user/joe.json'),
            body=get_content('user_joe.json'), status=200, content_type='text/json')
        response = requests.get(
            'https://hacker-news.firebaseio.com/v0/user/joe.json')

        self.user = hn_client.get_user('joe')

    def tearDown(self):
        httpretty.HTTPretty.disable()

    def test_user_data_type(self):
        """
        Test types of fields of a User object
        """

        assert type(self.user.id) == types.UnicodeType
        assert type(self.user.created) == int
        assert type(self.user.karma) == int
        assert type(self.user.submitted) == list
        assert type(self.user.about) == types.UnicodeType
        assert type(self.user.delay) == int

    def test_user_by(self):
        """
        Tests the submitter name
        """
        self.assertEqual(self.user.id, 'joe')


if __name__ == '__main__':
    unittest.main()
