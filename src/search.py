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

if not os.path.isfile("postsRead.txt"):
    print("postsRead.txt not found")
    exit(1)
else:
    with open("postsRead.txt", "r") as f:
        posts_searched = f.read()
        posts_searched = posts_searched.split("\n")
        posts_searched = filter(None, posts_searched)

for submission in subreddit.get_hot(limit = 10):
    if posts_searched.__contains__(submission.id):
        print( "already in .txt " + submission.title)
        continue
    else:
        forest_comments = submission.comments
        for comment in forest_comments:
            try:
                if searchPhrase not in comment.body:
                    continue
                else:
                    print "URL " + comment.permalink
            except AttributeError:
                pass
    posts_searched.append(submission.id)
with open("postsRead.txt", "w") as f:
    for post_id in posts_searched:
        f.write(post_id + "\n")