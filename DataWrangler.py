import os
import pandas as pd


class DataWrangler():
    def __init__(self, config, destination_filename):
        
        self.source_file = destination_filename
        
    def process_data(self):
        
        with open(self.source_file) as source_file:
            raw_text = source_file.read()

