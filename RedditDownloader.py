import os
from datetime import date
import praw
from Utils import ensure_dir
from praw.models import MoreComments


class RedditDownloader():
    def __init__(self, config):
            
        self.subreddit = config['subreddit']
        self.limit = config['limit']
        self.root = config['root']
        self.dataset_type = config['dataset_type']
        self.client_id=config['client_id']
        self.client_secret=config['client_secret']
        self.user_agent=config['user_agent']
        self.username=config['username']
        self.password=config['password']

    def create_comments_dataset(self):

        client = praw.Reddit(
        client_id=self.client_id,
        client_secret=self.client_secret,
        user_agent=self.user_agent,
        username=self.username,
        password=self.password,
        )

        today = date.today().strftime("%d-%m-%Y")
        destination_folder = os.path.join(self.root, "raw", self.dataset_type)
        print(f"Downloading in {destination_folder}")
        ensure_dir(destination_folder)

        with open(destination_folder + "/" + self.subreddit+  f'{today}.txt', 'w+') as file:
            for submission in client.subreddit(self.subreddit).hot(limit=10):
                if submission.title.startswith("Daily"):

                    for top_level_comment in submission.comments:
                        if isinstance(top_level_comment, MoreComments):
                            continue
                        try:
                            file.write(str(top_level_comment.body) + "\n")
                        except:
                            continue