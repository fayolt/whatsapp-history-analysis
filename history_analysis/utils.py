import re
from collections import defaultdict
from pathlib import Path

USER_MESSAGE_PATTERN = r"^(?:\d+\/\d+\/\d{2,4}, \d+:\d{2}(?: am| pm)?) - (?P<name>.*): (?P<message>.+)$"
SYSTEM_MESSAGE_PATTERN = r"^(?:\d+\/\d+\/\d{2,4}, \d+:\d{2}(?: am| pm)?) - (?P<message>.+)$"

def load_file(file_path):
    try:
        path = Path(__file__).parent.joinpath(file_path)
        with open(path, encoding='utf-8') as history_log_file:
            history_log_list = history_log_file.readlines()
        return history_log_list
    except:
        print("Kindly check that the chat history file exists in the ./data directory and is named 'history.txt'")
        print("Exiting now ...")
        exit()

def parse(history_log_list):
    messages = defaultdict(list)
    previous_key = ""
    for log in history_log_list:
        match = re.search(USER_MESSAGE_PATTERN, log, re.IGNORECASE)
        if match:
            messages[match.group('name').lower()].append(match.group('message').strip())
            previous_key = match.group('name').lower()
        elif not re.search(SYSTEM_MESSAGE_PATTERN, log, re.IGNORECASE):
            if previous_key in messages:
                messages[previous_key][-1] += "\n" + log.strip()
    return messages