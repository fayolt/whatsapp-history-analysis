import unittest
from history_analysis import utils
from . import TEST_FILE_PATH

class TestUtils(unittest.TestCase):
    def get_messages(self):
        return {
            "john": ["Hello"],
            "jane": ["Hi 😊"]
        }
    def test_load_file(self):
        logs = utils.load_file(TEST_FILE_PATH)
        self.assertAlmostEqual(len(logs), 2)

    def test_parse(self):
        logs = utils.load_file(TEST_FILE_PATH)
        self.assertDictEqual(utils.parse(logs), self.get_messages())