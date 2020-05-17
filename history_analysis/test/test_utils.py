from unittest import TestCase, mock
from pathlib import Path
from history_analysis import utils
from . import TEST_HISTORY_FILE, TEST_HISTORY_LOGS

DATA = "21/09/19, 14:04 - John: Hello\n21/09/2019, 16:12 - Jane: Hi"

class TestUtils(TestCase):
    def get_messages(self):
        return {
            "john": ["Hello! Do you still hate me?", "fuck!", "😡😡", "lol! You really got me there. Thanks!"],
            "jane": ["Yes!\nIf you are in a room with Hitler and I was given two bullets,\nI'd shoot you twice!!", "😂😂😂Gotcha!\nI'm kidding. We are good!"]
        }
    @mock.patch("history_analysis.utils.open", new_callable=mock.mock_open)
    def test_load_unexisting_file(self, mock_history_file):
        utils.load_file(TEST_HISTORY_FILE)
        mock_history_file.assert_not_called
    
    @mock.patch("history_analysis.utils.open", new_callable=mock.mock_open, read_data=DATA)
    def test_load_existing_file(self, mock_history_file):
        logs = utils.load_file(TEST_HISTORY_FILE)
        mock_history_file.assert_called_with(Path(__file__).parent.joinpath("./data/history.txt"), encoding='utf-8')
        self.assertEqual(len(logs), 2)
        self.assertListEqual(logs, ["21/09/19, 14:04 - John: Hello\n", "21/09/2019, 16:12 - Jane: Hi"])

    def test_parse(self):
        
        self.assertDictEqual(utils.parse(TEST_HISTORY_LOGS), self.get_messages())