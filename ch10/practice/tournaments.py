import itertools


def tournaments(teams):
    return [*itertools.combinations(teams, 3)]
