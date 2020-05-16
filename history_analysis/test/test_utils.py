import unittest
from history_analysis import utils
from . import TEST_FILE_WITH_SYSTEM_MESSAGES_ONLY, TEST_FILE_WITH_SINGLELINE_MESSAGES_ONLY, TEST_FILE_WITH_MULTILINE_MESSAGES

class TestUtils(unittest.TestCase):
    def get_singleline_messages(self):
        return {
            "john": ["Hello"],
            "jane": ["Hi"]
        }
    def get_multiline_messages(self):
        return {
            "john": ["Hello! Do you still hate me?", "fuck!", "😡😡", "lol! You really got me there. Thanks!"],
            "jane": ["Yes!\nIf you are in a room with Hitler and I was given two bullets,\nI'd shoot you twice!!", "😂😂😂Gotcha!\nI'm kidding. We are good!"]
        }
    def test_load_file(self):
        logs = utils.load_file(TEST_FILE_WITH_SINGLELINE_MESSAGES_ONLY)
        self.assertAlmostEqual(len(logs), 2)

    def test_parse(self):
        logs = utils.load_file(TEST_FILE_WITH_SINGLELINE_MESSAGES_ONLY)
        self.assertAlmostEqual(len(logs), 2)
        self.assertDictEqual(utils.parse(logs), self.get_singleline_messages())
        logs = utils.load_file(TEST_FILE_WITH_SYSTEM_MESSAGES_ONLY)
        self.assertAlmostEqual(len(logs), 2)
        self.assertDictEqual(utils.parse(logs), {})
        logs = utils.load_file(TEST_FILE_WITH_MULTILINE_MESSAGES)
        self.assertAlmostEqual(len(logs), 10)
        self.assertDictEqual(utils.parse(logs), self.get_multiline_messages())