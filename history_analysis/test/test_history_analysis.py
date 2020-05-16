# test load file
# test parse

# zero message sent
# few messages sent

# count word 0
# count multiple words with different case

# no emoji sent
# few emoji sent
import unittest
from history_analysis import utils, history_analysis
from . import TEST_FILE_PATH

class TestHistoryAnalysis(unittest.TestCase):
    def setUp(self):
        logs = utils.load_file(TEST_FILE_PATH)
        self.messages = utils.parse(logs)
    
    def test_sent_messages_count(self):
        self.assertEqual(history_analysis.sent_messages_count(self.messages, "john"), 1)
        self.assertEqual(history_analysis.sent_messages_count(self.messages, "jane"), 1)
        self.assertEqual(history_analysis.sent_messages_count(self.messages, "brian"), 0)

    def test_sent_word_count(self):
        self.assertEqual(history_analysis.sent_word_count(self.messages, "john", "hello"), 1)
        self.assertEqual(history_analysis.sent_word_count(self.messages, "john", "hi"), 0)

    def test_sent_emojis_count(self):
        self.assertEqual(history_analysis.sent_emojis_count(self.messages, "john"), 0)
        self.assertEqual(history_analysis.sent_emojis_count(self.messages, "jane"), 1)

    def test_received_emojis_count(self):
        self.assertEqual(history_analysis.received_emojis_count(self.messages, "john"), 1)
        self.assertEqual(history_analysis.received_emojis_count(self.messages, "jane"), 0)