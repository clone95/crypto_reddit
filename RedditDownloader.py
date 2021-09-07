import os
from datetime import date
import praw
from Utils import ensure_dir
from praw.models import MoreComments


class RedditDownloader():
    def __init__(self, config):
            
        today = date.today().strftime("%d-%m-%Y")
        self.subreddit = config['subreddit']
        self.limit = config['limit']
        self.root = config['root']
        self.dataset_type = config['dataset_type']
        self.client_id=config['client_id']
        self.client_secret=config['client_secret']
        self.user_agent=config['user_agent']
        self.username=config['username']
        self.password=config['password']
        self.destination_folder = os.path.join(self.root, "raw", self.dataset_type)
        self.destination_filename = self.destination_folder + "/" + self.subreddit+  f'{today}.txt'


    def create_comments_dataset(self):

        client = praw.Reddit(
        client_id=self.client_id,
        client_secret=self.client_secret,
        user_agent=self.user_agent,
        username=self.username,
        password=self.password,
        )

        print(f"Downloading in {self.destination_folder}")
        ensure_dir(self.destination_folder)
        with open(self.destination_filename, 'w+') as file:
            for submission in client.subreddit(self.subreddit).hot(limit=10):
                if submission.title.startswith("Daily"):

                    for top_level_comment in submission.comments:
                        if isinstance(top_level_comment, MoreComments):
                            continue
                        try:
                            file.write(str(top_level_comment.body) + "\n")
                        except:
                            continue
        
