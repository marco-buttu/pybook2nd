from operator import itemgetter

def sortdict(dictionary):
    return sorted(dictionary.items(), key=itemgetter(-1))
