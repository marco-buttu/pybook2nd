import fnmatch
import os


def file_finder(pattern: str, top_dir: str):
    result = []
    for path, _, files in os.walk(top_dir):
        for file_name in fnmatch.filter(files, pattern):
            result.append(file_name)
    return result
