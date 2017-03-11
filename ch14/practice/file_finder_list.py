import fnmatch
import os


def file_finder(pattern: str, top_dir: str):
    result = []
    for path, dirs, files in os.walk(top_dir):
        for name in fnmatch.filter(files, pattern):
            result.append(os.path.join(path, name))
    return result
