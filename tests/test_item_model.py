import httpretty
import unittest
from os import path
import sys

from yaaHN.models import item
from yaaHN import hn_client
from yaaHN.helpers import item_parser, API_BASE
from test_utils import get_content, PRESET_DIR


class TestItem(unittest.TestCase):

    def setUp(self):
        httpretty.HTTPretty.enable()
        httpretty.register_uri(
            httpretty.GET, '{0}{1}'.format(API_BASE,
                                           'item/8863.json'),
            body=get_content('item_8863.json'), status=200, content_type='text/json')
        response = requests.get(
            'https://hacker-news.firebaseio.com/v0/item/8863.json')

        self.PY2 = sys.version_info[0] == 0
        if not self.PY2:
            self.text_type = [str]
        else:
            self.text_type = [unicode, str]
        self.item_type = ['pollopt', 'poll', 'comment', 'story', 'job']
        self.item = hn_client.get_item('8863')

    def tearDown(self):
        httpretty.HTTPretty.disable()

    def test_item_data_type(self):
        """
        Test types of fields of a Item object
        """
        assert type(self.id) == int
        assert type(self.deleted) == bool or None
        assert self.type in self.item_type
        assert type(self.by) == text_type
        assert type(self.time) == int or None
        assert type(self.text) in text_type or None
        assert type(self.dead) == bool or None
        assert type(self.parent) == int or None
        assert type(self.kids) == int or None
        assert type(self.url) in text_type or None
        assert type(self.score) in text_type or None
        assert type(self.title) in text_type or None
        assert type(self.parts) == list or None

    def test_item_by(self):
        """
        Tests the submitter name
        """
        self.assertEqual(self.item.by, 'dhouston')


if __name__ == '__main__':
    unittest.main()
