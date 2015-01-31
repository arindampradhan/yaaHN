import httpretty
import unittest
from os import path
import sys

from yaaHN.models import update
from yaaHN import hn_client
from yaaHN.helpers import update_parser, API_BASE
from test_utils import get_content, PRESET_DIR


class TestUpdate(unittest.TestCase):

    def setUp(self):
        httpretty.HTTPretty.enable()
        httpretty.register_uri(
            httpretty.GET, '{0}{1}'.format(API_BASE,
                                           'updates.json'),
            body=get_content('updates.json'), status=200, content_type='text/json')

        self.update = hn_client.updates()

    def tearDown(self):
        httpretty.HTTPretty.disable()

    def test_item_len(self):
        value = 10
        result = update.items
        self.assertEqual(len(result), value)

    def test_item_len(self):
        value = 10
        result = update.profiles
        self.assertEqual(len(result), value)

if __name__ == '__main__':
    unittest.main()
