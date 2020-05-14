# -*- coding: UTF-8 -*-
import re 
from collections import defaultdict

def load_file(file_name):
    history_file = open(file_name, encoding='utf8')
    history_list = history_file.readlines()
    return history_list

def parse(history_log):
    user_message_pattern = r"^(\d+\/\d+\/\d+, \d{2}:\d{2}( am| pm)?) - (.*): (.+)$"
    system_message_pattern = r"^(\d+\/\d+\/\d+, \d{2}:\d{2}( am| pm)?) - (.+)$"
    messages = defaultdict(list)
    previous_key = ""
    for log in history_log:
        match = re.search(user_message_pattern, log)
        if match is not None:
            # messages.append([match.group(3), match.group(4)])
            messages[match.group(3).lower()].append(match.group(4))
            previous_key = match.group(3).lower()
        elif not re.search(system_message_pattern, log) :
            # messages[-1][-1] += log
            messages[previous_key][-1] += log
    return messages