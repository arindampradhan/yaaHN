import httpretty
import unittest
from os import path
import sys

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
            body=get_content('user_879.json'), status=200, content_type='text/json')
        response = requests.get(
            'https://hacker-news.firebaseio.com/v0/user/joe.json')

        self.PY2 = sys.version_info[0] == 0
        if not self.PY2:
            self.text_type = [str]
        else:
            self.text_type = [unicode, str]
        self.user = hn_client.get_user('joe')

    def tearDown(self):
        httpretty.HTTPretty.disable()

    def test_user_data_type(self):
        """
        Test types of fields of a User object
        """

        assert type(self.user.id) in self.text_type
        assert type(self.user.created) == int
        assert type(self.user.karma) == int
        assert type(self.user.submitted) == list
        assert type(self.user.about) in self.text_type
        assert type(self.user.delay) == int

    def test_user_by(self):
        """
        Tests the submitter name
        """
        self.assertEqual(self.user.by, 'nate')


if __name__ == '__main__':
    unittest.main()
