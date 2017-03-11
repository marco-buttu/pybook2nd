import fnmatch
import os

def file_finder(pattern: str, top_dir: str):
    for path, dirs, files in os.walk(top_dir):
        for name in fnmatch.filter(files, pattern):
            yield os.path.join(path, name)
