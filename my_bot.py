# bigwordbot

import praw
from PyDictionary import PyDictionary
import enchant

# create the objects from the imported modules

# reddit api login
reddit = praw.Reddit(client_id='JCwUD3jqy46VHg',
                     client_secret='	AKgi8heRCi1zrEKM9nDNNQQPo6Y',
                     username='wordbot',
                     password='wordbot',
                     user_agent='wordude by /u/tom')

# dictionary and word check
dictionary = PyDictionary()
d = enchant.Dict("en_US")

# check if the word is real
def isWord(word):
    return d.check(word)

# the subreddits you want your bot to live on
subreddit = reddit.subreddit('words')

# phrase to activate the bot
keyphrase = '!wordbot '

# look for phrase and reply appropriately
for comment in subreddit.stream.comments():
    if keyphrase in comment.body:
        word = comment.body.replace(keyphrase, '')
        try:
            if isWord(word):
                # get meaning as object, get the index of a sentence and reply it
                words = dictionary.meaning(word)
                reply = [item[0] for item in words.values()]
                comment.reply(word + ': '  + reply[0])
                print('posted')
            else:
                reply = 'This is not a word.'
                comment.reply(reply)
                print('posted')
        except:
print('too frequent')
