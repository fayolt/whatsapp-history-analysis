import unittest
from history_analysis import utils, history_analysis
from . import TEST_FILE_WITH_MULTILINE_MESSAGES, PROFANITIES

class TestHistoryAnalysis(unittest.TestCase):
    def setUp(self):
        logs = utils.load_file(TEST_FILE_WITH_MULTILINE_MESSAGES)
        self.messages = utils.parse(logs)
    
    def test_sent_messages_count(self):
        self.assertEqual(history_analysis.sent_messages_count(self.messages, "john"), 4)
        self.assertEqual(history_analysis.sent_messages_count(self.messages, "jane"), 2)
        self.assertEqual(history_analysis.sent_messages_count(self.messages, "brian"), 0)

    def test_sent_word_count(self):
        self.assertEqual(history_analysis.sent_word_count(self.messages, "john", "you"), 2)
        self.assertEqual(history_analysis.sent_word_count(self.messages, "john", "you"), 2)
        self.assertEqual(history_analysis.sent_word_count(self.messages, "jane", "hate"), 0)

    def test_sent_profanities_count(self):
        self.assertEqual(history_analysis.sent_profanities_count(self.messages, "john", PROFANITIES), 1)
        self.assertEqual(history_analysis.sent_profanities_count(self.messages, "jane", PROFANITIES), 0)

    def test_sent_emojis_count(self):
        self.assertEqual(history_analysis.sent_emojis_count(self.messages, "john"), 2)
        self.assertEqual(history_analysis.sent_emojis_count(self.messages, "jane"), 3)

    def test_received_emojis_count(self):
        self.assertEqual(history_analysis.received_emojis_count(self.messages, "john"), 3)
        self.assertEqual(history_analysis.received_emojis_count(self.messages, "jane"), 2)
    
    def test_received_angry_face_emoji_count(self):
        self.assertEqual(history_analysis.received_angry_face_emoji_count(self.messages, "john"), 0)
        self.assertEqual(history_analysis.received_angry_face_emoji_count(self.messages, "jane"), 2)