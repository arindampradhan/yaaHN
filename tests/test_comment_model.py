import httpretty
import unittest
from os import path
import sys

from yaaHN.models import comment
from yaaHN import hn_client
from yaaHN.helpers import comment_parser, API_BASE
from test_utils import get_content, PRESET_DIR


class TestComment(unittest.TestCase):

    def setUp(self):
        httpretty.HTTPretty.enable()
        httpretty.register_uri(
            httpretty.GET, '{0}{1}'.format(API_BASE,
                                           'item/2921983.json'),
            body=get_content('story_2921983.json'), status=200, content_type='text/json')
        response = requests.get(
            'https://hacker-news.firebaseio.com/v0/item/2921983.json')

        self.PY2 = sys.version_info[0] == 0
        if not self.PY2:
            self.text_type = [str]
        else:
            self.text_type = [unicode, str]
        self.comment = hn_client.get_story('2921983')

    def tearDown(self):
        httpretty.HTTPretty.disable()

    def test_story_data_type(self):
        """
        Test types of fields of a Comment object
        """

        assert self.comment.type == "comment"
        assert type(self.comment.id) == int
        assert type(self.comment.parent) == int
        assert type(self.comment.kids) == list
        assert type(self.comment.time) == int
        assert type(self.comment.type) in self.text_type
        assert type(self.comment.text) in self.text_type
        assert type(self.comment.by) in self.text_type

    def test_story_by(self):
        """
        Tests the submitter name
        """
        self.assertEqual(self.comment.by, 'norvig')


if __name__ == '__main__':
    unittest.main()
