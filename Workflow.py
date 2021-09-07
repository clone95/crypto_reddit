import os
import json
import time
from RedditDownloader import RedditDownloader


def main():
    config_file = open('config.json')
    downloader = RedditDownloader(json.load(config_file))
    downloader.create_comments_dataset()
    
if __name__ == '__main__':
    main()
    