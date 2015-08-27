__author__ = 'Petter'
import praw
import os

user_agent = ("SearchBot 1.0")
r = praw.Reddit(user_agent=user_agent)


subredditInput = raw_input('Enter the subreddit you would like to search. Note: Only type in what comes after reddit.com/r/ : ')
try:
    type = r.get_subreddit(subredditInput).subreddit_type
except:
    print "Invalid subreddit!"
    exit()

subreddit = r.get_subreddit(subredditInput)
searchPhrase = raw_input('Enter what you want to search for on the subreddit: ')
print ("Please wait for about 20 seconds. Any comments containing the phrase will be linked here.")

for submission in subreddit.get_hot(limit = 10):
    forest_comments = submission.comments
    for comment in forest_comments:
        try:
            if searchPhrase not in comment.body:
                continue
            else:
                print "URL " + comment.permalink
        except AttributeError:
            pass
print ("Done!")