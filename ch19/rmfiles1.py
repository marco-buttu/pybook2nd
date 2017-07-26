import os

def remove_recursively(from_='.', suffix='.pyc'):
    for root, dirs, files in os.walk(from_):
        found = [file for file in files if file.endswith(suffix)]
        for file in found:
            os.remove(os.path.join(root, file))
            print(os.path.join(root, file), 'file removed')

remove_recursively()
