import os
import praw
from praw.models import MoreComments


class RedditDownloader():
    def __init__(self, config):
            
        self.subreddit = config['subreddit']
        self.limit = config['limit']
        self.root = config['root']
        self.dataset_type = config['dataset_type']

    def create_dataset(self):

        client = praw.Reddit(
        client_id="7pzwfJp0nlisZ688tKjTNA",
        client_secret="Kkal2oclz2d09fggBv1YvzBGfe7ugA",
        user_agent="my user agent",
        username="clone290595",
        password="scottex95",
        )

        with open(os.path.join(self.root, self.dataset_type, self.subreddit + '.txt'), 'w+') as file:
            for submission in client.subreddit(self.subreddit).hot(limit=10):
                if submission.title.startswith("Daily"):
         
                    for top_level_comment in submission.comments:
                        if isinstance(top_level_comment, MoreComments):
                            continue
                        try:
                            file.write(str(top_level_comment.body) + "\n")
                        except:
                            continue