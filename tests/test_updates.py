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
        result = self.update.items
        self.assertEqual(len(result), value)

    def test_profile_len(self):
        value = 10
        result = self.update.profiles
        self.assertEqual(len(result), value)

    def test_profile_name(self):
        """
        Tests one profile name
        """
        result = self.update.profiles[0]
        self.assertEqual(result, 'enqk')

    def test_item_id(self):
        """
        Tests one id in the list
        """
        result = self.update.items[0]
        self.assertEqual(result, 8975429)

if __name__ == '__main__':
    unittest.main()
