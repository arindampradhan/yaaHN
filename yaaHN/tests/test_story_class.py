import httpretty
import unittest
from os import path
import sys

from yaaHN.models import story
from yaaHN import hn_client
from yaaHN.helpers import story_parser, API_BASE
from test_utils import get_content, PRESET_DIR


class TestStory(unittest.TestCase):

    def setUp(self):
        httpretty.HTTPretty.enable()
        httpretty.register_uri(
            httpretty.GET, '{0}{1}'.format(API_BASE,
                                           'item/879.json'),
            body=get_content('story_879.json'), status=200, content_type='text/json')
        response = requests.get(
            'https://hacker-news.firebaseio.com/v0/item/879.json')

        self.PY2 = sys.version_info[0] == 0
        if not self.PY2:
            self.text_type = [str]
        else:
            self.text_type = [unicode, str]
        self.story = hn_client.get_story('879')

    def tearDown(self):
        httpretty.HTTPretty.disable()

    def test_story_data_type(self):
        """
        Test types of fields of a Story object
        """

        assert self.story.type == "story"
        assert type(self.story.id) == int
        assert type(self.story.score) == int
        assert type(self.story.time) == int
        assert type(self.story.type) in self.text_type
        assert type(self.story.title) in self.text_type
        assert type(self.story.by) in self.text_type

    def test_story_by(self):
        """
        Tests the submitter name
        """
        self.assertEqual(self.story.by, 'nate')


if __name__ == '__main__':
    unittest.main()
