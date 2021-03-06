from unittest import TestCase, mock
from history_analysis import utils, history_analysis
from . import TEST_HISTORY_LOGS, PROFANITIES

class TestHistoryAnalysis(TestCase):
    def setUp(self):
        self.messages = utils.parse(TEST_HISTORY_LOGS)
    
    def test_sent_messages_count(self):
        self.assertEqual(history_analysis.sent_messages_count(self.messages, "john"), 4)
        self.assertEqual(history_analysis.sent_messages_count(self.messages, "jane"), 2)
        self.assertEqual(history_analysis.sent_messages_count(self.messages, "brian"), 0)
    
    def test_sent_word_count(self):
        self.assertEqual(history_analysis.sent_word_count(self.messages, "john", "you"), 2)
        self.assertEqual(history_analysis.sent_word_count(self.messages, "john", "you"), 2)
        self.assertEqual(history_analysis.sent_word_count(self.messages, "jane", "hate"), 0)

    @mock.patch('history_analysis.history_analysis.sent_word_count', return_value=2)
    def test_sent_profanities_count(self, mock_sent_word_count):
        expected_calls = [
            mock.call(self.messages, "john", "fuck"), 
            mock.call(self.messages, "john", "merde")
        ]
        res = history_analysis.sent_profanities_count(self.messages, "john", PROFANITIES)
        mock_sent_word_count.assert_has_calls(expected_calls)
        self.assertEqual(mock_sent_word_count.call_count, 2)
        self.assertEqual(res, 4)

    def test_sent_emojis_count(self):
        self.assertEqual(history_analysis.sent_emojis_count(self.messages, "john"), 2)
        self.assertEqual(history_analysis.sent_emojis_count(self.messages, "jane"), 3)

    def test_received_emojis_count(self):
        self.assertEqual(history_analysis.received_emojis_count(self.messages, "john"), 3)
        self.assertEqual(history_analysis.received_emojis_count(self.messages, "jane"), 2)
    
    @mock.patch('history_analysis.history_analysis.sent_word_count', return_value=0)
    def test_received_angry_face_emoji_count(self, mock_sent_word_count):
        res = history_analysis.received_angry_face_emoji_count(self.messages, "john")
        self.assertEqual(mock_sent_word_count.call_count, 1)
        self.assertEqual(res, 0)

    @mock.patch('history_analysis.history_analysis.sent_word_count', return_value=1)
    def test_interest_words_count(self, mock_sent_word_count):
        expected_calls = [
            mock.call(self.messages, "john", "first_word"), 
            mock.call(self.messages, "jane", "first_word"),
            mock.call(self.messages, "john", "second_word"),
            mock.call(self.messages, "jane", "second_word")
        ]
        res = history_analysis.interest_words_count(self.messages, ["first_word", "second_word"])
        mock_sent_word_count.assert_has_calls(expected_calls)
        self.assertEqual(mock_sent_word_count.call_count, 4)
        self.assertEqual(res, 4)