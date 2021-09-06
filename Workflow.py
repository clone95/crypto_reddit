import os
import json

from RedditDownloader import RedditDownloader
# Opening JSON file
config_file = open('config.json')

downloader = RedditDownloader(json.load(config_file))

downloader.create_dataset()

#import praw
#
#reddit = praw.Reddit(
#    client_id="7pzwfJp0nlisZ688tKjTNA",
#    client_secret="Kkal2oclz2d09fggBv1YvzBGfe7ugA",
#    user_agent="my user agent",
#    username="clone290595",
#    password="scottex95",
#)
#
## continued from code above
#
#for submission in reddit.subreddit("CryptoCurrency").hot(limit=100):
#    print(submission.title)
#
## Output: 10 submissions