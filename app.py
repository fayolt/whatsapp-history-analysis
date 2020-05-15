import utils
import re
from emoji import UNICODE_EMOJI

ANGRY_FACE_EMOJI = "\U0001F621"
CHAT_HISTORY_FILEPATH = "data/history.txt"

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

if __name__ == "__main__":
    # List of words of interst
    INTEREST_LIST = ["amen", "akpe", "merci", "nagode", "imela", "thanks", "thank you", "alhamdulillah", "shukran"]
    
    # List of profanities to check for are "fuck", "merde", "putain", "ass"
    PROFANITIES = ["fuck", "merde", "putain", "ass"]
    
    # Read the chat history line by line
    history_logs = utils.load_file(CHAT_HISTORY_FILEPATH)
    
    # Creatte a dictionary of messages from the logs, 
    # dictionary keys are usernames and values are the list of messages sent by the given user
    messages = utils.parse(history_logs)
    username = input("Enter a username: ").lower()
    
    # Total number of messages sent.
    print("Total number of messages sent {}.".format(sent_messages_count(messages, username)))
	
    # Total number of times the user sent "lol".
    print("Total number of times the user sent 'lol': {}.".format(sent_word_count(messages, username, "lol")))
    
    # Total number of times the user sent "lmao".
    print("Total number of times the user sent 'lmao': {}.".format(sent_word_count(messages, username, "lmao")))
	
    # Total number of profanities the user sent.
    print("Total number of profanities the user sent: {}.".format(sent_profanities_count(messages, username, PROFANITIES)))

    # Total number of times the user sent emojis.
    print("Total number of times the user sent emojis: {}.".format(sent_emojis_count(messages, username)))
	
    # Total number of times the user recieved emojis.
    print("Total number of times the user recieved emojis: {}.".format(received_emojis_count(messages, username)))
	
    # Total number of times the user recieved the angry 😡 emoji.
    print("Total number of times the user recieved the angry 😡 emoji: {}.".format(received_angry_face_emoji_count(messages, username)))

    # Total number of times the user sent and recieved the words 
    # "amen", "akpe", "merci", "nagode", "imela", "thanks", "thank you", "alhamdulillah", "shukran"
    print("Total number of times the user sent and recieved the words"
            + "'amen', 'akpe', 'merci', 'nagode', 'imela', 'thanks', 'thank you', 'alhamdulillah'," 
            + "'shukran': {}.".format(interest_words_count(messages, INTEREST_LIST)))

