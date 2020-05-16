import re

from emoji import UNICODE_EMOJI

ANGRY_FACE_EMOJI = "\U0001F621"

def sent_messages_count(messages, name):
    return len(messages[name])

def sent_word_count(messages, name, word):
    separator = '\n'
    return separator.join(messages[name]).lower().count(word.lower())

def sent_profanities_count(messages, name, profanities):
    count = 0
    for profanity in profanities:
        count += sent_word_count(messages, name, profanity)
    return count

def sent_emojis_count(messages, name):
    count = 0
    separator = '\n'
    message_string = separator.join(messages[name])
    for emoji in UNICODE_EMOJI:
        count += message_string.count(emoji)
    return count

def received_emojis_count(messages, name):
    count = 0
    for a_name in messages:
        if name != a_name: 
            count += sent_emojis_count(messages, a_name)
    return count

def received_angry_face_emoji_count(messages, name):
    count = 0
    for a_name in messages:
        if name != a_name: 
            count += sent_word_count(messages, a_name, ANGRY_FACE_EMOJI)
    return count

def interest_words_count(messages, interest_list):
    count = 0
    for word in interest_list:
        for name in messages:
            count += sent_word_count(messages, name, word)
    return count

