import praw

user_agent = ("PyEng mich 0.1")

r = praw.Reddit(user_agent = user_agent)

subreddit = r.get_subreddit("hearthstone")

print "URL" + subreddit._url

for submission in subreddit.get_hot(limit = 1):
    print "Title: ", submission.title
    print "Text: ", submission.selftext
    print "Score: ", submission.score
    print "---------------------------------\n"