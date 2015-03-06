import httpretty
import unittest
from os import path
import types
import sys
import requests
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

        self.item_type = ['pollopt', 'poll', 'comment', 'story', 'job']
        self.item = hn_client.get_item('8863')

    def tearDown(self):
        httpretty.HTTPretty.disable()

    def test_item_data_type(self):
        """
        Test types of fields of a Item object
        """
        assert type(self.item.id) == int
        assert type(self.item.deleted) == types.NoneType
        assert self.item.type in self.item_type
        assert type(self.item.by) == types.UnicodeType
        assert type(self.item.time) == int
        assert type(self.item.text) == types.NoneType
        assert type(self.item.dead) == types.NoneType
        assert type(self.item.parent) == types.NoneType
        assert type(self.item.kids) == types.ListType
        assert type(self.item.url) == types.UnicodeType
        assert type(self.item.score) == types.IntType
        assert type(self.item.title) == types.UnicodeType
        assert type(self.item.parts) == types.NoneType

    def test_item_by(self):
        """
        Tests the submitter name
        """
        self.assertEqual(self.item.by, 'dhouston')


if __name__ == '__main__':
    unittest.main()
