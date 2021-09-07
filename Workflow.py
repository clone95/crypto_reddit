import os
import json
import time
from RedditDownloader import RedditDownloader
from DataWrangler import DataWrangler


def main():
    config_file = open('WorkflowConfig.json')
    config = json.load(config_file)

    launch_workflow(config)
    print("Worflow completed.")

def launch_workflow(config):
    downloader = RedditDownloader(config)
    #destination_filename = downloader.create_comments_dataset()

    data_wrangler = DataWrangler(config, downloader.destination_filename)
    data_wrangler.process_data()
        
if __name__ == '__main__':
    main()
    