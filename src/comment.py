__author__ = 'Petter'
import praw
import pdb
import re
import os
from config_skel import *

if not os.path.isfile("config_skel.py"):
    print("No username / pw found")
    exit(1)

user_agent = ("PyFor Eng bot 0.1")
r = praw.Reddit(user_agent=user_agent)
r.login(REDDIT_USERNAME, REDDIT_PASSWORD)

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to=[]
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = filter(None, posts_replied_to)

subreddit = r.get_subreddit('pythonforengineers')
for submission in subreddit.get_hot(limit=5):
    if submission.id not in posts_replied_to:
        if re.search("ayyy", submission.title, re.IGNORECASE):
            submission.add_comment("lmao")

            print("Bot replying to : ", submission.title)
            posts_replied_to.append(submission.id)

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")