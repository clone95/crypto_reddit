import os

def ensure_dir(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return None