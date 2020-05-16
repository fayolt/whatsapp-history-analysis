from history_analysis import utils
from history_analysis import history_analysis as ha

CHAT_HISTORY_FILEPATH = "../data/history.txt"
def run():
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
    print("Total number of messages sent {}.".format(ha.sent_messages_count(messages, username)))
	
    # Total number of times the user sent "lol".
    print("Total number of times the user sent 'lol': {}.".format(ha.sent_word_count(messages, username, "lol")))
    
    # Total number of times the user sent "lmao".
    print("Total number of times the user sent 'lmao': {}.".format(ha.sent_word_count(messages, username, "lmao")))
	
    # Total number of profanities the user sent.
    print("Total number of profanities the user sent: {}.".format(ha.sent_profanities_count(messages, username, PROFANITIES)))

    # Total number of times the user sent emojis.
    print("Total number of times the user sent emojis: {}.".format(ha.sent_emojis_count(messages, username)))
	
    # Total number of times the user recieved emojis.
    print("Total number of times the user recieved emojis: {}.".format(ha.received_emojis_count(messages, username)))
	
    # Total number of times the user recieved the angry 😡 emoji.
    print("Total number of times the user recieved the angry 😡 emoji: {}.".format(ha.received_angry_face_emoji_count(messages, username)))

    # Total number of times the user sent and recieved the words 
    # "amen", "akpe", "merci", "nagode", "imela", "thanks", "thank you", "alhamdulillah", "shukran"
    print("Total number of times the user sent and recieved the words"
            + "'amen', 'akpe', 'merci', 'nagode', 'imela', 'thanks', 'thank you', 'alhamdulillah'," 
            + "'shukran': {}.".format(ha.interest_words_count(messages, INTEREST_LIST)))