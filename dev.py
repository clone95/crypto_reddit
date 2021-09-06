from re import sub
import praw 

reddit = praw.Reddit(
        client_id="7pzwfJp0nlisZ688tKjTNA",
        client_secret="Kkal2oclz2d09fggBv1YvzBGfe7ugA",
        user_agent="my user agent",
        username="clone290595",
        password="scottex95",
        )

for submission in reddit.subreddit("CryptoCurrency").hot(limit=3):
    if submission.title.startswith("Daily"):
        print(submission.title)

# Output: 10 submissions