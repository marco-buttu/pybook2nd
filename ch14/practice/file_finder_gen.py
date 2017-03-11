import fnmatch
import os

def file_finder(pattern: str, top_dir: str):
    for path, _, files in os.walk(top_dir):
        for file_name in fnmatch.filter(files, pattern):
            yield file_name
