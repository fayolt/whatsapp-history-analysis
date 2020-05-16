import re 
from collections import defaultdict
from pathlib import Path

def load_file(file_path):
    path = Path(__file__).parent.joinpath(file_path)
    with path.open(encoding='utf-8') as history_log_file:
        history_log_list = history_log_file.readlines()
    return history_log_list

def parse(history_log):
    user_message_pattern = r"^(\d+\/\d+\/\d{2,4}, \d+:\d{2}( am| pm)?) - (.*): (.+)$"
    system_message_pattern = r"^(\d+\/\d+\/\d{2,4}, \d+:\d{2}( am| pm)?) - (.+)$"
    messages = defaultdict(list)
    previous_key = ""
    for log in history_log:
        match = re.search(user_message_pattern, log, re.IGNORECASE)
        if match is not None:
            messages[match.group(3).lower()].append(match.group(4).strip())
            previous_key = match.group(3).lower()
        elif not re.search(system_message_pattern, log, re.IGNORECASE) :
            messages[previous_key][-1] += "\n" + log.strip()
    return messages